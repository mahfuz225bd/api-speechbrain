from speechbrain.pretrained import EncoderDecoderASR
from flask import Flask, request, jsonify

# Initialize the Flask app for the sub-application
sub_app = Flask(__name__)

# Load the SpeechBrain ASR model
asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-transformer-transformerlm-librispeech", savedir="tmpdir")

@sub_app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    """
    Endpoint to transcribe audio file using the SpeechBrain ASR model.
    """
    # Get the audio file from the request
    audio_file = request.files['audio']
    transcript = asr_model.transcribe_file(audio_file)
    return jsonify({"transcript": transcript})

@sub_app.route('/test', methods=['GET'])
def test_route():
    """
    Test route to check if the sub-app is working.
    """
    return "This is a test route."
