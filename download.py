# You need to install moviepy && pytube
# pip install moviepy
# pip install pytube

# For creating Windows executables
# pip install pyinstaller

from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
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
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

logo_img = PhotoImage(file="cute_d.png")
#resize
logo_img = logo_img.subsample(4, 4)
canvas.create_image(250, 80, image=logo_img)

#add temporary directional text into txt-field
def temp_text(e):
   link_field.delete(0,"end")

#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Video Url: ", font=('Roboto', 18))
#temporary
link_field.insert(0, "Please press Ctrl V, to paste video url")
link_field.pack(pady=20)
link_field.bind("<FocusIn>", temp_text)

#select save location
path_label = Label(screen, text="Select Pull Location", font=('Roboto', 15))
select_btn = Button(screen, text="Select", command=select_path)

#add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#add widgets
canvas.create_window(250, 190, window=link_label)
canvas.create_window(250, 220, window=link_field)

# Get the data from the clipboard
cliptext = screen.clipboard_get()

#paste button
paste_btn = Button(screen, text="Paste Url", command=paste_url)

canvas.create_window(90, 250, window=paste_btn)

#download buttons
download_btn = Button(screen, text="Pull It", command=download_file)

#add to canvas
canvas.create_window(250, 390, window=download_btn)


###############################################################

screen.mainloop()