#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pyautogui",
#     "realtimestt",
#     "requests",
#     "nvidia-cublas-cu12",
#     "nvidia-cudnn-cu12",
# ]
# ///

import tkinter as tk
import pyautogui

root = tk.Tk()

root.title("A Tkinter App")

root.geometry("1000x1000")
root.configure(bg='black')
root.wait_visibility(root)
# root.wm_attributes("-fullscreen", True)
root.wm_attributes("-alpha", 0.6)
root.attributes('-topmost', True)

width = root.winfo_width()
entry_height = root.winfo_height()/12

#"DaddyTimeMono Nerd Font Mono
entry = tk.Entry(font=("Monaco", 24), bd=3, fg="white", bg="black")

# entry = tk.Entry(root)
# define the function accepting the event parameter:
def submit(event):
    text = entry.get()
    print(f"text: {text}")
    root.destroy()
    pyautogui.write(text + "\n")
    root.quit()

entry.bind('<Return>', submit)



# entry.wm_attributes("-alpha", 0.8)
# entry.configure(bg='white')
entry_width = entry.winfo_width()
# entry.place(x=x,  y=height/2)
entry.place(relx=.5, rely=.6, anchor="c")
entry.focus_set()
# Now user can use Typist or just type.
# Then, after typist or the user hit return:
# pyautogui.typewrite(text + " ")






root.mainloop()
