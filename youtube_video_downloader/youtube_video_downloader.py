import pytube
from pytube import StreamQuery


def get_qualities(video_streams: "StreamQuery") -> list[dict]:
    """Return available qualities"""
    qualities = []
    for quality in video_streams:
        quality_dict = {"resolution": quality.resolution, "fps": quality.fps}
        qualities.append(quality_dict)
    qualities.append("audio only")
    return qualities


def show_qualities(qualities):
    """Show available qualities"""
    i = 1
    for quality in qualities:
        if quality != "audio only":
            print(f"{i} - {quality['resolution']} {quality['fps']}fps")
        else:
            print(f"{i} - {quality}")
        i += 1


while True:
    try:
        video_url = input("Input the link to the video you want to download: ")
        yt = pytube.YouTube(video_url)
        break
    except pytube.exceptions.RegexMatchError:
        print(f'The Regex pattern did not return any matches for the video: {video_url}')
    except pytube.exceptions.ExtractError:
        print(f'An extraction error occurred for the video: {video_url}')

    except pytube.exceptions.VideoUnavailable:
        print(f'The following video is unavailable: {video_url}')


all_streams = yt.streams
video_streams = all_streams.filter(mime_type="video/mp4", adaptive=True)
# audio stream in the best quality
audio_stream = all_streams.filter(mime_type="audio/webm").last()

available_qualities = get_qualities(video_streams)

show_qualities(available_qualities)

quality_chosen = False
while not quality_chosen:
    chosen_quality_idx = int(input(f"Choose quality: "))
    if chosen_quality_idx in range(1, len(available_qualities) + 1):
        chosen_quality = available_qualities[chosen_quality_idx]
        quality_chosen = True
    else:
        print("Write the index of quality")

if chosen_quality != "audio only":
    chosen_quality = chosen_quality['resolution']
    chosen_stream = video_streams.filter(res=chosen_quality)
    chosen_stream.first().download()
# download audio stream anyway
audio_stream.download()
