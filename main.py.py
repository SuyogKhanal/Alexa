from flask import Flask, render_template, request
from SpeechRec import run_alexa
app = Flask(__name__,template_folder='templates')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    speech_result = request.form.get('speechResult')
    speech_result = speech_result.lower()
    run_alexa(speech_result)
    return render_template('index.html', speech_result=speech_result)

if __name__ == '__main__':
    app.run(debug=True)

