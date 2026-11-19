# Emotion Detection Application Using IBM Watson NLP and Flask

A Flask application and Python package that use IBM Watson NLP EmotionPredict to identify anger, disgust, fear, joy, sadness, and the dominant emotion.

## Project structure

```text
Emotion-Detection-Application/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── tests/
│   └── test_emotion_detection.py
├── .gitignore
├── README.md
├── requirements.txt
└── server.py
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

On Windows use `.venv\\Scripts\\activate`.

## Watson NLP endpoint

The default URL is the IBM Skills Network course-lab EmotionPredict endpoint. If your lab provides a different URL, set `WATSON_EMOTION_URL` before running the app:

```bash
export WATSON_EMOTION_URL="YOUR_LAB_ENDPOINT"
```

Do not commit private credentials or tokens.

## Run

```bash
python3 -c "from EmotionDetection import emotion_detector; print('Import successful')"
python3 server.py
```

Open http://127.0.0.1:5000.

The `/emotionDetector` route accepts a `textToAnalyze` query parameter.

## Tests and static analysis

```bash
python3 -m unittest discover -s tests -v
pylint server.py
```

The unit tests mock the Watson HTTP response and do not require a live service. Report only the Pylint score actually produced by your local run.

## Assignment evidence

Capture genuine screenshots from your own lab/terminal for the required assignment artifacts. No execution screenshots or unverified test/lint results are included in this repository. Confirm the exact endpoint, output wording, and required starter files against your course lab instructions before submission.
