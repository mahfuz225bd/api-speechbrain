import logging
from flask import Flask, request, jsonify
from speechbrain.pretrained import EncoderDecoderASR

app = Flask(__name__)

# Set up logging for the sub-app
logging.basicConfig(level=logging.DEBUG)

asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-transformer-transformerlm-librispeech", savedir="tmpdir")

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    try:
        app.logger.info('Received transcription request')
        audio_file = request.files['audio']
        transcript = asr_model.transcribe_file(audio_file)
        app.logger.info('Transcription successful')
        return jsonify({"transcript": transcript})
    except Exception as e:
        app.logger.error(f"Error transcribing audio: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/test', methods=['POST'])
def test():
    return "This is a test route."