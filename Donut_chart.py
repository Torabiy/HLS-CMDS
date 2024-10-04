"""
Sound Types Donut Chart Visualization

This Python script generates a multi-layered donut chart to visualize the number of different heart, lung, and mixed sounds in a dataset. It uses the `matplotlib` library to create concentric donut layers representing heart sounds, lung sounds, and mixed sounds. The chart includes a legend showing the total counts for each sound type.

## Features:
- Three concentric donut charts: inner (lung sounds), middle (heart sounds), outer (mixed sounds).
- Consistent color mapping across all layers for each sound type.
- Displays the count for each sound type within the chart.

## Citation:
If you use this code or the associated dataset in your research, please cite the following:
- Mendeley Data DOI: [Insert DOI Here]
- Related Article DOI: [Insert Related Article DOI Here]

## Copyright:
© 2024 by Yasaman Torabi. All rights reserved.
"""

import matplotlib.pyplot as plt
import numpy as np

# Define the corrected values for each layer: heart, lung, and mixed sounds
heart_values_updated = [9, 6, 7, 5, 4, 2, 6, 5, 3, 3]  # Heart sounds
lung_values_updated = [12, 7, 5, 8, 9, 9]  # Lung sounds
mix_values_updated = [9, 10, 10, 16, 13, 12, 8, 11, 12, 9, 18, 16, 13, 21, 24, 18]  # Mixed sounds

# Define the sound types for each layer
heart_labels_updated = ['Normal Heart', 'Late Diastolic Murmur', 'Mid Systolic Murmur', 
                        'Late Systolic Murmur', 'Atrial Fibrillation', 'Fourth Heart Sound', 
                        'Early Systolic Murmur', 'Third Heart Sound', 'Tachycardia', 
                        'Atrioventricular Block']
lung_labels_updated = ['Normal Lung', 'Wheezing', 'Crackles', 'Rhonchi', 
                       'Pleural Rub', 'Gurgling']
mix_labels_updated = heart_labels_updated + lung_labels_updated

# Define a consistent color palette for all sound types across the three layers
color_mapping = {
    'Normal Heart': '#1f77b4', 'Late Diastolic Murmur': '#ff7f0e', 'Mid Systolic Murmur': '#2ca02c', 
    'Late Systolic Murmur': '#d62728', 'Atrial Fibrillation': '#9467bd', 'Fourth Heart Sound': '#8c564b', 
    'Early Systolic Murmur': '#e377c2', 'Third Heart Sound': '#7f7f7f', 'Tachycardia': '#bcbd22', 
    'Atrioventricular Block': '#17becf', 'Normal Lung': '#9edae5', 'Wheezing': '#ff9896', 
    'Crackles': '#98df8a', 'Rhonchi': '#c5b0d5', 'Pleural Rub': '#ffbb78', 'Gurgling': '#c49c94'
}

# Map the colors for each layer using the same color for the same sound type
heart_colors = [color_mapping[label] for label in heart_labels_updated]
lung_colors = [color_mapping[label] for label in lung_labels_updated]
mix_colors = [color_mapping[label] for label in mix_labels_updated]

# Define new legend labels with total counts for each sound type
legend_labels_with_counts = [
    f'Normal Heart (18)', f'Late Diastolic Murmur (16)', f'Mid Systolic Murmur (17)', 
    f'Late Systolic Murmur (21)', f'Atrial Fibrillation (17)', f'Fourth Heart Sound (14)', 
    f'Early Systolic Murmur (14)', f'Third Heart Sound (16)', f'Tachycardia (15)', 
    f'Atrioventricular Block (12)', f'Normal Lung (30)', f'Wheezing (23)', 
    f'Crackles (18)', f'Rhonchi (29)', f'Pleural Rub (33)', f'Gurgling (27)'
]

# Create the donut plot with the updated legend including total counts
fig, ax = plt.subplots(figsize=(10, 10))

# Outer layer (Mixed Sounds) - Add count numbers in the middle of each section
wedges, texts = ax.pie(mix_values_updated, radius=1, colors=mix_colors, startangle=90, pctdistance=0.85)
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = np.cos(np.deg2rad(angle)) * 0.85
    y = np.sin(np.deg2rad(angle)) * 0.85
    ax.text(x, y, str(mix_values_updated[i]), ha='center', va='center', fontsize=10)

# Middle layer (Heart Sounds) - Add count numbers in the middle of each section
wedges, texts = ax.pie(heart_values_updated, radius=0.75, colors=heart_colors, startangle=90, pctdistance=0.75)
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = np.cos(np.deg2rad(angle)) * 0.6
    y = np.sin(np.deg2rad(angle)) * 0.6
    ax.text(x, y, str(heart_values_updated[i]), ha='center', va='center', fontsize=10)

# Inner layer (Lung Sounds) - Add count numbers in the middle of each section
wedges, texts = ax.pie(lung_values_updated, radius=0.5, colors=lung_colors, startangle=90, pctdistance=0.65)
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = np.cos(np.deg2rad(angle)) * 0.45
    y = np.sin(np.deg2rad(angle)) * 0.45
    ax.text(x, y, str(lung_values_updated[i]), ha='center', va='center', fontsize=10)

# Add a circle at the center to make it a true donut chart
centre_circle = plt.Circle((0, 0), 0.3, fc='white')
fig.gca().add_artist(centre_circle)

# Add a title
plt.title('Sound Types in the Dataset', fontsize=16, fontweight='bold', y=0.95)

# Add a legend outside the chart with total counts for each sound type
plt.legend(labels=legend_labels_with_counts, loc='center left', bbox_to_anchor=(1, 0.5), title="Sound Types")

# Display the chart with updated legend
plt.tight_layout()
plt.show()
