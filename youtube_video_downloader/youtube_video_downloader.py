from pytube import YouTube


def get_qualities(streams: "StreamQuery") -> list:
    """Return available qualities"""
    qualities = []
    for quality in streams:
        qualities.append(quality.resolution)
    return qualities


def show_qualities(qualities):
    """Show available qualities"""
    i = 1
    for quality in qualities:
        print(f"{i} - {quality}")
        i += 1


video_link = input("Input the link to the video you want to download: ")
yt = YouTube(video_link)

all_streams = yt.streams
video_audio_streams = all_streams.filter(mime_type="video/mp4", progressive=True)
available_qualities = get_qualities(video_audio_streams)
show_qualities(available_qualities)

quality_chosen = False
while not quality_chosen:
    chosen_quality_idx = int(input(f"Choose quality: "))
    if chosen_quality_idx in range(1, len(available_qualities) + 1):
        chosen_quality = available_qualities[chosen_quality_idx - 1]
        quality_chosen = True
    else:
        print("Write the index of quality")

chosen_stream = video_audio_streams.filter(res=chosen_quality)
chosen_stream.first().download()
