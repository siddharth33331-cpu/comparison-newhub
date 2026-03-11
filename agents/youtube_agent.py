from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

client = OpenAI()


def get_transcript(video_id):

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    text = " ".join([t["text"] for t in transcript])

    return text


def analyze_product(transcript):

    prompt = f"""
    Analyze this product review transcript.

    Extract:
    - Pros
    - Cons
    - Key features
    - Who should buy it

    Transcript:
    {transcript}
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text