from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('example.mp3')

# Mengonversi file audio ke format lain
audio.export('result.wav', format='wav')