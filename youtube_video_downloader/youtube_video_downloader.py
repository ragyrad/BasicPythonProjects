import pytube
from pytube import StreamQuery


def get_qualities(video_streams: "StreamQuery") -> list:
    """Return available qualities"""
    qualities = []
    for quality in video_streams:
        qualities.append(quality.resolution)
    qualities.append("audio only")
    return qualities


def show_qualities(qualities):
    """Show available qualities"""
    i = 1
    for quality in qualities:
        print(f"{i} - {quality}")
        i += 1


# https://www.youtube.com/watch?v=9NWd8Sb0fFk&ab_channel=%D0%90%D1%80%D1%82%D1%91%D0%BC%D0%9F%D1%83%D0%BC%D0%BF%D1%83%D1%88%D0%BA%D0%B8%D0%BD
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
        chosen_quality = available_qualities[chosen_quality_idx - 1]
        quality_chosen = True
    else:
        print("Write the index of quality")

if chosen_quality != "audio only":
    chosen_stream = video_streams.filter(res=chosen_quality)
    chosen_stream.first().download()
# download audio stream anyway
audio_stream.download()
