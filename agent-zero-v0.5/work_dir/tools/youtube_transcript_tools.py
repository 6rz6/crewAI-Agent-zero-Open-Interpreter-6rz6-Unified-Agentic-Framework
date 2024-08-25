from youtube_transcript_api import YouTubeTranscriptApi
from langchain.tools import tool

class YoutubeTranscriptTool():
    @tool("transcripts Tool")
    def youtube_transcript_tool(video_url: str):
        """Fetch YouTube video transcripts"""
        video_id = video_url.split("v=")[1]
     
        try:
            
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
            print(len(transcript),"RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
            text_list = [entry['text'] for entry in transcript]
            
            return text_list
            # if len(transcript) >= 201:
            #     return transcript[201]  # Returning the 201st element
            # else:
            return transcript  # Returning the entire transcript if it has fewer than 201 elements
        except Exception as e:
            print(f"Error retrieving transcript: {e}")
            return None