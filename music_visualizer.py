import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pydub import AudioSegment
from pydub.playback import play
import tkinter as tk
from tkinter import filedialog, messagebox
import threading

CHUNK = 1024 * 2
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100

class AudioVisualizer:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            output=False,
            frames_per_buffer=CHUNK
        )
        
        # Create the figure and plot
        self.fig, self.ax = plt.subplots()
        self.x = np.arange(0, CHUNK)
        self.line, = self.ax.plot(self.x, np.zeros(CHUNK))
        
        # Set up the plot
        self.ax.set_title('Real-Time Audio Waveform')
        self.ax.set_xlabel('Sample')
        self.ax.set_ylabel('Amplitude')
        self.ax.set_ylim(-1, 1)
        self.ax.set_xlim(0, CHUNK)
        
        self.mp3_data = None
        self.playing_mp3 = False
        
    def update_plot(self, frame):
        if self.playing_mp3 and self.mp3_data:
            audio_data = np.frombuffer(self.mp3_data.read(CHUNK), dtype=np.float32)
        else:
            data = self.stream.read(CHUNK, exception_on_overflow=False)
            audio_data = np.frombuffer(data, dtype=np.float32)
        self.line.set_ydata(audio_data)
        return self.line,
        
    def run(self):
        root = tk.Tk()
        root.withdraw()
        if messagebox.askyesno("Audio Source", "Do you want to play an MP3 file?"):
            self.select_mp3_file()
        ani = FuncAnimation(
            self.fig,
            self.update_plot,
            interval=30,
            blit=True
        )
        plt.show()
        
    def cleanup(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        
    def select_mp3_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            try:
                self.mp3_data = AudioSegment.from_file(file_path)
                self.playing_mp3 = True
                threading.Thread(target=play, args=(self.mp3_data,)).start()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load MP3 file: {e}")
                self.playing_mp3 = False

if __name__ == "__main__":
    visualizer = AudioVisualizer()
    try:
        visualizer.run()
    finally:
        visualizer.cleanup()
