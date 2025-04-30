import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("temperatures.csv")

# Drop rows with missing ANNUAL values (if any)
df = df.dropna(subset=['ANNUAL'])

# Fastest Warming Months 
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
          'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

slopes = {}
for month in months:
    z = np.polyfit(df['YEAR'], df[month], 1)
    slopes[month] = z[0]  # Slope of the line

# Sort and display top 3 warming months
sorted_slopes = sorted(slopes.items(), key=lambda x: x[1], reverse=True)
top_3 = sorted_slopes[:3]

print(" Fastest Warming Months:")
for month, slope in top_3:
    print(f"  - {month}: {slope:.4f} °C/YEAR")

#  Hottest & Coldest YEARs
hottest = df.loc[df['ANNUAL'].idxmax()]
coldest = df.loc[df['ANNUAL'].idxmin()]

print(f"\n Hottest YEAR: {int(hottest['YEAR'])} — {hottest['ANNUAL']}°C")
print(f" Coldest YEAR: {int(coldest['YEAR'])} — {coldest['ANNUAL']}°C")

# Seasonal Shift 
df['Winter_Avg'] = df[['JAN', 'FEB']].mean(axis=1)
df['Summer_Avg'] = df[['APR', 'MAY', 'JUN']].mean(axis=1)

# Calculate slope for both
winter_slope = np.polyfit(df['YEAR'], df['Winter_Avg'], 1)[0]
summer_slope = np.polyfit(df['YEAR'], df['Summer_Avg'], 1)[0]

print("\n Seasonal Shift:")
print(f"  - Winter warming rate: {winter_slope:.4f} °C/YEAR")
print(f"  - Summer warming rate: {summer_slope:.4f} °C/YEAR")

if winter_slope > summer_slope:
    print("  → Winters are warming faster than summers.")
elif summer_slope > winter_slope:
    print("  → Summers are intensifying more than winters.")
else:
    print("  → Both seasons are warming at similar rates.")
