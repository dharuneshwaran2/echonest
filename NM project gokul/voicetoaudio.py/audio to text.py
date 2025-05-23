import os
from pydub import AudioSegment
import speech_recognition as sr

# 🔁 Split audio into 10-second .wav chunks
def split_audio(file_path, chunk_length_ms=10000):
    audio = AudioSegment.from_wav(file_path)  # Only WAV is supported without FFmpeg
    chunks = []

    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunk_name = f"chunk_{i//chunk_length_ms}.wav"
        chunk.export(chunk_name, format="wav")
        chunks.append((chunk_name, i // 1000))  # time in seconds
    return chunks

# 🎙 Transcribe each chunk
def transcribe_chunks(chunks):
    r = sr.Recognizer()
    results = []

    for file, start_time in chunks:
        with sr.AudioFile(file) as source:
            audio = r.record(source)
        try:
            text = r.recognize_google(audio)
            print(f"[{start_time}s] {text}")
            results.append((start_time, text))
        except sr.UnknownValueError:
            print(f"[{start_time}s] ❌ Couldn't understand audio")
        os.remove(file)  # delete temp file
    return results

# 🔍 Keyword search
def search_keyword(transcripts, keyword):
    return [(t, txt) for t, txt in transcripts if keyword.lower() in txt.lower()]

# ▶️ Main
def main():
    file_path = r"C:\Users\Admin\Documents\NM project gokul\cricketoncats_01_euwer_64kb.wav" # WAV only
    print("🔄 Splitting audio...")
    chunks = split_audio(file_path)

    print("🧠 Transcribing...")
    transcripts = transcribe_chunks(chunks)

    keyword = input("\n🔍 Enter keyword to search: ")
    results = search_keyword(transcripts, keyword)

    print("\n📋 Results:")
    if results:
        for time, text in results:
            print(f"⏱ {time}s: {text}")
    else:
        print("❌ No matches found.")

if __name__ == "__main__":
    main()
