from pytube import YouTube
import os
from moviepy.editor import *
import time
import cons
import AudioConverter 

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

#print screen

print("-------------------------------")
print("Welcome to Youtube Downloader!")

url = input("Youtube URL: ")
my_video = YouTube(url)

print("***********Video Title************")
print(my_video.title)
print("-------------------------------")





my_video = my_video.streams.get_highest_resolution()

# my_video = my_video.streams.first()
print("your mp4 file will be downloaded in the folder downloadvideos")
print("-------------------------------")
my_video.download("D:\Auto\downloadvideos")

#converter mp3 wav

video1 = input("Would you like to convert your file into another format?: (1-YES) (2-NO)?: ")
if video1 == "1":



    #yes to convert
    video2 = input("what type of file converter?"
                    "\n1. MP3"
                    "\n2. WAV"
                    "\n3. "
                    "\n4."
                    "\n5. : ")

    #mp3 converter
    if video2 == "1":
        video = input("Put video file path here: ")
        videoint = (video)
        videoex = VideoFileClip(videoint)
        videomp3 = input("name of extract file")
        video.audio.write_audiofile(videomp3)


    #wav converter
    if video2 == "2":
        wav1 = input("Path to file to extract: ")
        wav2 = (wav1)





#no to convert
if video1 == "2":
    print("video is downloaded in your downloadvideos folder!")






time.sleep(1000)
os.close()
