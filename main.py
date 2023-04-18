from pytube import YouTube
from pytube.exceptions import PytubeError

if __name__ == "__main__":
    
    link: str = "https://www.youtube.com/watch?v=iEOSJeA2_48"
    yt = None

    while yt is None: 
        try:
            yt = YouTube(link)
            print(yt.title)

        except PytubeError: 
            yt = None
            print(f"Could not get youtube link! ")
    
    
    print(f"Title: {yt.title}")
