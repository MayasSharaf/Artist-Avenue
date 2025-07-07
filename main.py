import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, UnidentifiedImageError
from app.model.loader import load_model
from app.model.caption_engine import CaptionEngine
from app.brains.feedback_learning_brain import refine_with_feedback  # 🧠 Feedback Learning Brain

def choose_image():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
        title="🖼️ Select a painting or image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    return file_path

def process_image(image_path):
    try:
        image = Image.open(image_path).convert("RGB")
        return image
    except UnidentifiedImageError:
        print("❌ Error: Selected file is not a valid image.")
        return None
    except Exception as e:
        print(f"❌ Unexpected error while opening image: {e}")
        return None

def main():
    print("🎨 Welcome to the Artistic Title & Description Generator!")

    # Step 1: Let user choose an image
    image_path = choose_image()
    if not image_path:
        print("⚠️ No image selected. Exiting...")
        return

    # Step 2: Load and validate image
    image = process_image(image_path)
    if image is None:
        print("❌ Failed to load image.")
        return

    # Step 3: Load the smart model with device-awareness
    try:
        processor, model, device = load_model()
        engine = CaptionEngine(processor, model, device=device)
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        return

    # Step 4: Generate intelligent caption with enhanced prompt
    try:
        output = engine.generate(image)

        print("\n🎉 Here's your creative output:")
        print("🖌️ Title:", output["title"])
        print("📖 Description:", output["description"])
        print("📄 Raw Caption:", output["raw_caption"])
        print("🧠 Refined Caption:", output["refined_caption"])
        print("🎨 Dominant Color (RGB):", output["dominant_color"])
        print("🌡️ Mood:", output["mood"])
        print("🧑‍🎨 Art Style Guess:", output["style"])

        # 🧠 Optional Feedback Learning Brain
        feedback = input("\n💬 Want to tweak the caption? (e.g., 'make it more poetic', 'simplify', 'add detail'): ").strip()
        if feedback:
            improved_caption = refine_with_feedback(output["refined_caption"], feedback)
            print("\n🛠️ Improved Caption (based on feedback):", improved_caption)

    except Exception as e:
        print(f"❌ Failed to generate caption: {e}")

if __name__ == "__main__":
    main()
