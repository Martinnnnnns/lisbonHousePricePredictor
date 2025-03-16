import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import cross_val_score, KFold
from model_training import load_processed_data, prepare_data_for_modeling, split_data

# Set non-interactive backend to prevent plots from being displayed
plt.switch_backend('Agg')

def evaluate_model(model, X_test, y_test, X_train=None, y_train=None, model_name="Model", cv=5, models_dir='./backend/models/saved_models/'):
    """
    Args:
        model: Trained scikit-learn model object to evaluate
        X_test (pandas.DataFrame): Test feature set
        y_test (pandas.Series): Test target values
        X_train (pandas.DataFrame, optional): Training feature set for cross-validation
        y_train (pandas.Series, optional): Training target values for cross-validation
        model_name (str): Name of the model for display purposes
        cv (int): Number of cross-validation folds
        models_dir (str): Directory containing saved models
    
    Returns:
        dict: Dictionary containing evaluation metrics and predictions
    """
    y_pred = model.predict(X_test)
    
    # Calculate metrics on test set
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Calculate additional metrics
    mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100  # Mean Absolute Percentage Error
    
    print(f"\n{model_name} Evaluation Results (Test Set):")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")
    print(f"R² Score: {r2:.4f}")
    
    # Perform cross-validation if training data is provided
    cv_results = {}
    if X_train is not None and y_train is not None:
        print(f"\n{model_name} Cross-Validation Results ({cv} folds):")
        
        # Define cross-validation strategy
        kf = KFold(n_splits=cv, shuffle=True, random_state=42)
        
        # Cross-validation for R²
        cv_r2 = cross_val_score(model, X_train, y_train, cv=kf, scoring='r2')
        print(f"Cross-validated R² Score: {cv_r2.mean():.4f} ± {cv_r2.std():.4f}")
        
        # Cross-validation for negative MSE (scikit-learn uses negative MSE)
        cv_mse = -cross_val_score(model, X_train, y_train, cv=kf, scoring='neg_mean_squared_error')
        cv_rmse = np.sqrt(cv_mse)
        print(f"Cross-validated RMSE: {cv_rmse.mean():.2f} ± {cv_rmse.std():.2f}")
        
        # Cross-validation for negative MAE
        cv_mae = -cross_val_score(model, X_train, y_train, cv=kf, scoring='neg_mean_absolute_error')
        print(f"Cross-validated MAE: {cv_mae.mean():.2f} ± {cv_mae.std():.2f}")
        
        cv_results = {
            'cv_r2_mean': cv_r2.mean(),
            'cv_r2_std': cv_r2.std(),
            'cv_rmse_mean': cv_rmse.mean(),
            'cv_rmse_std': cv_rmse.std(),
            'cv_mae_mean': cv_mae.mean(),
            'cv_mae_std': cv_mae.std()
        }
    
    # Combine test results and cross-validation results
    results = {
        'model_name': model_name,
        'rmse': rmse,
        'mae': mae,
        'mape': mape,
        'r2': r2,
        'predictions': y_pred
    }
    
    if cv_results:
        results.update(cv_results)
    
    return results

def plot_predictions(y_test, y_pred, model_name="Model", save_path=None):
    """
    Args:
        y_test (pandas.Series): Actual target values
        y_pred (numpy.ndarray): Predicted target values
        model_name (str): Name of the model for plot titles
        save_path (str, optional): Directory to save plots
    
    Returns:
        None: Creates and saves plots for actual vs predicted values, residuals, and residual distribution
    """
    plt.figure(figsize=(10, 6), num=f'{model_name}: Actual vs Predicted House Prices')
    plt.scatter(y_test, y_pred, alpha=0.7)
    
    # Scatter Plot
    min_val = min(min(y_test), min(y_pred))
    max_val = max(max(y_test), max(y_pred))
    plt.plot([min_val, max_val], [min_val, max_val], 'r--')
    
    plt.title(f'{model_name}: Actual vs Predicted House Prices')
    plt.xlabel('Actual Prices')
    plt.ylabel('Predicted Prices')
    plt.grid(True)
    
    if save_path:
        os.makedirs(save_path, exist_ok=True)
        plt.savefig(f"{save_path}/{model_name.lower().replace(' ', '_')}_predictions.png", dpi=300, bbox_inches='tight')
    
    plt.close()
    
    # Residuals Plot
    plt.figure(figsize=(10, 6), num=f'{model_name}: Residuals Plot')
    residuals = y_test - y_pred
    plt.scatter(y_pred, residuals, alpha=0.7)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.title(f'{model_name}: Residuals Plot')
    plt.xlabel('Predicted Prices')
    plt.ylabel('Residuals')
    plt.grid(True)
    
    if save_path:
        plt.savefig(f"{save_path}/{model_name.lower().replace(' ', '_')}_residuals.png", dpi=300, bbox_inches='tight')
    
    plt.close()
    
    # Histogram
    plt.figure(figsize=(10, 6), num=f'{model_name}: Distribution of Residuals')
    sns.histplot(residuals, kde=True)
    plt.title(f'{model_name}: Distribution of Residuals')
    plt.xlabel('Residual Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    
    if save_path:
        plt.savefig(f"{save_path}/{model_name.lower().replace(' ', '_')}_residuals_dist.png", dpi=300, bbox_inches='tight')
    
    plt.close()

def plot_feature_importance(model, feature_names, model_name="Model", save_path=None, top_n=15):
    """
    Args:
        model: Trained scikit-learn model object with feature_importances_ attribute
        feature_names (list): List of feature names
        model_name (str): Name of the model for plot title
        save_path (str, optional): Directory to save plot
        top_n (int): Number of top features to display
    
    Returns:
        pandas.Series or None: Feature importance values or None if model doesn't support feature importance
    """
    if hasattr(model, 'feature_importances_'):
        importance = pd.Series(model.feature_importances_, index=feature_names)
        
        plt.figure(figsize=(12, 8), num=f'Top {top_n} Important Features - {model_name}')
        importance.sort_values(ascending=False).head(top_n).plot(kind='barh')
        plt.title(f'Top {top_n} Important Features - {model_name}')
        plt.tight_layout()
        
        if save_path:
            os.makedirs(save_path, exist_ok=True)
            plt.savefig(f"{save_path}/{model_name.lower().replace(' ', '_')}_feature_importance.png", dpi=300, bbox_inches='tight')
        
        plt.close()
        return importance
    else:
        print(f"Model {model_name} doesn't have feature_importances_ attribute.")
        return None

def compare_models(evaluation_results, save_path=None, metrics=None):
    """
    Args:
        evaluation_results (list): List of dictionaries with evaluation metrics for each model
        save_path (str, optional): Directory to save comparison plot
        metrics (list, optional): List of metrics to compare, defaults to ['rmse', 'r2', 'mae']
    
    Returns:
        pandas.DataFrame: DataFrame containing model comparison metrics
    """
    if metrics is None:
        metrics = ['rmse', 'r2', 'mae']
    
    # Extract data for plotting
    models = [result['model_name'] for result in evaluation_results]
    
    # DataFrame for easy plotting
    df = pd.DataFrame({
        'Model': models
    })
    
    for metric in metrics:
        if metric in evaluation_results[0]:
            df[metric] = [result[metric] for result in evaluation_results]
    
    if 'r2' in df.columns:
        df = df.sort_values('r2', ascending=False).reset_index(drop=True)
    
    plt.figure(figsize=(14, 10), num='Model Comparison')
    
    for i, metric in enumerate(metrics, 1):
        if metric in df.columns:
            plt.subplot(len(metrics), 1, i)
            
            if metric == 'r2':
                color = 'skyblue'
                plt.barh(df['Model'], df[metric], color=color)
                plt.xlim(0, 1) 
            else:
                color = 'salmon'
                plt.barh(df['Model'], df[metric], color=color)
            
            metric_display = {
                'rmse': 'RMSE (Root Mean Squared Error)',
                'mae': 'MAE (Mean Absolute Error)',
                'mape': 'MAPE (Mean Absolute Percentage Error)',
                'r2': 'R² Score',
                'cv_rmse_mean': 'CV RMSE (Cross-validated)',
                'cv_mae_mean': 'CV MAE (Cross-validated)',
                'cv_r2_mean': 'CV R² Score (Cross-validated)'
            }
            
            plt.xlabel(metric_display.get(metric, metric))
            plt.title(f'Model Comparison - {metric_display.get(metric, metric)}')
            plt.grid(axis='x')
    
    plt.tight_layout()
    
    if save_path:
        os.makedirs(save_path, exist_ok=True)
        plt.savefig(f"{save_path}/model_comparison.png", dpi=300, bbox_inches='tight')
    
    plt.close()
    
    # Create a summary table
    summary_df = df.set_index('Model')
    print("\nModel Comparison Summary:")
    print(summary_df)
    
    # Add model ranking across metrics
    for metric in metrics:
        if metric.endswith('r2') or metric.endswith('r2_mean'): 
            summary_df[f'{metric}_rank'] = summary_df[metric].rank(ascending=False)
        else:
            summary_df[f'{metric}_rank'] = summary_df[metric].rank(ascending=True)
    
    rank_columns = [f'{metric}_rank' for metric in metrics]
    summary_df['avg_rank'] = summary_df[rank_columns].mean(axis=1)
    
    ranked_df = summary_df.sort_values('avg_rank')
    
    print("\nModel Ranking (lower rank is better):")
    print(ranked_df[rank_columns + ['avg_rank']])
    
    # Get the overall best model based on average rank
    best_overall_model = ranked_df['avg_rank'].idxmin()
    
    # Get this model's individual ranks
    best_model_ranks = {}
    for metric in metrics:
        rank_col = f'{metric}_rank'
        best_model_ranks[metric] = ranked_df.loc[best_overall_model, rank_col]
    
    print(f"\nBest overall model based on ranking: {best_overall_model}")
    print(f"Individual ranks for {best_overall_model}:")
    for metric, rank in best_model_ranks.items():
        metric_display = {
            'rmse': 'RMSE',
            'mae': 'MAE',
            'mape': 'MAPE',
            'r2': 'R² Score',
            'cv_rmse_mean': 'CV RMSE',
            'cv_mae_mean': 'CV MAE',
            'cv_r2_mean': 'CV R² Score'
        }
        print(f"  - {metric_display.get(metric, metric)}: Rank {rank:.1f}")
    
    # Identify the best model for each metric
    best_models = {}
    for metric in metrics:
        if metric.endswith('r2') or metric.endswith('r2_mean'):
            best_model = summary_df[metric].idxmax()
            best_value = summary_df[metric].max()
        else:
            best_model = summary_df[metric].idxmin()
            best_value = summary_df[metric].min()
        
        best_models[metric] = {'model': best_model, 'value': best_value}
        
    print("\nBest Models by Individual Metric:")
    for metric, info in best_models.items():
        metric_display = {
            'rmse': 'RMSE',
            'mae': 'MAE',
            'mape': 'MAPE',
            'r2': 'R² Score',
            'cv_rmse_mean': 'CV RMSE',
            'cv_mae_mean': 'CV MAE',
            'cv_r2_mean': 'CV R² Score'
        }
        print(f"Best model for {metric_display.get(metric, metric)}: {info['model']} with value {info['value']:.4f}")
    
    return df

def load_models_and_evaluate(X_test, y_test, X_train=None, y_train=None, models_dir='./backend/models/saved_models/', save_path='./backend/models/visuals/', cv=5):
    """
    Args:
        X_test (pandas.DataFrame): Test feature set
        y_test (pandas.Series): Test target values
        X_train (pandas.DataFrame, optional): Training feature set for cross-validation
        y_train (pandas.Series, optional): Training target values for cross-validation
        models_dir (str): Directory containing the trained models
        save_path (str): Directory to save evaluation results and plots
        cv (int): Number of cross-validation folds
        
    Returns:
        list: List of evaluation result dictionaries for each model
    """
    if save_path:
        os.makedirs(save_path, exist_ok=True)
    
    model_files = [f for f in os.listdir(models_dir) if f.startswith('lhp_') and f.endswith('.pkl') 
                   and not f.endswith('_features.pkl')]
    
    if not model_files:
        print("No models found in the specified directory.")
        return []
    
    evaluation_results = []
    
    for model_file in model_files:
        model_name = model_file.replace('lhp_', '').replace('.pkl', '')
        print(f"\nEvaluating {model_name} model...")
        
        model_path = os.path.join(models_dir, model_file)
        model = joblib.load(model_path)
        
        # Evaluate model (with cross-validation if training data is provided)
        results = evaluate_model(
            model, 
            X_test, 
            y_test, 
            X_train=X_train, 
            y_train=y_train, 
            model_name=model_name.capitalize(),
            cv=cv,
            models_dir=models_dir
        )
        evaluation_results.append(results)
        
        # Plot predictions and residuals
        plot_predictions(y_test, results['predictions'], model_name=model_name.capitalize(), save_path=save_path)
        
        # Plot feature importance if applicable
        if hasattr(model, 'feature_importances_'):
            plot_feature_importance(model, X_test.columns, model_name=model_name.capitalize(), save_path=save_path)
    
    # Compare all models
    compare_models(evaluation_results, save_path=save_path, metrics=['rmse', 'mae', 'mape', 'r2'])
    
    if X_train is not None and y_train is not None:
        cv_metrics = ['cv_rmse_mean', 'cv_mae_mean', 'cv_r2_mean']
        if all(metric in evaluation_results[0] for metric in cv_metrics):
            print("\nComparing cross-validation results:")
            compare_models(evaluation_results, save_path=save_path, 
                          metrics=cv_metrics)
    
    return evaluation_results

def display_all_visualizations(visuals_path='./backend/models/visuals/'):
    """
    Args:
        visuals_path (str): Directory containing saved visualizations
    
    Returns:
        None: Displays all visualization images found in the specified directory
    """
    plt.switch_backend('TkAgg') 
    
    try:
        image_files = [f for f in os.listdir(visuals_path) if f.endswith('.png')]
        
        if not image_files:
            print("No visualization files found in the specified directory.")
            return
        
        print(f"\nDisplaying {len(image_files)} visualizations...")
        
        image_files.sort()
        
        for image_file in image_files:
            # Create a nice title from filename
            title = image_file.replace('_', ' ').replace('.png', '').title()
            
            # Display image with proper title in window
            img = plt.imread(os.path.join(visuals_path, image_file))
            plt.figure(figsize=(12, 8), num=title)
            plt.imshow(img)
            plt.axis('off')
            plt.tight_layout()
            plt.show()
            
    except Exception as e:
        print(f"Error displaying visualizations: {e}")

def main():
    """
    Args:
        None
    
    Returns:
        list: List of evaluation result dictionaries for each model
    """
    
    
    os.makedirs('./backend/models/saved_models', exist_ok=True)
    os.makedirs('./backend/models/visuals', exist_ok=True)
    
    df = load_processed_data('./backend/data/processed/lisbon_houses_processed.csv')
    if df is None:
        return
    
    model_df = prepare_data_for_modeling(df)
    X_train, X_test, y_train, y_test = split_data(model_df)
    
    models_dir = './backend/models/saved_models/'
    results_dir = './backend/models/visuals/'
    
    # Number of cross-validation folds
    cv_folds = 5
    
    # Evaluate all models with cross-validation
    evaluation_results = load_models_and_evaluate(
        X_test, 
        y_test, 
        X_train=X_train, 
        y_train=y_train,
        models_dir=models_dir, 
        save_path=results_dir,
        cv=cv_folds
    )
    
    print("\nModel evaluation with cross-validation completed successfully!")
    
    # Displays all visualizations after generation
    # display_all_visualizations(results_dir)
    
    return evaluation_results

if __name__ == "__main__":
    main()