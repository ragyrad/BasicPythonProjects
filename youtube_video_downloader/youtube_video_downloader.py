import tkinter as tk
import pytube
from pytube import StreamQuery

WIDTH = 800
HEIGHT = 400
CHOSEN_VIDEO = None
CHOSEN_AUDIO = None
VIDEO_STREAMS = None


def get_qualities(video_streams: "StreamQuery") -> list[dict]:
    """Return available qualities"""
    qualities = []
    for quality in video_streams:
        quality_dict = {"resolution": quality.resolution, "fps": quality.fps}
        qualities.append(quality_dict)
    qualities.append("audio only")
    return qualities


def fill_quality_listbox(video_streams):
    """fills the listbox with available video qualities"""
    qualities = get_qualities(video_streams)
    listbox.delete(0, tk.END)
    for q in qualities:
        if q != "audio only":
            listbox.insert(tk.END, f'{q["resolution"]} {q["fps"]}fps')
        else:
            listbox.insert(tk.END, "audio only")


def filter_streams(yt):
    """filter video streams by mime type mp4 and select one best quality audio stream"""
    global VIDEO_STREAMS, CHOSEN_AUDIO
    all_streams = yt.streams
    VIDEO_STREAMS = all_streams.filter(mime_type="video/mp4", adaptive=True)
    # audio stream in the best quality
    CHOSEN_AUDIO = all_streams.filter(mime_type="audio/webm").last()
    fill_quality_listbox(VIDEO_STREAMS)


def find_video(event):
    """change videname_label and return video"""
    try:
        video_url = message_entry.get()
        yt = pytube.YouTube(video_url)
        videoname_label.configure(text=yt.title)
    except pytube.exceptions.RegexMatchError:
        videoname_label.configure(text='The Regex pattern did not return any matches for this video')
    except pytube.exceptions.ExtractError:
        videoname_label.configure(text='An extraction error occurred for this video')
    except pytube.exceptions.VideoUnavailable:
        videoname_label.configure(text='The following video is unavailable')
    filter_streams(yt)


def choose_video_quality(event):
    """choose video quality when user click on listbox"""
    global CHOSEN_AUDIO, CHOSEN_VIDEO, VIDEO_STREAMS
    download_button.configure(state=tk.ACTIVE)
    widget = event.widget
    selection = widget.curselection()
    picked_quality = widget.get(selection[0])
    if picked_quality != "audio only":
        res = picked_quality.split()[0]
        fps = int(picked_quality.split()[1].replace("fps", ""))
        CHOSEN_VIDEO = VIDEO_STREAMS.filter(res=res, fps=fps)
    else:
        CHOSEN_VIDEO = None


def download_video(event):
    """download selected streams"""
    if CHOSEN_VIDEO is not None:
        CHOSEN_VIDEO.first().download()
    CHOSEN_AUDIO.download()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry(f'{WIDTH}x{HEIGHT}')
    root.resizable(width=False, height=False)
    root.title("VideoDownloader")

    message = tk.StringVar()
    message_entry = tk.Entry(textvariable=message, width=WIDTH//10)
    message_entry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    input_label = tk.Label(root, text="enter video link:", font=("Arial Bold", 14))
    input_label.place(relx=0.5, rely=0.13, anchor=tk.CENTER)

    videoname_label = tk.Label(root, text="", font=("Arial Bold", 10))
    videoname_label.place(relx=0.5, rely=0.27, anchor=tk.CENTER)

    listbox = tk.Listbox(root, width=WIDTH//20, font=("Arial Bold", 12))
    listbox.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    download_button = tk.Button(root, text="download", font=("Arial Bold", 12), state=tk.DISABLED)
    download_button.place(relx=0.5, rely=0.93, anchor=tk.CENTER)

    message_entry.bind('<Return>', find_video)
    download_button.bind('<Button-1>', download_video)
    listbox.bind('<<ListboxSelect>>', choose_video_quality)

    root.mainloop()
