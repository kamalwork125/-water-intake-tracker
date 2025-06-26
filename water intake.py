import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('water.csv')
df.columns = df.columns.str.strip

print("✅ Columns after cleaning:")
print(df.columns.tolist())  # Confirm they're clean

# Now safely plot
plt.plot(df['WaterIntake (ml)'], df['Recommended (ml)'], marker='o', color='red')
plt.title("Water Intake VS Recommended")
plt.xlabel("Water Intake (ml)")
plt.ylabel("Recommended (ml)")
plt.grid(True)
plt.show()

