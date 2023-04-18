from pytube import YouTube
from pytube.exceptions import PytubeError

if __name__ == "__main__":
    
    link: str = "https://www.youtube.com/watch?v=iEOSJeA2_48"

    try:
        yt = YouTube(link)
        print(f"Title: {yt.title}")
    
    except PytubeError: 
    
        print(f"Could not get youtube link! ")
