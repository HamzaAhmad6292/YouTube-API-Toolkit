from youtube_transcript_api import YouTubeTranscriptApi
def get_video_transcription(video_id):
    data=YouTubeTranscriptApi.get_transcript("video_id")
    return data



print(get_video_transcription("DVH9ke2gwJ0"))
