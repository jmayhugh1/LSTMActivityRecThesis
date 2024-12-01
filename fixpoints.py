import pandas as pd

# Load the original CSV
df = pd.read_csv('points.csv')

# Combine points into a single list for each row
df['Points'] = df[['Point 1', 'Point 2', 'Point 3', 'Point 4', 'Point 5', 'Point 6']].values.tolist()

# Remove NaN values and convert points to a clean list format
df['Points'] = df['Points'].apply(lambda points: [point for point in points if pd.notna(point)])

# Create a new DataFrame with 'Video Name' and combined 'Points' column
transformed_df = df[['Video Name', 'Points']]

# Save the transformed data to a new CSV
transformed_df.to_csv('combined_points.csv', index=False)

print("Points have been combined into a single list and saved to 'combined_points.csv'.")
