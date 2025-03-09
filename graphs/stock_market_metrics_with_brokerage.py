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
        # Create a new figure for each metric
        plt.figure(figsize=(12, 6))
        ax = sns.barplot(
            x="Model",
            y=metric,
            hue="Stock",
            data=df[df["Stock"].isin(stocks)],
            palette="muted",
        )

        # Set a clear title and labels
        plt.title(
            f"Comparison of {metric} Across Models and Stocks With Transactional Cost Of 0.3% Per Trade",
            fontsize=14,
            pad=10,
        )
        plt.xlabel("Models", fontsize=12)
        plt.ylabel(metric, fontsize=12)
        plt.legend(title="Stock", bbox_to_anchor=(1.05, 1), loc="upper left")

        # Format the y-axis based on the metric
        if metric in ["ROI", "CAGR", "Accuracy"]:
            ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y * 100:.2f}%"))
        elif metric == "Final_Capital":
            ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:,.2f}"))

        # Add value labels on top of each bar, skipping NaN or zero values
        for p in ax.patches:
            height = p.get_height()
            if pd.notna(height) and height != 0:  # Skip NaN and zero values
                if metric in ["ROI", "CAGR", "Accuracy"]:
                    label = f"{height * 100:.2f}%"
                elif metric == "Final_Capital":
                    label = f"{height:,.2f}"
                ax.annotate(
                    label,
                    (p.get_x() + p.get_width() / 2.0, height),
                    ha="center",
                    va="center",
                    xytext=(0, 5),
                    textcoords="offset points",
                    fontsize=8,
                )

        # Adjust layout to prevent overlap
        plt.tight_layout()
        plt.show()


# Example usage with real data from the CSV
if __name__ == "__main__":
    # Define the stocks from the CSV
    stocks = ["Yuanta", "TATAMOTORS", "SHREECEMENT", "RIL", "HDFCBANK", "AAPL"]

    # Define the models based on the CSV columns
    models = [
        "Attention_CNN_BiLSTM_STFT",
        "MFA_STFT",
        "Attention_CNN_BiLSTM_Multi_Indicator",
        "MFA_Multi_indicator",
    ]

    # Sample data: nested dictionary for easier manual input
    # - Outer key: Model name
    # - Inner key: Stock ticker
    # - Values: Dictionary of metrics (ROI, CAGR, Final_Capital)
    data = {
        "Attention_CNN_BiLSTM_STFT": {
            "Yuanta": {"ROI": 0.1429, "CAGR": 0.0691, "Final_Capital": 114287.92},
            "TATAMOTORS": {"ROI": 0.5972, "CAGR": 0.2638, "Final_Capital": 159715.05},
            "SHREECEMENT": {"ROI": 0.2959, "CAGR": 0.1384, "Final_Capital": 129586.17},
            "RIL": {"ROI": 0.4675, "CAGR": 0.2114, "Final_Capital": 146750.58},
            "HDFCBANK": {"ROI": 0.6165, "CAGR": 0.2714, "Final_Capital": 161646.83},
            "AAPL": {"ROI": 0.4211, "CAGR": 0.1921, "Final_Capital": 142113.79},
        },
        "MFA_STFT": {
            "Yuanta": {"ROI": 0.1674, "CAGR": 0.0804, "Final_Capital": 116737.20},
            "TATAMOTORS": {"ROI": 0.6406, "CAGR": 0.2809, "Final_Capital": 164062.65},
            "SHREECEMENT": {"ROI": 0.0448, "CAGR": 0.0222, "Final_Capital": 104482.51},
            "RIL": {"ROI": 0.4490, "CAGR": 0.2037, "Final_Capital": 144896.81},
            "HDFCBANK": {"ROI": 0.5933, "CAGR": 0.2623, "Final_Capital": 159331.02},
            "AAPL": {"ROI": 0.4583, "CAGR": 0.2076, "Final_Capital": 145830.41},
        },
        "Attention_CNN_BiLSTM_Multi_Indicator": {
            "Yuanta": {"ROI": 0.5520, "CAGR": 0.2458, "Final_Capital": 155196.60},
            "TATAMOTORS": {"ROI": 1.2533, "CAGR": 0.5011, "Final_Capital": 225326.89},
            "SHREECEMENT": {"ROI": 0.5321, "CAGR": 0.2378, "Final_Capital": 153211.83},
            "RIL": {"ROI": 0.7643, "CAGR": 0.3283, "Final_Capital": 176431.69},
            "HDFCBANK": {"ROI": 0.3811, "CAGR": 0.1752, "Final_Capital": 138114.73},
            "AAPL": {"ROI": 0.1619, "CAGR": 0.0779, "Final_Capital": 116188.80},
        },
        "MFA_Multi_indicator": {
            "Yuanta": {"ROI": 1.0299, "CAGR": 0.4248, "Final_Capital": 202992.96},
            "TATAMOTORS": {"ROI": 1.5513, "CAGR": 0.5973, "Final_Capital": 255125.01},
            "SHREECEMENT": {"ROI": 0.6089, "CAGR": 0.2684, "Final_Capital": 160893.76},
            "RIL": {"ROI": 0.7286, "CAGR": 0.3148, "Final_Capital": 172860.48},
            "HDFCBANK": {"ROI": 0.1583, "CAGR": 0.0762, "Final_Capital": 115831.05},
            "AAPL": {"ROI": 0.7404, "CAGR": 0.3192, "Final_Capital": 174039.86},
        },
    }

    # Convert the data dictionary to a DataFrame
    df = pd.DataFrame(
        [
            {"Model": model, "Stock": stock, **metrics}
            for model, stock_data in data.items()
            for stock, metrics in stock_data.items()
        ]
    )

    # Define metrics to plot (removed Number_of_Trades and Accuracy as requested)
    metrics = ["ROI", "CAGR", "Final_Capital"]

    # Generate the plots
    plot_model_performance(df, metrics, stocks)
