# apps/ai_engine/cnn_model.py

import os
from ultralytics import YOLO
from PIL import Image

# -------------------------------
# LOAD MODEL (ONCE)
# -------------------------------
model = YOLO("yolov8n.pt")


# -------------------------------
# ANALYZE IMAGE
# -------------------------------
def analyze_image_cnn(image_path):
    """
    Real object detection using YOLOv8
    """

    score = 0
    reasons = []

    # -------------------------------
    # FILE SAFETY CHECK
    # -------------------------------
    if not os.path.exists(image_path):
        return 0.0, ["Image file not found"]

    # -------------------------------
    # HANDLE JFIF FORMAT
    # -------------------------------
    if image_path.lower().endswith(".jfif"):
        try:
            img = Image.open(image_path)
            new_path = image_path.replace(".jfif", ".jpg")
            img.save(new_path)
            image_path = new_path
        except Exception:
            return 0.0, ["Unsupported image format"]

    try:
        results = model(image_path)
    except Exception:
        return 0.0, ["Image processing failed"]

    detected_objects = []

    # -------------------------------
    # LABEL CATEGORIES
    # -------------------------------
    weapon_labels = ["knife"]
    risky_context_labels = ["person"]

    # -------------------------------
    # PROCESS RESULTS
    # -------------------------------
    for r in results:
        for box in r.boxes:

            confidence = float(box.conf[0])

            # 🔥 IGNORE LOW CONFIDENCE
            if confidence < 0.4:
                continue

            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            detected_objects.append(label)

            # -------------------------------
            # WEAPON DETECTION
            # -------------------------------
            if label in weapon_labels:
                score += 0.8
                reasons.append(f"Weapon detected: {label}")

            # -------------------------------
            # PERSON CONTEXT (LOW WEIGHT)
            # -------------------------------
            elif label in risky_context_labels:
                score += 0.1
                reasons.append("Person detected")

    # -------------------------------
    # CONTEXT BOOST (WEAPON + PERSON)
    # -------------------------------
    if "knife" in detected_objects and "person" in detected_objects:
        score += 0.2
        reasons.append("Potential harmful context (weapon + person)")

    # -------------------------------
    # MULTIPLE OBJECT BOOST
    # -------------------------------
    if len(detected_objects) >= 3:
        score += 0.1

    # -------------------------------
    # NORMALIZE SCORE
    # -------------------------------
    score = min(score, 1.0)

    # -------------------------------
    # DEFAULT SAFE RESPONSE
    # -------------------------------
    if not reasons:
        reasons.append("No harmful objects detected")

    return round(score, 2), reasons