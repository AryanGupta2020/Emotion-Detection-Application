"""Unit tests for the emotion detector."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector, WATSON_URL


class TestEmotionDetector(unittest.TestCase):
    """Test valid and invalid service responses."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_successful_response(self, mock_post):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.01,
                    "disgust": 0.02,
                    "fear": 0.03,
                    "joy": 0.90,
                    "sadness": 0.04,
                }
            }]
        }
        mock_post.return_value = response

        result = emotion_detector("I am happy today!")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.90)
        mock_post.assert_called_once()
        self.assertEqual(mock_post.call_args.args[0], WATSON_URL)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_non_200_response(self, mock_post):
        response = Mock()
        response.status_code = 400
        mock_post.return_value = response

        result = emotion_detector("invalid request")

        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["anger"])

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_blank_input(self, mock_post):
        result = emotion_detector("  ")

        self.assertIsNone(result["dominant_emotion"])
        mock_post.assert_not_called()


if __name__ == "__main__":
    unittest.main()
