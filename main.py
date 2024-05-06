url = "https://www.youtube.com/watch?v=xYjUMUdMfIU"


from youtube_transcript_api import YouTubeTranscriptApi

x = YouTubeTranscriptApi.get_transcript("xYjUMUdMfIU", languages=['es', 'en'])

print(x)