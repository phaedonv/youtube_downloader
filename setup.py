import sys
import os

from cx_Freeze import setup, Executable

#add files
files = ["dead.ico"]

#add Target
target = Executable(
    script="download.py",
    base="Win32GUI",
    icon="dead.ico"
)

#setup CX FREEZE
setup(
    name = "DeadPull",
    version = "1.0",
    description = "Pytube YT downloader",
    author = "Neuronic Mantis",
    options = {"build_exe" : {"include_files" : files}},
    executables = [target]
)