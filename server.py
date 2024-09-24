"""Module to start server for flask application"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """Function to render root website"""
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """Function to get the result from user input"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Extract the result from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with the result
    if anger is None:
        formatted_result = "Invalid text! Please try again!."
    else:
        formatted_result = f"For the given statement, the system response is \
          'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} \
          and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    return formatted_result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
