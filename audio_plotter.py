"""
Audio Waveform Plotter

This Python script allows you to visualize and plot time-domain waveforms of audio files and play them back using the IPython library. It is specifically designed to handle heart and lung sound data but can be applied to any audio file.

## Features:
- Plot multiple waveforms in one figure.
- Automatically adjust for the number of audio files.
- Save the figure as an image file.
- Play the audio file directly using IPython.

## Citation:
If you use this code or the associated dataset in your research, please cite the following:
- Mendeley Data DOI: [Insert DOI Here]
- Related Article DOI: [Insert Related Article DOI Here]

## Copyright:
© 2024 by Yasaman Torabi. All rights reserved.
"""

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os
import IPython.display as ipd

def plot_audio_waveform(audio_path, ax, title):
    """
    Plots the waveform of an audio file.

    Parameters:
    - audio_path: str, path to the audio file
    - ax: matplotlib axis, axis to plot on
    - title: str, title of the plot
    """
    if not os.path.exists(audio_path):
        print(f"Error: {audio_path} not found.")
        return

    # Load audio
    y, sr = librosa.load(audio_path)

    # Plot waveform
    librosa.display.waveshow(y, sr=sr, color='black', ax=ax)
    ax.set_title(title)
    ax.set_ylim([-0.05, 0.05])  # Standardize y-limits
    ax.set_xlim([0, len(y) / sr])  # Time in seconds
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')

def plot_combined_waveforms(audio_paths, titles, output_file='combined_plots.png'):
    """
    Plots waveforms for multiple audio files and saves the figure as an image.

    Parameters:
    - audio_paths: list of str, paths to the audio files
    - titles: list of str, titles for each plot
    - output_file: str, name of the output file for the figure
    """
    num_plots = len(audio_paths)
    
    # Create subplots
    fig, axs = plt.subplots(num_plots, 1, figsize=(12, 4 * num_plots))
    
    for i in range(num_plots):
        plot_audio_waveform(audio_paths[i], axs[i], titles[i])
    
    # Adjust layout and save figure
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()

def play_audio(audio_path):
    """
    Plays the audio using IPython's Audio player.

    Parameters:
    - audio_path: str, path to the audio file
    """
    if not os.path.exists(audio_path):
        print(f"Error: {audio_path} not found.")
        return

    # Load the audio
    y, sr = librosa.load(audio_path)
    
    # Play the audio
    return ipd.Audio(y, rate=sr)


# Example usage
audio_files = [
    '/content/M_AF_LC.wav',  # Update paths if necessary
    '/content/M_S3_C_RUSB.wav',
    '/content/M_W_RLA.wav'
]
titles = ['AF_LC', 'S3_C_RUSB', 'W_RLA']

# Plot and save combined waveforms
plot_combined_waveforms(audio_files, titles)

# Play one of the audio files
audio_to_play = '/content/M_W_RLA.wav'
play_audio(audio_to_play)
