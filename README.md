# Real-Time Music Visualizer

A Python application that captures audio input from your microphone and displays a real-time waveform visualization.

## Requirements
- Python 3.x
- Virtual environment
- Required packages are listed in `requirements.txt`

## Setup and Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows: `.\venv\Scripts\activate`
- Unix/MacOS: `source venv/bin/activate`

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Ensure your microphone is connected and working
2. Activate the virtual environment if not already activated
3. Run the program:
```bash
python music_visualizer.py
```
4. Speak or play music to see the audio waveform visualization
5. Close the matplotlib window to exit the program

## Features
- Real-time audio capture from microphone
- Live waveform visualization
- Adjustable visualization parameters (CHUNK size, sample rate)

## Technical Details
- Uses PyAudio for audio capture
- Matplotlib for real-time visualization
- Numpy for audio data processing
- Sample rate: 44.1kHz
- Frame buffer size: 2048 samples