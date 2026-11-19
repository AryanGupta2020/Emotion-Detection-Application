"""IBM Watson NLP emotion detection."""

import os

import requests

WATSON_URL = os.getenv(
    "WATSON_EMOTION_URL",
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict",
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
EMOTION_NAMES = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    """Return an empty response when input or service response is invalid."""
    result = {emotion: None for emotion in EMOTION_NAMES}
    result["dominant_emotion"] = None
    return result


def emotion_detector(text_to_analyze):
    """Analyze text with Watson NLP and return emotion scores."""
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()

    headers = {"grpc-metadata-mm-model-id": MODEL_ID}
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            WATSON_URL,
            headers=headers,
            json=payload,
            timeout=30,
        )
    except requests.RequestException:
        return _empty_result()

    if response.status_code != 200:
        return _empty_result()

    try:
        prediction = response.json()["emotionPredictions"][0]["emotion"]
        scores = {emotion: prediction[emotion] for emotion in EMOTION_NAMES}
    except (KeyError, IndexError, TypeError, ValueError):
        return _empty_result()

    scores["dominant_emotion"] = max(scores, key=scores.get)
    return scores
