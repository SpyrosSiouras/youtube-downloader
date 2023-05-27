from pytube import YouTube, Search
from pytube.exceptions import PytubeError

def get_query_results(query: str) -> list[YouTube]:

    try:
        s = Search(query)
        return s.results
    except PytubeError as e:
        print(f"EXCEPTION: {e}")
        return []


if __name__ == "__main__":

    query_results = get_query_results("Sido Astronaut")
    print(len(query_results))
    for result in query_results:
        print(result.thumbnail_url)
    # # link: str = "https://www.youtube.com/watch?v=iEOSJeA2_48"
    # link: str = "https://www.youtube.com/watch?v=UWeAyFrfWz0"
    # yt = None

    # while yt is None: 
    #     try:
    #         yt = YouTube(link)
    #         print(yt.title)

    #     except PytubeError: 
    #         yt = None
    #         print(f"Could not get youtube link! ")
    
    
    # print(f"Title: {yt.title}")
    # print(f"streams : {yt.streams.filter(only_audio = True)[-1]}")
    # # stream = yt.streams.get_by_itag(251)
    # # stream.download()
    # x = 0
    # while x < 30: 
    #     s = Search('Sido Astronaut')
    #     print(f"{x}-{s.results[0].title}")
    #     x += 1
    #     time.sleep(0.1)
    # s.results[0].streams[-1].download()