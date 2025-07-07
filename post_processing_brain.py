import re
import random

def post_process_caption(caption: str) -> str:
    """
    Elevates an art-related caption by:
    - Fixing grammar and punctuation
    - Enriching with poetic and metaphorical vocabulary
    - Introducing artistic flourishes
    - Expanding emotional and stylistic context
    """
    # 1. Grammar & punctuation
    caption = caption.strip().capitalize()
    if not caption.endswith('.'):
        caption += '.'

    # 2. Poetic and expressive replacements
    poetic_replacements = {
        r"\ba painting of\b": "a soul-borne glimpse of",
        r"\ban image of\b": "a timeless impression of",
        r"\ba drawing of\b": "a hand-woven tale of",
        r"\ba scene of\b": "a realm of",
        r"\ban abstract of\b": "a dreamscape of",
        r"\bshows\b": "reveals",
        r"\bis shown\b": "is unveiled",
        r"\bdepicts\b": "echoes",
        r"\bcaptures\b": "immortalizes",
        r"\bpresents\b": "unfolds",
        r"\bfeatures\b": "celebrates",
        r"\bis\b": "exists as",
        r"\bwas created by\b": "was conceived by",
        r"\bbrings forth\b": "summons",
        r"\bexpresses\b": "whispers",
        r"\bshows the essence of\b": "bares the heart of",
        r"\breveals the beauty of\b": "uncovers the hidden poetry of",
        r"\bin the style of\b": "woven in the threads of",
        r"\bsymbolizes\b": "is a reflection of",
        r"\bis depicted as\b": "is shaped as",
        r"\billustrates\b": "paints a portrait of",
        r"\bcaptures the spirit of\b": "imbues the soul with",
        r"\bis framed by\b": "is embraced by",
        r"\bholds the message of\b": "carries the whispers of",
    }

    for pattern, poetic in poetic_replacements.items():
        caption = re.sub(pattern, poetic, caption, flags=re.IGNORECASE)

    # 3. Rescue overly generic captions
    if caption.strip().lower() in {"a painting.", "an image.", "a drawing."}:
        caption = "An untold story wrapped in strokes of color, waiting to unfold."

    # 4. Add artistic flourishes occasionally
    artistic_flourishes = [
        "an eternal dance of light and shadow",
        "a melody painted with color",
        "a fleeting moment captured in time",
        "the soul’s expression through the canvas",
        "a voyage of imagination",
        "the visual language of the heart",
        "a dream woven in hues",
        "an invitation to an unseen world",
        "a journey into the unknown",
        "the echoes of a distant memory",
        "a canvas that breathes emotion",
    ]
    if random.random() < 0.3:
        flourish = random.choice(artistic_flourishes)
        caption += f" It is {flourish}."

    # 5. Expand moods/styles if mentioned
    mood_expansions = {
        "fresh": "a breath of air from untouched forests",
        "natural": "born from the earth, eternal and pure",
        "balanced": "a perfect harmony of elements",
        "structured": "a carefully designed masterpiece",
        "calm": "the quiet stillness of dawn",
        "energetic": "an explosion of life and color",
        "abstract": "a fluid dance of chaotic yet beautiful lines",
        "vibrant": "a burst of living energy captured in hues",
    }

    for mood, expansion in mood_expansions.items():
        pattern = rf"\b{mood}\b"
        if re.search(pattern, caption, re.IGNORECASE):
            caption = re.sub(pattern, expansion, caption, flags=re.IGNORECASE)

    # 6. Final touch: clean-up extra spacing and stray words
    caption = re.sub(r"\s{2,}", " ", caption).strip()

    return caption




#########################################
#########################################
#########################################
#########################################

# ## 🧠 Summary:
# | Step | What it does | Artistic Role |
# |------|--------------|----------------|
# | 1. Grammar Fix | Capitalizes & ends sentence | Makes it grammatically correct |
# | 2. Poetic Substitution | Replaces common phrases | Adds emotion and metaphor |
# | 3. Generic Rescue | Rewrites boring captions | Gives soul to flat phrases |
# | 4. Flourishes | Adds random poetic phrase | Makes it more whimsical |
# | 5. Mood Expansion | Expands emotion words | Deepens style/mood context |
# | 6. Clean-up | Removes excess space | Polishes the output |

# ---

# ### 🖼️ Example Transformation:

# **Input:**  
# `"a painting of a sunset in the style of Monet"`

# **Possible Output:**  
# `"A soul-borne glimpse of a sunset woven in the threads of Monet. It is a melody painted with color."`

# ---
