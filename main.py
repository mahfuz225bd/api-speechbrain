import os
from flask import Flask, request, jsonify
from speechbrain.pretrained import EncoderDecoderASR

# Set the fetching strategy to "copy" to avoid symlink issues
os.environ["SB_FETCH_STRATEGY"] = "copy"

# Initialize Flask app
app = Flask(__name__)

# Load ASR model
asr_model = None
try:
    print("Loading ASR model...")
    asr_model = EncoderDecoderASR.from_hparams(
        source="speechbrain/asr-transformer-transformerlm-librispeech",
        savedir="tmpdir"
    )
    print("ASR model loaded successfully!")
except Exception as e:
    print(f"Failed to load ASR model: {e}")

# Define a route for speech-to-text
@app.route("/api/speech-to-text", methods=["POST"])
def speech_to_text():
    if not asr_model:
        return jsonify({"error": "ASR model not loaded"}), 500

    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files["audio"]

    try:
        # Perform speech recognition
        transcription = asr_model.transcribe_file(audio_file)
        return jsonify({"transcription": transcription})
    except Exception as e:
        return jsonify({"error": f"Failed to transcribe audio: {str(e)}"}), 500

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
