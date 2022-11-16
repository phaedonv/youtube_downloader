from pytube import YouTube

link = "https://www.youtube.com/watch?v=TEATfq6hPIg"

yt =YouTube(link)

#yt.streams.first().download()

print("***********starting downloading video***********")

yt.streams.get_highest_resolution().download()

print("***********finished download***********")
