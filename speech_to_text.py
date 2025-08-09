import speech_recognition as sr
from config import AUDIO_FILE, LANGUAGE
from audio_utils import get_audio_duration, is_wav_file

def transcribe_audio(audio_file_path, language=LANGUAGE):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        print(f"Listening to the audio file: {audio_file_path}")
        audio = recognizer.record(source)
    try:
        print("Transcribing...")
        text = recognizer.recognize_google(audio, language=language)
        print("Transcription:")
        print(text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    if not is_wav_file(AUDIO_FILE):
        print("Only WAV files are supported.")
    else:
        try:
            duration = get_audio_duration(AUDIO_FILE)
            print(f"Audio duration: {duration:.2f} seconds")
            transcribe_audio(AUDIO_FILE)
        except Exception as e:
            print(f"Error: {e}")
