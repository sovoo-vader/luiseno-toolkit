# AVStoryRebuilder – Pair Luiseño Audio and Visual Elements for Digital Storytelling

import random

# Example multimedia database
story_segments = [
    {"audio": "audio/01_miyax.mp3", "image": "images/miyax_go.jpg", "text": "míyax – to go"},
    {"audio": "audio/02_tupanax.mp3", "image": "images/tupanax_coyote.jpg", "text": "túpanax – coyote"},
    {"audio": "audio/03_yawush.mp3", "image": "images/yawush_howl.jpg", "text": "yawúsh – howl"}
]

def show_story_segment():
    segment = random.choice(story_segments)
    print(f"🎧 Play Audio: {segment['audio']}")
    print(f"🖼️ Show Image: {segment['image']}")
    print(f"🗣️ Caption: {segment['text']}")

# Example use
if __name__ == '__main__':
    show_story_segment()