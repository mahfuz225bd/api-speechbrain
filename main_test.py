from flask import Flask
app = Flask(__name__)

@app.route('/test')
def test():
    return 'Test main, test route of api-brainspeech'