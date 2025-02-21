import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
        
    def update_plot(self, frame):
        data = self.stream.read(CHUNK, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.float32)
        self.line.set_ydata(audio_data)
        return self.line,
        
    def run(self):
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

if __name__ == "__main__":
    visualizer = AudioVisualizer()
    try:
        visualizer.run()
    finally:
        visualizer.cleanup()