import gtts
tts = gtts.gTTS(text='สวัสดีค่ะ นักเรียน',lang='th')
tts.save('hello.mp3')