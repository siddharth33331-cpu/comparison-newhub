from youtube_agent import get_transcript, analyze_product

video_id = "VIDEO_ID"

text = get_transcript(video_id)

analysis = analyze_product(text)

print(analysis)