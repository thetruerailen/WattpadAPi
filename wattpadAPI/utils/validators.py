
import re

def validate_story_id(story_id):
    if not re.match(r'^\d+$', str(story_id)):
        raise ValueError("Invalid story ID format")
