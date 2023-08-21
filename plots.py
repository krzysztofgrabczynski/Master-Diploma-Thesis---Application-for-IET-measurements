from numpy.fft import fft, fftfreq
from numpy import abs as np_abs
from numpy import argmax, arange, ndarray, float64, bool_
from scipy.signal import stft
import matplotlib.pyplot as plot

from dataclasses import dataclass
from types import ModuleType
from tkinter import StringVar
from typing import Tuple, Union

from excel_service import create_excel_file


@dataclass
class PlotRange:
    """
    Class representing x-axis range and y-axis range
    """

    x: Union[None, Tuple[float, float]]
    y: Union[None, Tuple[float, float]]


def plot_time(signal: ndarray, FS: int) -> ModuleType:
    """
    Function that returns the plot of time vs sound pressure.
    """

    T = 1.0 / FS  # sampling period
    time = arange(0, len(signal) / FS, T)  # Time axis

    plot.figure(figsize=(6, 4))
    plot.plot(time, signal, color="red")
    plot.xlabel("Time [s]")
    plot.ylabel("Sound pressure")
    plot.title("Sound pressure")
    plot.grid(True)

    return plot


def _computing_signal_fft(
    signal: ndarray, T: float
) -> Tuple[ndarray[float], ndarray[float], ndarray[bool_]]:
    """
    Function to return FFT magnitude, frequencies and mask after fft.
    """

    frequencies = fftfreq(len(signal), T)  # Array of frequencies for FFT
    mask = frequencies > 0  # Exclude negative frequencies
    fft_values = fft(
        signal
    )  # FFT operation on the sound pressure from the microphone
    fft_abs = np_abs(fft_values)

    return fft_abs, frequencies, mask


def plot_frequency(
    signal: ndarray,
    FS: int,
    is_log_scale: bool,
    plot_range: PlotRange,
    window_functions: dict,
    window_choice: StringVar,
) -> Tuple[ModuleType, float64]:
    """
    Function to return plot of the FFT magnitude 2D, maximum frequency and initialization other function to create .xslx file and save the data.
    """

    T = 1.0 / FS  # sampling period

    # Window function choice
    selected_window = window_functions[window_choice.get()]
    if selected_window is not None:
        window = selected_window(len(signal))
        signal = signal * window

    fft_abs, frequencies, mask = _computing_signal_fft(signal, T)

    plot.figure(figsize=(10, 6))
    plot.plot(frequencies[mask], fft_abs[mask], color="blue")
    plot.xlabel("Frequency [Hz]")
    plot.ylabel("Amplitude [db]")
    plot.title("FFT Magnitude 2D")
    # Setting logarithmic scale if selected by user
    if is_log_scale:
        plot.xscale("log")
        plot.yscale("log")
    plot.grid(True)
    # Setting x-axis and y-axis range if specified by user
    if plot_range.x is not None:
        plot.xlim(plot_range.x[0], plot_range.x[1])
    if plot_range.y is not None:
        plot.ylim(plot_range.y[0], plot_range.y[1])

    # Determining the maximum frequency value
    max_frequency = frequencies[mask][argmax(fft_abs[mask])] / 1000

    create_excel_file(frequencies, fft_abs, mask)

    return plot, max_frequency


def plot_waterfall(
    signal: ndarray, FS: int, window_functions: dict, window_choice: StringVar
) -> ModuleType:
    """
    Function to plot waterfall chart for FFT Magnitude 3D
    """

    # Window function choice
    selected_window = window_functions[window_choice.get()]
    if selected_window is not None:
        window = selected_window(len(signal))
        signal = signal * window

    frequencies, times, stft_result = stft(signal, FS)
    stft_result_abs = np_abs(stft_result)

    # creates a waterfall plot
    fig, ax = plot.subplots(figsize=(10, 6))
    cax = ax.pcolormesh(times, frequencies, stft_result_abs, shading="auto")

    ax.set_xlabel("Time [s]")
    ax.set_ylabel("FFT Magnitude")
    ax.set_title("FFT Magnitude 3D")

    fig.colorbar(cax)  # add colorbar

    return plot
