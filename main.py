import webbrowser
from tkinter import *
from tkinter import ttk
import os
import threading
from youtube_dl import YoutubeDL
import moviepy.editor as mpe
from tkinter import filedialog


def open_yb():
    webbrowser.open_new_tab("https://www.youtube.com/")


def location():
    global save_loaction
    save_loaction = filedialog.askdirectory(
        initialdir="/home/tazim/Desktop/", title="Choose Loacation")


def download():
    location()
    os.chdir(save_loaction)
    global info
    vedio_format = var.get()
    link_url = link_var.get()
    yb = YoutubeDL()
    yb.add_default_info_extractors()
    info = yb.extract_info(str(link_url), download=False)
    if vedio_format == "144p":
        status_on_start()
        os.system(f"youtube-dl -f 160 {link_url}")
        os.system(f"youtube-dl -f 140 {link_url}")
        merge()
        remove()
        print("144p")
        status_on_end()
    elif vedio_format == "240p":
        status_on_start()
        os.system(f"youtube-dl -f 133 {link_url}")
        os.system(f"youtube-dl -f 140 {link_url}")
        merge()
        remove()
        print("240p")
        status_on_end()
    elif vedio_format == "360p":
        status_on_start()
        os.system(f"youtube-dl -f 18 {link_url}")
        print("360p")
        status_on_end()
    elif vedio_format == "480p":
        status_on_start()
        os.system(f"youtube-dl -f 135 {link_url}")
        os.system(f"youtube-dl -f 140 {link_url}")
        merge()
        remove()
        print("480p")
        status_on_end()
    elif vedio_format == "720p":
        status_on_start()
        os.system(f"youtube-dl -f 22 {link_url}")
        print("720p")
        status_on_end()


def merge():
    vedio_name = info['title']+'-'+info['id']+'.mp4'
    audio_name = info['title']+'-'+info['id']+'.m4a'
    outname = info['title']+'.mp4'
    my_clip = mpe.VideoFileClip(vedio_name)
    audio_background = mpe.AudioFileClip(audio_name)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname, fps=25)


def remove():
    os.remove(info['title']+'-'+info['id']+'.mp4')
    os.remove(info['title']+'-'+info['id']+'.m4a')


def status_on_start():
    status_bar_text_onstart = "Downloading "+info['title']
    status_bar['text'] = status_bar_text_onstart


def status_on_end():
    status_bar_text_onend = "Downloaded "+info['title']
    status_bar['text'] = status_bar_text_onend


window = Tk()
window.geometry('270x200')
logo_image = PhotoImage(file='yt-downloader.png')
window.iconphoto(True, logo_image)
window.title("Youtube Downloader")
link_labelframe = LabelFrame(window, text="Drop the link")
link_var = StringVar()
entry = Entry(link_labelframe, textvariable=link_var)
btn = Button(link_labelframe, text="Get Link", command=open_yb)
entry.pack(side=LEFT, padx=8)
btn.pack(side=RIGHT)
link_labelframe.pack()
quality_labelframe = LabelFrame(window, text="Choose Quality")
var = StringVar()
p144 = ttk.Radiobutton(quality_labelframe, text="144p",
                       value="144p", variable=var).pack(side=LEFT)
p240 = ttk.Radiobutton(quality_labelframe, text="240p",
                       value="240p", variable=var).pack(side=LEFT)
p360 = ttk.Radiobutton(quality_labelframe, text="360p",
                       value="360p", variable=var).pack(side=LEFT)
p480 = ttk.Radiobutton(quality_labelframe, text="480p",
                       value="480p", variable=var).pack(side=LEFT)
p720 = ttk.Radiobutton(quality_labelframe, text="720p",
                       value="720p", variable=var).pack(side=LEFT)
quality_labelframe.pack(pady=5)
download_btn = Button(window, text="Download",
                      command=download)
download_btn.pack(pady=5, fill='x', padx=8)
status_bar = Label(window, text="", bg="Orange")
status_bar.pack(side=BOTTOM, fill='x')
window.mainloop()
