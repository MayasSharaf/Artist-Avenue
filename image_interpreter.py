from collections import Counter
from PIL import Image, ImageFilter
import numpy as np

def extract_dominant_color(image, k=4):
    """Return the dominant RGB color in the image using pixel clustering logic."""
    img = image.resize((150, 150))  # Resize for speed
    data = np.array(img).reshape(-1, 3)
    color_counts = Counter(map(tuple, data))
    dominant = color_counts.most_common(1)[0][0]
    return tuple(int(c) for c in dominant)

def classify_mood_by_color(rgb):
    """Classify general mood based on dominant color."""
    r, g, b = rgb

    # Normalize for weighted distance
    total = max(r + g + b, 1)
    r_ratio, g_ratio, b_ratio = r / total, g / total, b / total

    if r_ratio > 0.5 and g_ratio < 0.25:
        return "warm and energetic"
    elif b_ratio > 0.5 and r_ratio < 0.25:
        return "cool and calm"
    elif g_ratio > 0.4 and r_ratio > 0.3:
        return "fresh and natural"
    elif r > 180 and g > 180 and b < 120:
        return "sunny and joyful"
    elif r < 100 and g < 100 and b < 100:
        return "dark and moody"
    else:
        return "neutral and soft"

def guess_art_style(image):
    """Guess art style based on basic heuristics like aspect ratio and brush-like features."""
    width, height = image.size
    aspect_ratio = width / height

    # Analyze complexity: more edges = potentially abstract or expressive
    grayscale = image.convert("L")
    edge_image = grayscale.filter(ImageFilter.FIND_EDGES)
    edges = np.array(edge_image).astype(np.uint8)
    edge_density = np.count_nonzero(edges > 100) / edges.size

    if edge_density > 0.12:
        return "abstract or expressive"
    elif aspect_ratio > 1.8:
        return "panoramic landscape"
    elif aspect_ratio < 0.8:
        return "portrait-focused composition"
    else:
        return "balanced and structured"

def interpret_image(image):
    """High-level interface to interpret artistic features of an image."""
    dominant_color = extract_dominant_color(image)
    mood = classify_mood_by_color(dominant_color)
    style = guess_art_style(image)

    # Construct enhanced descriptive prompt
    enhanced_prompt = f"A {mood} painting rendered in {style}."

    return {
        "color": dominant_color,
        "mood": mood,
        "style": style,
        "prompt": enhanced_prompt
    }  
