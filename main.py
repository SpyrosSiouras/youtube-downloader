from pytube import YouTube


if __name__ == "__main__":
    
    link: str = "https://www.youtube.com/watch?v=iEOSJeA2_48"

    yt = YouTube(link)

    print(f"Title: {yt.title}")
