import torch
from app.generators.title_generator import apply_title_template
from app.generators.description_generator import generate_description
from app.config import DEFAULT_PROMPT, MAX_TITLE_TOKENS
from app.brains.image_interpreter import interpret_image  # 🧠 Pre-processing brain
from app.brains.post_processing_brain import post_process_caption  # 🧠 Post-processing brain
from app.brains.feedback_learning_brain import refine_with_feedback  # 🧠 Feedback Learning Brain


class CaptionEngine:
    def __init__(self, processor, model, device="cpu"):
        self.processor = processor
        self.model = model
        self.device = device
        self.model.eval()

    def generate(self, image, prompt=DEFAULT_PROMPT, feedback=None):
        # 🧠 Step 1: Validate input
        if image is None:
            raise ValueError("Image input is required for caption generation.")

        if prompt and not isinstance(prompt, str):
            raise TypeError("Prompt must be a string or None.")

        try:
            # 🧠 Step 2: Interpret image first (Pre-Processing Brain)
            interpretation = interpret_image(image)  # returns mood, style, prompt
            enhanced_prompt = interpretation["prompt"]
            full_prompt = f"{prompt} {enhanced_prompt}" if prompt else enhanced_prompt

            # 🧠 Step 3: Prepare inputs for BLIP (with new prompt)
            inputs = self.processor(images=image, text=full_prompt, return_tensors="pt")
            inputs = {k: v.to(self.device) for k, v in inputs.items()}

            # 🧠 Step 4: Generate caption
            output = self.model.generate(**inputs, max_new_tokens=MAX_TITLE_TOKENS)
            raw_caption = self.processor.decode(output[0], skip_special_tokens=True).strip()

            # 🧠 Step 4.5: Post-Processing Brain - Refine caption
            refined_caption = post_process_caption(raw_caption)

            # 🧠 Step 4.6: Apply Feedback Learning Brain if feedback is provided
            if feedback:
             refined_caption = refine_with_feedback(refined_caption, feedback)
            
            # 🧠 Step 5: Clean & extract base title
            base_title = refined_caption.split(":")[0] if ":" in refined_caption else refined_caption
            base_title = base_title.strip().capitalize()

            # 🧠 Step 6: Generate intelligent title & description
            final_title = apply_title_template(base_title)
            description = generate_description(base_title)

            # ✅ Step 7: Return full structured output with interpretation metadata
            return {
                "title": final_title,
                "description": description,
                "raw_caption": raw_caption,
                "refined_caption": refined_caption,
                "mood": interpretation["mood"],
                "style": interpretation["style"],
                "dominant_color": interpretation["color"]
            }

        except Exception as e:
            print(f"[❌] Caption generation failed: {e}")
            raise RuntimeError("Failed to generate caption from image.")
