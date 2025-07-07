import torch
import os
from transformers import BlipProcessor, BlipForConditionalGeneration
from app.config import MODEL_NAME

# 🔒 Force offline mode
os.environ["TRANSFORMERS_OFFLINE"] = "1"

def load_model(device_preference: str = "auto"):
    """
    Load the BLIP model and processor with intelligent behavior:
    - Auto-detect device (CPU or GPU)
    - Validate loading
    - Future-ready for model switching / caching / quantization
    """
    print("[🧠] Loading BLIP model and processor...")

    # Device selection: smart fallback
    if device_preference == "auto":
        device = "cuda" if torch.cuda.is_available() else "cpu"
    else:
        device = device_preference

    try:
        processor = BlipProcessor.from_pretrained(MODEL_NAME)
        model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)

        # Optional: eval mode for better performance in inference
        model.eval()

        print(f"[✅] Model loaded on device: {device.upper()}")
        return processor, model, device

    except Exception as e:
        print(f"[❌] Failed to load model: {e}")
        raise RuntimeError("Model loading failed. Check MODEL_NAME or internet connection.")

