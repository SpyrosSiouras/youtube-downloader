from pytube import YouTube, Search
from pytube.exceptions import PytubeError

if __name__ == "__main__":
    try:
        s = Search("eminem without me")
        lista = []
        result_showing = 5
        for x in range(result_showing):
            # print(s.results[x].title)
            lista.append(s.results[x].thumbnail_url)
    except PytubeError:
        print(f"Could not get youtube link! ")

    for v in lista:
        print(f"{v}")
    print("befpr")
    for v in lista:
        if not v.endswith(".jpg"):
            v = v[: (v.find(".jpg") + 4)]
        print(f"{v}")
    # yt=s.results[1]
    # stream = yt.streams.filter(only_audio = True)[-1]
    # while not stream.download():
    #     pass
