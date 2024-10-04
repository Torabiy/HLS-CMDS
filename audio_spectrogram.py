"""
Mel-Spectrogram Plotter

This Python script plots the Mel-spectrograms of multiple audio files using `librosa` and `matplotlib`. It processes audio files, generates Mel-spectrograms, and displays them in a vertically oriented figure.

## Features:
- Generate and plot Mel-spectrograms for multiple audio files.
- Customize frequency range and Mel band limits.
- Include a color bar for better interpretation of dB scale values.

## Acknowledgment:
We would like to acknowledge the Mohawk Institute for Applied Health Sciences (IAHS) for their assistance in data collection using patient simulators.

## Citation:
If you use this code or the associated dataset in your research, please cite the following:
- Heart and Lung Sounds Dataset Recorded from a Clinical Manikin using Digital Stethoscope (HLS-CMDS), Yasaman Torabi, Shahram Shirani, James P. Reilly. McMaster University.
- Mendeley Data DOI: [Insert DOI Here]
- Related Article DOI: [Insert Related Article DOI Here]

## Copyright:
© 2024 by Yasaman Torabi, Shahram Shirani, and James P. Reilly. All rights reserved.
"""

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

# Set up the figure with 3 rows and 1 column using gridspec
fig = plt.figure(figsize=(8, 12))  # Adjust the figure size for vertical orientation
gs = gridspec.GridSpec(4, 1, height_ratios=[1, 1, 1, 0.05])  # Last row for the colorbar

# Define audio file paths and titles
audio_files = [
    ('/content/M_AF_LC.wav', 'M_AF_LC'),
    ('/content/M_S3_C_RUSB.wav', 'M_S3_C_RUSB'),
    ('/content/M_W_RLA.wav', 'M_W_RLA')
]

axs = [plt.subplot(gs[i]) for i in range(3)]  # Create 3 subplots for the spectrograms

# Plot spectrograms
for i, (audio_path, title) in enumerate(audio_files):
    # Load the audio file
    y, sr = librosa.load(audio_path)
    
    # Generate the mel spectrogram
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=2048)  # Limit frequency to 2048 Hz
    S_dB = librosa.power_to_db(S, ref=np.max)
    
    # Plot the spectrogram in the corresponding subplot
    img = librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel', fmax=2048, ax=axs[i])
    
    # Set the title and axis labels
    axs[i].set_title(title)
    axs[i].set_xlabel('Time (s)')
    axs[i].set_ylabel('Frequency (Hz)')

# Add a color bar to the bottom of the last subplot
cbar_ax = plt.subplot(gs[3])  # Create a new axis for the colorbar
fig.colorbar(img, cax=cbar_ax, format='%+2.0f dB', orientation='horizontal')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Leave space for the color bar on the bottom
plt.show()
