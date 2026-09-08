import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Generate synthetic dataset using NumPy (seed=7)
np.random.seed(7)
n = 200

df = pd.DataFrame({
    "order_value": np.random.uniform(100, 800, n),
    "distance_km": np.random.uniform(1, 20, n),
    "delivery_time_mins": np.random.normal(30, 8, n),
    "rating": np.random.uniform(1.0, 5.0, n),
    "discount_pct": np.random.uniform(0, 30, n)
})

# 2. Artificially introduce 5% null values using np.random.choice()
for column in ["delivery_time_mins", "rating"]:
    null_indices = np.random.choice(df.index, size=int(0.05 * n), replace=False)
    df.loc[null_indices, column] = np.nan

# 3. Fill nulls with the respective column medians
df["delivery_time_mins"] = df["delivery_time_mins"].fillna(
    df["delivery_time_mins"].median()
)
df["rating"] = df["rating"].fillna(df["rating"].median())

# 4. Add derived delivery speed column
df["delivery_speed_kmph"] = (
    df["distance_km"] / (df["delivery_time_mins"] / 60)
)

# 5. Classify rows into 3 equal-frequency speed bands using pd.qcut()
df["speed_band"] = pd.qcut(
    df["delivery_speed_kmph"],
    q=3,
    labels=["Slow", "Normal", "Fast"]
)

# 6. Pearson correlation heatmap for all numeric columns
numeric_df = df.select_dtypes(include=np.number)
correlation_matrix = numeric_df.corr(method="pearson")

plt.figure(figsize=(10, 8))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    center=0
)
plt.title("Pearson Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=150)
plt.close()

# 7. Seaborn pairplot coloured by speed_band
pairplot = sns.pairplot(
    df,
    vars=["order_value", "distance_km", "delivery_time_mins", "rating"],
    hue="speed_band"
)
pairplot.fig.suptitle(
    "Food Delivery Pairplot by Speed Band",
    y=1.02
)
pairplot.fig.tight_layout()
pairplot.fig.savefig("pairplot.png", dpi=150, bbox_inches="tight")
plt.close(pairplot.fig)

print("Task 4 completed successfully.")
print(f"Dataset shape: {df.shape}")
print("Null values after median filling:")
print(df[["delivery_time_mins", "rating"]].isnull().sum())
print("\\nSpeed band counts:")
print(df["speed_band"].value_counts().sort_index())
print("\\nCharts saved:")
print("correlation_heatmap.png")
print("pairplot.png")
