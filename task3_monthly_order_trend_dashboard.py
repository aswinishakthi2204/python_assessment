import numpy as np
import matplotlib.pyplot as plt

# Reproducible synthetic data
np.random.seed(42)

months = np.arange(1, 13)
month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Generate 12 months of total orders
orders = np.random.randint(1000, 5001, 12)

# Generate average order value and monthly revenue
avg_order_value = np.random.uniform(200, 400, 12)
revenue = orders * avg_order_value

# Generate 500 delivery times using mean=28 and std=4
delivery_times = np.random.normal(28, 4, 500)

# Create dashboard with three subplots
fig, axes = plt.subplots(3, 1, figsize=(12, 15))
fig.suptitle("Food Delivery Platform - Monthly Performance Dashboard",
             fontsize=16, fontweight="bold")

# Subplot 1: Line chart with annotations
axes[0].plot(month_labels, orders, marker="o")
axes[0].set_title("Monthly Total Orders")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Total Orders")

for i, value in enumerate(orders):
    axes[0].annotate(str(value),
                     (i, value),
                     textcoords="offset points",
                     xytext=(0, 7),
                     ha="center")

# Subplot 2: Revenue bar chart
bar_colors = ["green" if value > 800000 else "red" for value in revenue]
axes[1].bar(month_labels, revenue, color=bar_colors)
axes[1].axhline(800000, linestyle="--", linewidth=1.5,
                label="Rs 8,00,000 Threshold")
axes[1].set_title("Monthly Revenue")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Revenue (Rs)")
axes[1].legend()

# Subplot 3: Delivery-time histogram
axes[2].hist(delivery_times, bins=15)
sample_mean = np.mean(delivery_times)
axes[2].axvline(sample_mean, linestyle="--", linewidth=1.5,
                label="Mean")
axes[2].set_title("Delivery Time Distribution")
axes[2].set_xlabel("Delivery Time (minutes)")
axes[2].set_ylabel("Frequency")
axes[2].legend()

plt.tight_layout()
plt.savefig("food_delivery_dashboard.png", dpi=150)
plt.show()
