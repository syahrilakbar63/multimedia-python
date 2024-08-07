from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('example.mp3')

# Define clipped_audio
clipped_audio = AudioSegment.from_file('clipped_audio.mp3')

combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')