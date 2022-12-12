from gtts import gTTS

tts = gTTS('ドレミファソラシド', lang='ja')
tts.save('どれみ.mp3')
