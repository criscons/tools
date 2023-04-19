#pip3 install pytube3

from pytube import YouTube

link = "https://www.youtube.com/watch?v=t10QcFx7d5k"
yt=YouTube(link)
yt.streams.get_highest_resolution().download()
print("*" * 10 +"SCARICATO" + "*" * 10 )
