import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

RF_CSV = os.path.join('results', 'rf_distances.csv')
FIG_DIR = os.path.join('results', 'figures')
os.makedirs(FIG_DIR, exist_ok=True)

df = pd.read_csv(RF_CSV)
rf_vals = df['rf_distance']
mean_rf = np.mean(rf_vals)
se_rf = np.std(rf_vals, ddof=1) / np.sqrt(len(rf_vals))
print(f"Mean RF distance: {mean_rf:.3f}")
print(f"Standard error: {se_rf:.3f}")

plt.figure(figsize=(8, 5))
sns.histplot(rf_vals, bins=10, kde=True)
plt.title('Distribution of Robinson-Foulds Distances')
plt.xlabel('RF Distance')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, 'rf_histogram.png'))
plt.close()

plt.figure(figsize=(6, 5))
sns.boxplot(y=rf_vals)
plt.title('Boxplot of Robinson-Foulds Distances')
plt.ylabel('RF Distance')
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, 'rf_boxplot.png'))
plt.close() 