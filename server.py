"""
Server for the ai application. Running on port 5000
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")


@app.route("/")
def render_index_page():
    """
    Renders the index page
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def emote_detector():
    """
    Gets text input from javascript and passes it through
    the emotion detector function
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Invalid text! Please try again!"
    return f'''For the given statement the system response is {str(response)[1:-1]}.
     The dominant emotion is {response['dominant_emotion']}'''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
