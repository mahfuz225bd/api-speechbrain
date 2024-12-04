from speechbrain.pretrained import EncoderDecoderASR
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the SpeechBrain ASR model
asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-transformer-transformerlm-librispeech", savedir="tmpdir")

@app.route('/transcribe', methods=['POST'])
def transcribe():
    # Get the audio file from the request
    audio_file = request.files['audio']
    transcript = asr_model.transcribe_file(audio_file)
    return jsonify({"transcript": transcript})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
