from gtts import gTTS

f = open('Sample.md', 'r')
tts = gTTS(f.read(), lang='ja')
tts.save('Sample.mp3')
f.close()
