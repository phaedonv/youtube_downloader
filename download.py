# You need to install moviepy && pytube
# pip install moviepy
# pip install pytube

from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

#functions
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

screen = Tk()
title = screen.title("Dead Pull")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

logo_img = PhotoImage(file="cute_d.png")
#resize
logo_img = logo_img.subsample(4, 4)
canvas.create_image(250, 80, image=logo_img)

#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Video Url: ", font=('Roboto', 18))

#select save location
path_label = Label(screen, text="Select Pull Location", font=('Roboto', 15))
select_btn = Button(screen, text="Select", command=select_path)

#add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#add widgets
canvas.create_window(250, 190, window=link_label)
canvas.create_window(250, 220, window=link_field)

#download buttons
download_btn = Button(screen, text="Pull It")

#add to canvas
canvas.create_window(250, 390, window=download_btn)




screen.mainloop()