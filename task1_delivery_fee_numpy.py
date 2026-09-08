import numpy as np

# Fixed seed for reproducible random distances
np.random.seed(42)

# Generate 25 random delivery distances between 1.0 km and 15.0 km
distances = np.random.uniform(1.0, 15.0, 25)

# Vectorised delivery fee calculation
fees = 20 + (5 * distances)

# Boolean indexing: select orders where fee exceeds Rs 60
qualifying_distances = distances[fees > 60]
qualifying_fees = fees[fees > 60]

print("Orders where delivery fee exceeds Rs 60:")
print("Distance (km)    Fee (Rs)")
print(np.column_stack((qualifying_distances, qualifying_fees)))

# NumPy statistical functions on the complete fee array
print("\nFee statistics for all 25 orders:")
print(f"Minimum fee       : Rs {np.min(fees):.2f}")
print(f"Maximum fee       : Rs {np.max(fees):.2f}")
print(f"Mean fee          : Rs {np.mean(fees):.2f}")
print(f"Standard deviation: Rs {np.std(fees):.2f}")
