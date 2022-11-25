# You need to install moviepy && pytube
# pip install moviepy
# pip install pytube

# For creating Windows executables
# pip install pyinstaller

# For compiling into Windows & other executables!!
#pip install cx_freeze

from os import path
from tkinter import *
from tkinter import filedialog
#from moviepy import *
#from moviepy.editor import VideoFileClip
#import moviepy.editor as moviepy
from moviepy.video.fx.crop import crop

from pytube import YouTube

import shutil

#functions
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def paste_url():
    link_field.insert(0, cliptext)

def download_file():
    #get usr link
    get_link = link_field.get() 
    #get selected link
    user_path = path_label.cget("text")
    screen.title("Pulling...")

    #download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move file 2 selected dir
    shutil.move(mp4_video, user_path)
    screen.title("Dead Pulled!!! Pull Another One...")

def do_popup(event):
    try:
        m.tk_popup(event.x_screen, event.y_screen)
    finally:
        m.grab_release()

screen = Tk()
title = screen.title("Dead Pull")
canvas = Canvas(screen, width=500, height=700)
canvas.pack()

logo_img = PhotoImage(file="DeadPull-sticker.png")
#resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 100, image=logo_img)

#add temporary directional text into txt-field
def temp_text(e):
   link_field.delete(0,"end")

#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Video Url: ", font=('Roboto', 15))
#temporary
link_field.insert(0, "Please press Ctrl V, to paste video url")
link_field.pack(pady=20)
link_field.bind("<FocusIn>", temp_text)

#select save location
path_label = Label(screen, text="Select Pull Location", font=('Roboto', 15))
select_btn = Button(screen, text="Select", command=select_path)

#add to window
canvas.create_window(250, 330, window=path_label)
canvas.create_window(250, 380, window=select_btn)

#add widgets
canvas.create_window(250, 240, window=link_label)
canvas.create_window(250, 270, window=link_field)

# Get the data from the clipboard
cliptext = screen.clipboard_get()

#paste button
paste_btn = Button(screen, text="DON'T PRESS IT", command=paste_url)

canvas.create_window(110, 300, window=paste_btn)

#download buttons
download_btn = Button(screen, text="Pull It", command=download_file)

#add to canvas
canvas.create_window(250, 440, window=download_btn)


###############################################################

screen.mainloop()