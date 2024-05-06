url = "https://www.youtube.com/watch?v="


from youtube_transcript_api import YouTubeTranscriptApi

x = YouTubeTranscriptApi.get_transcript("", languages=['es', 'en'])

print(x)