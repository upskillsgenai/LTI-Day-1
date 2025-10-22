"""
Azure OpenAI GPT-4o - Image Classification
------------------------------------------
Pass an image file at runtime; the model classifies it
into one of 20 predefined categories.

Usage:
    python image_classification.py path/to/image.jpg
"""

import sys
import os
import base64
import re
from mimetypes import guess_type
from openai import AzureOpenAI


# ============================================================
# Azure OpenAI credentials (replace with your own)
# ============================================================
AZURE_OPENAI_ENDPOINT = "https://xxxxxxxxxxxxx-resource.openai.azure.com/"
AZURE_OPENAI_KEY = "xxxxxxxxxxxxxxxxxxxxxxx"
AZURE_OPENAI_DEPLOYMENT = "gpt-4o"
API_VERSION = "2024-12-01-preview"


# ============================================================
# Predefined 20 categories
# ============================================================
LABELS = [
    "cat",
    "dog",
    "car",
    "bicycle",
    "truck",
    "bus",
    "airplane",
    "boat",
    "train",
    "person",
    "tree",
    "flower",
    "building",
    "computer",
    "phone",
    "book",
    "chair",
    "food",
    "animal",
    "landscape",
]


# ============================================================
# Initialize Azure OpenAI client
# ============================================================
client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version=API_VERSION,
    base_url=f"{AZURE_OPENAI_ENDPOINT}openai/deployments/{AZURE_OPENAI_DEPLOYMENT}",
)


# ============================================================
# Convert image file to Base64 Data URL
# ============================================================
def image_to_data_url(path: str) -> str:
    mime, _ = guess_type(path)
    if not mime:
        mime = "application/octet-stream"
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{b64}"


# ============================================================
# Classify image using GPT-4o
# ============================================================
def classify_image(image_path: str) -> str:
    data_url = image_to_data_url(image_path)
    label_str = ", ".join(LABELS)

    system_prompt = "You are an image classifier. Choose exactly one label. If image not belong to Given Category mentioned Category name - Other "
    user_prompt = (
        f"Allowed labels: [{label_str}]. "
        "Return only the label name as plain text — no explanation or JSON."
    )

    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": data_url, "detail": "auto"},
                    },
                ],
            },
        ],
        max_tokens=50,
    )

    label = response.choices[0].message.content.strip()
    label = re.sub(r"[^a-zA-Z0-9\s_-]", "", label).strip().lower()
    return label


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python image_classification.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]

    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        sys.exit(1)

    print(f"\n🔍 Classifying image: {image_path}\n")
    label = classify_image(image_path)
    print(f"✅ Predicted label: {label}")
