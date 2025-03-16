import sys
import os
import datetime
from contextlib import contextmanager

class LogCapture:
    """Class to capture console output and redirect it to both console and file."""
    
    def __init__(self, log_file=None):
        """
        Initialize the log capture system.
        
        Args:
            log_file (str, optional): Path to the log file. If None, a timestamped file
                                     in ./backend/models/logs/ will be created.
        """
        # Create logs directory if it doesn't exist
        log_dir = './backend/models/logs/'
        os.makedirs(log_dir, exist_ok=True)
        
        if log_file is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = f"{log_dir}model_log_{timestamp}.txt"
        
        self.log_file = log_file
        self.terminal_stdout = sys.stdout
        self.terminal_stderr = sys.stderr
        self.log = None
    
    def start(self):
        """Start capturing output."""
        self.log = open(self.log_file, 'a', encoding='utf-8')
        sys.stdout = self
        sys.stderr = self
        print(f"\n{'='*50}")
        print(f"Log started at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*50}\n")
        return self
    
    def stop(self):
        """Stop capturing output and close the log file."""
        print(f"\n{'='*50}")
        print(f"Log ended at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*50}\n")
        
        sys.stdout = self.terminal_stdout
        sys.stderr = self.terminal_stderr
        
        if self.log:
            self.log.close()
            self.log = None
            print(f"Log saved to: {self.log_file}")
    
    def write(self, message):
        """Write to both terminal and log file."""
        self.terminal_stdout.write(message)
        if self.log:
            self.log.write(message)
    
    def flush(self):
        """Flush both outputs."""
        self.terminal_stdout.flush()
        if self.log:
            self.log.flush()


@contextmanager
def capture_logs(log_file=None, operation_name=None):
    """
    Context manager for capturing logs.
    
    Args:
        log_file (str, optional): Path to log file. If None, generates timestamped file.
        operation_name (str, optional): Name of the operation being logged.
    
    Example:
        with capture_logs(operation_name='Model Training'):
            # Code that generates console output
            model = train_model()
    """
    logger = LogCapture(log_file)
    logger.start()
    
    if operation_name:
        print(f"Operation: {operation_name}")
        print(f"{'-'*50}\n")
    
    try:
        yield logger
    finally:
        logger.stop()


def log_model_operation(func):
    """
    Decorator to automatically log output from model operations.
    
    Args:
        func: The function to wrap with logging
    
    Example:
        @log_model_operation
        def train_my_model():
            print("Training model...")
            # training code
    """
    def wrapper(*args, **kwargs):
        operation_name = func.__name__.replace('_', ' ').title()
        
        # Create timestamped log file
        log_dir = './backend/models/logs/'
        os.makedirs(log_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f"{log_dir}{func.__name__}_{timestamp}.txt"
        
        with capture_logs(log_file, operation_name):
            result = func(*args, **kwargs)
        
        return result
    
    return wrapper


def get_latest_log(log_dir='./backend/models/logs/'):
    """
    Get the content of the most recent log file.
    
    Args:
        log_dir (str): Directory containing log files
        
    Returns:
        str: Content of the most recent log file
    """
    try:
        os.makedirs(log_dir, exist_ok=True)
        
        log_files = [os.path.join(log_dir, f) for f in os.listdir(log_dir) 
                    if f.endswith('.txt')]
        
        if not log_files:
            return "No log files found."
        
        latest_log = max(log_files, key=os.path.getmtime)
        
        with open(latest_log, 'r', encoding='utf-8') as f:
            return f.read()
    
    except Exception as e:
        return f"Error retrieving log: {e}"


def main():
    log_dir = './backend/models/logs/'
    os.makedirs(log_dir, exist_ok=True)
    
    with capture_logs(operation_name="Test Logging"):
        print("This is a test log message")
        print("It will be captured and saved to a file")
        
    print("Check the logs directory for the output")


if __name__ == "__main__":
    main()