import matplotlib.pyplot as plt
import seaborn as sns
import os
import uuid

def visualize_data(df):
    chart_id = str(uuid.uuid4())
    chart_path = f"static/{chart_id}.png"

    # Create static folder if it doesn't exist
    os.makedirs("static", exist_ok=True)

    # Basic logic to choose chart type
    if "sales" in df.columns and "region" in df.columns:
        sns.barplot(data=df, x="region", y="sales")
    elif "sales" in df.columns and "date" in df.columns:
        sns.lineplot(data=df, x="date", y="sales")
    else:
        df.plot()

    plt.title("Auto-Generated Visualization")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return chart_path
