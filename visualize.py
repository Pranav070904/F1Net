import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# Load data
data = pd.read_csv("data/combined_driver_data.csv")

# Features to plot
features = ['AvgFPTime', 'QualyTime', 'QualTimeDelta', 'GridPos']
target = 'FinishPos'

# Create subplots: 2 rows, 2 columns for scatter, 1 full-width bar plot
fig = plt.figure(figsize=(14, 12))
gs = fig.add_gridspec(3, 2, height_ratios=[1, 1, 0.8])
axes = [fig.add_subplot(gs[i // 2, i % 2]) for i in range(4)]
bar_ax = fig.add_subplot(gs[2, :])

# Scatter plots
for i, feature in enumerate(features):
    ax = axes[i]
    ax.scatter(data[feature], data[target], alpha=0.5, s=20)
    ax.set_xlabel(feature)
    ax.set_ylabel(target)
    ax.set_ylim([0.5, 20.5])
    ax.invert_yaxis()
    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    cor = np.corrcoef(data[feature], data[target])[0, 1]
    ax.set_title(f'{feature} vs {target} (Corr: {cor:.2f})')

# Bar plot for label distribution
class_counts = data[target].value_counts().sort_index()
bar_ax.bar(class_counts.index.astype(str), class_counts.values, color='skyblue')
bar_ax.set_xlabel("Finishing Position")
bar_ax.set_ylabel("Count")
bar_ax.set_title("Finish Position Distribution")
bar_ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))

plt.tight_layout()
plt.savefig("visualizations/Clean_Data_Visualizations.png")
plt.show()
