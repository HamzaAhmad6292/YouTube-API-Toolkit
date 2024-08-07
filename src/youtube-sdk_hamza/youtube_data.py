from youtube_api import YouTubeDataAPI
def get_youtube_data():
    api_key = 'AKAIXXXXXXXX'
    yt = YouTubeDataAPI(api_key)

    data=yt.search('alexandria ocasio-cortez')
    return data