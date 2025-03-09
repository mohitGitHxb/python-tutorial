import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

def plot_model_performance(df, metrics, stocks):
    """
    Generate grouped bar charts to compare the performance of different models across stocks for specified metrics.

    Parameters:
    - df (pd.DataFrame): DataFrame with columns 'Model', 'Stock', and the metrics (e.g., 'ROI', 'CAGR').
    - metrics (list): List of metric column names to plot (e.g., ['ROI', 'CAGR']).
    - stocks (list): List of stock names to include in the plots (e.g., ['AAPL', 'NVDA', 'TSLA']).
    """
    # Set Seaborn style for better visuals
    sns.set_style("whitegrid")

    for metric in metrics:
        # Filter data: exclude 'Actual Market' model for 'Accuracy' since it doesn't apply
        if metric == 'Accuracy':
            plot_df = df[df['Model'] != 'Actual Market']
        else:
            plot_df = df.copy()

        # Create a new figure for each metric
        plt.figure(figsize=(12, 6))
        ax = sns.barplot(x='Model', y=metric, hue='Stock', data=plot_df[plot_df['Stock'].isin(stocks)], palette="muted")
        
        # Set a clear title and labels
        plt.title(f'Comparison of {metric} Across Models and Stocks', fontsize=14, pad=10)
        plt.xlabel('Model', fontsize=12)
        plt.ylabel(metric, fontsize=12)
        plt.legend(title='Stock', bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # Format the y-axis based on the metric
        if metric in ['ROI', 'CAGR', 'Accuracy']:
            ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y*100:.2f}%'))
        elif metric == 'Number_of_Trades':
            ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.0f}'))
        elif metric == 'Final_Capital':
            ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:,.2f}'))
        
        # Add value labels on top of each bar, skipping NaN or zero values
        for p in ax.patches:
            height = p.get_height()
            if pd.notna(height) and height != 0:  # Skip NaN and zero values
                if metric in ['ROI', 'CAGR', 'Accuracy']:
                    label = f'{height*100:.2f}%'
                elif metric == 'Number_of_Trades':
                    label = f'{height:.0f}'
                elif metric == 'Final_Capital':
                    label = f'{height:,.2f}'
                ax.annotate(label, 
                            (p.get_x() + p.get_width() / 2., height),
                            ha='center', va='center', 
                            xytext=(0, 5), textcoords='offset points', 
                            fontsize=8)

        # Adjust layout to prevent overlap
        plt.tight_layout()
        plt.show()

# Example usage with real data from the CSV
if __name__ == "__main__":
    # Define the stocks from the CSV
    stocks = ['Yuanta', 'TATAMOTORS', 'SHREECEMENT', 'RIL', 'HDFCBANK', 'AAPL']
    
    # Define the models based on the CSV columns
    models = ['Actual Market', 'Attention_CNN_BiLSTM_STFT', 'MFA_STFT', 'Attention_CNN_BiLSTM_Multi_Indicator', 'MFA_Multi_indicator']
    
    # Sample data: nested dictionary for easier manual input
    # - Outer key: Model name
    # - Inner key: Stock ticker
    # - Values: Dictionary of metrics (ROI, CAGR, Number_of_Trades, Final_Capital, Accuracy)
    data = {
        'Actual Market': {
            'Yuanta': {'ROI': 0.6383, 'CAGR': 0.2799, 'Number_of_Trades': 0, 'Final_Capital': 163830, 'Accuracy': None},
            'TATAMOTORS': {'ROI': 1.0854, 'CAGR': 0.4441, 'Number_of_Trades': 0, 'Final_Capital': 208540, 'Accuracy': None},
            'SHREECEMENT': {'ROI': 0.2374, 'CAGR': 0.1124, 'Number_of_Trades': 0, 'Final_Capital': 123740, 'Accuracy': None},
            'RIL': {'ROI': 0.2558, 'CAGR': 0.1206, 'Number_of_Trades': 0, 'Final_Capital': 125580, 'Accuracy': None},
            'HDFCBANK': {'ROI': 0.2469, 'CAGR': 0.1167, 'Number_of_Trades': 0, 'Final_Capital': 124690, 'Accuracy': None},
            'AAPL': {'ROI': 0.4219, 'CAGR': 0.1924, 'Number_of_Trades': 0, 'Final_Capital': 142190, 'Accuracy': None}
        },
        'Attention_CNN_BiLSTM_STFT': {
            'Yuanta': {'ROI': 0.2518, 'CAGR': 0.1188, 'Number_of_Trades': 29, 'Final_Capital': 125178.45, 'Accuracy': 0.545},
            'TATAMOTORS': {'ROI': 0.7845, 'CAGR': 0.3359, 'Number_of_Trades': 35, 'Final_Capital': 178452.56, 'Accuracy': 0.5797},
            'SHREECEMENT': {'ROI': 0.4528, 'CAGR': 0.2053, 'Number_of_Trades': 36, 'Final_Capital': 145275.98, 'Accuracy': 0.5564},
            'RIL': {'ROI': 0.5562, 'CAGR': 0.2475, 'Number_of_Trades': 19, 'Final_Capital': 155620.97, 'Accuracy': 0.5836},
            'HDFCBANK': {'ROI': 0.7196, 'CAGR': 0.3114, 'Number_of_Trades': 20, 'Final_Capital': 171964.72, 'Accuracy': 0.5077},
            'AAPL': {'ROI': 0.5879, 'CAGR': 0.2601, 'Number_of_Trades': 35, 'Final_Capital': 158786.36, 'Accuracy': 0.5931}
        },
        'MFA_STFT': {
            'Yuanta': {'ROI': 0.2703, 'CAGR': 0.1271, 'Number_of_Trades': 27, 'Final_Capital': 127026.33, 'Accuracy': 0.545},
            'TATAMOTORS': {'ROI': 0.8088, 'CAGR': 0.3449, 'Number_of_Trades': 31, 'Final_Capital': 180884.95, 'Accuracy': 0.5608},
            'SHREECEMENT': {'ROI': 0.1558, 'CAGR': 0.0751, 'Number_of_Trades': 32, 'Final_Capital': 115578.00, 'Accuracy': 0.5719},
            'RIL': {'ROI': 0.5366, 'CAGR': 0.2396, 'Number_of_Trades': 19, 'Final_Capital': 153655.15, 'Accuracy': 0.57},
            'HDFCBANK': {'ROI': 0.7114, 'CAGR': 0.3082, 'Number_of_Trades': 23, 'Final_Capital': 171139.66, 'Accuracy': 0.5116},
            'AAPL': {'ROI': 0.5920, 'CAGR': 0.2618, 'Number_of_Trades': 28, 'Final_Capital': 159203.51, 'Accuracy': 0.6387}
        },
        'Attention_CNN_BiLSTM_Multi_Indicator': {
            'Yuanta': {'ROI': 0.5756, 'CAGR': 0.2552, 'Number_of_Trades': 5, 'Final_Capital': 157560.00, 'Accuracy': 0.86},
            'TATAMOTORS': {'ROI': 1.5667, 'CAGR': 0.6021, 'Number_of_Trades': 2, 'Final_Capital': 256665.00, 'Accuracy': 0.8307},
            'SHREECEMENT': {'ROI': 0.5555, 'CAGR': 0.2472, 'Number_of_Trades': 5, 'Final_Capital': 155545.00, 'Accuracy': 0.8657},
            'RIL': {'ROI': 0.7803, 'CAGR': 0.3343, 'Number_of_Trades': 3, 'Final_Capital': 178034.00, 'Accuracy': 0.8504},
            'HDFCBANK': {'ROI': 0.4022, 'CAGR': 0.1841, 'Number_of_Trades': 5, 'Final_Capital': 140218.00, 'Accuracy': 0.8774},
            'AAPL': {'ROI': 0.1760, 'CAGR': 0.0844, 'Number_of_Trades': 4, 'Final_Capital': 117600.00, 'Accuracy': 0.59}
        },
        'MFA_Multi_indicator': {
            'Yuanta': {'ROI': 1.0546, 'CAGR': 0.4334, 'Number_of_Trades': 4, 'Final_Capital': 205458.46, 'Accuracy': 0.7568},
            'TATAMOTORS': {'ROI': 1.2669, 'CAGR': 0.5056, 'Number_of_Trades': 2, 'Final_Capital': 226687.01, 'Accuracy': 0.7334},
            'SHREECEMENT': {'ROI': 0.6435, 'CAGR': 0.2820, 'Number_of_Trades': 7, 'Final_Capital': 164345.00, 'Accuracy': 0.5428},
            'RIL': {'ROI': 0.7496, 'CAGR': 0.3227, 'Number_of_Trades': 4, 'Final_Capital': 174960.00, 'Accuracy': 0.7217},
            'HDFCBANK': {'ROI': 0.1688, 'CAGR': 0.0811, 'Number_of_Trades': 3, 'Final_Capital': 116883.00, 'Accuracy': 0.8346},
            'AAPL': {'ROI': 0.7723, 'CAGR': 0.3313, 'Number_of_Trades': 6, 'Final_Capital': 177230.00, 'Accuracy': 0.5741}
        }
    }
    
    # Convert the data dictionary to a DataFrame
    df = pd.DataFrame([
        {'Model': model, 'Stock': stock, **metrics}
        for model, stock_data in data.items()
        for stock, metrics in stock_data.items()
    ])
    
    # Define metrics to plot
    metrics = ['ROI', 'CAGR', 'Number_of_Trades', 'Final_Capital', 'Accuracy']
    
    # Generate the plots
    plot_model_performance(df, metrics, stocks)