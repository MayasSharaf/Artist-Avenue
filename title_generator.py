import random
from collections import defaultdict

# 🎨 Vast & Balanced Title Prefixes (General, Poetic, Flexible)
TITLE_TEMPLATES = [
    "Echoes of", "Dreams of", "Whispers of", "Visions of", "Reflections of",
    "Colors of", "Mysteries of", "Fragments of", "Shadows of", "Light of",
    "Essence of", "Harmony in", "The Spirit of", "A Tale of", "Journey through",
    "Moments of", "Rhythms of", "Brushstrokes of", "Symphony of", "Pulse of",
    "Grace in", "Winds of", "Fire within", "Textures of", "A Glimpse of",
    "Embrace of", "Mirrors of", "Truth in", "Awakening of", "Whirlwind of",
    "Energy of", "Timeless", "Wonders of", "Solitude in", "Waves of",
    "Heart of", "Balance in", "Murmurs of", "Beyond the", "Cradle of"
]

# 🧠 Smart random selection tracker
_selection_history = defaultdict(int)

def _smart_choice(templates):
    """Choose from the list while avoiding overuse of a few options."""
    # Score = base count + small random noise to allow variation
    scored_templates = [
        (template, _selection_history[template] + random.uniform(0, 0.5))
        for template in templates
    ]
    # Sort by lowest use count
    scored_templates.sort(key=lambda x: x[1])
    # Take top 10 least-used options and pick randomly among them
    top_choices = [tpl for tpl, _ in scored_templates[:10]]
    choice = random.choice(top_choices)
    _selection_history[choice] += 1
    return choice

def apply_title_template(base_title: str) -> str:
    prefix = _smart_choice(TITLE_TEMPLATES)
    return f"{prefix} {base_title.capitalize()}"
