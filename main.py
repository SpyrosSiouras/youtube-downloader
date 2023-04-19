from pytube import YouTube
from pytube.exceptions import PytubeError

if __name__ == "__main__":
    
    # link: str = "https://www.youtube.com/watch?v=iEOSJeA2_48"
    link: str = "https://www.youtube.com/watch?v=UWeAyFrfWz0"
    yt = None

    while yt is None: 
        try:
            yt = YouTube(link)
            print(yt.title)

        except PytubeError: 
            yt = None
            print(f"Could not get youtube link! ")
    
    
    print(f"Title: {yt.title}")
    # print(f"streams : {yt.streams.filter(only_audio = True)}")
    stream = yt.streams.get_by_itag(251)
    stream.download()
