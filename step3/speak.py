from gtts import gTTS
import re
import glob

files = glob.glob("*.md")
for file in files:
  f = open(file, 'r')
  lines = f.readlines()
  # 先頭の見出し文字を削除
  text = "".join(map(lambda x: re.sub('^#+ ', '', x), lines))
  tts = gTTS(text, lang='ja')
  tts.save('sounds/' + file.split('.')[0] + '.mp3')
  f.close()
