import gtts
import playsound

text = input("enter the text to be converted to voice: ")

sound = gtts.gTTS(text,lang="en",tld='co.in')
sound.save("voice.mp3")
playsound.playsound("voice.mp3")
