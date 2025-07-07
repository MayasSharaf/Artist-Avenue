import random
from difflib import get_close_matches

# 🌍 Main keyword-description mapping
DESCRIPTION_MAP = {
    "sea": "Waves dance gently under a silver sky.",
    "tree": "Branches whisper stories of time and growth.",
    "sun": "A warm glow embraces the earth quietly.",
    "moon": "Soft light graces the calm of night.",
    "mountain": "Majestic peaks rise in tranquil power.",
    "flower": "Petals bloom with delicate confidence.",
    "desert": "Endless sands shimmer with ancient secrets.",
    "city": "The skyline hums with quiet ambition.",
    "rain": "Raindrops compose a song of longing.",
    "bird": "Wings trace freedom across open skies.",
    
    # 🆕 Additional keywords
    "forest": "A symphony of life rustles in the leaves.",
    "cloud": "Soft shapes drift in a boundless ballet.",
    "river": "A winding whisper of time and memory.",
    "fire": "Crimson flames dance in wild rhythm.",
    "dream": "A surreal landscape of feeling and thought.",
    "sky": "The heavens stretch in infinite wonder.",
    "ice": "Frozen beauty in silent brilliance.",
    "light": "Illumination wraps the world in warmth.",
    "shadow": "Mystery walks softly in the dark.",
    "wind": "Invisible threads stir stories untold."
}

# 🌠 Multiple poetic fallback descriptions
FALLBACK_DESCRIPTIONS = [
    "A silent expression of emotion and color.",
    "An untold story painted in hues and shapes.",
    "A visual echo of thoughts unspoken.",
    "Where feelings take form beyond words.",
    "A poetic dance between color and soul."
]

def extract_keyword(title: str):
    candidates = DESCRIPTION_MAP.keys()
    matches = get_close_matches(title.lower(), candidates, n=1, cutoff=0.6)
    return matches[0] if matches else None

def generate_description(base_title: str) -> str:
    keyword = extract_keyword(base_title)
    if keyword:
        return DESCRIPTION_MAP[keyword]
    else:
        return random.choice(FALLBACK_DESCRIPTIONS)
