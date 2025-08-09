# Speech Recognition System

This project is a basic speech-to-text system using Python and the SpeechRecognition library. It can transcribe short audio clips into text using pre-trained models and Google’s free API.

## Features
- Transcribes audio files (WAV format)
- Simple and easy to use
- Modular code for easy enhancements

## How to Use
1. Place your audio file (e.g., `sample.wav`) in the project folder.
2. Install dependencies:
   - `SpeechRecognition`
   - `PyAudio` (for microphone input, optional)
3. Run the script:
   ```powershell
   & ".venv\Scripts\python.exe" speech_to_text.py
   ```

## Enhancements
- Add support for microphone input
- Add support for multiple audio formats
- Use advanced models like Wav2Vec2 for better accuracy

---

## Files
- `speech_to_text.py`: Main script for transcribing audio files
- `audio_utils.py`: Utility functions for audio processing
- `config.py`: Configuration settings
