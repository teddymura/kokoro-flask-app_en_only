from flask import Flask, render_template, request, send_file
import subprocess
import os
import uuid
import sys
print("Using Python executable:", sys.executable)


app = Flask(__name__)

MODEL_PATH = r"C:\Users\teddy\.cache\kokoro\kokoro-v1.0.onnx"
VOICES_PATH = r"C:\Users\teddy\.cache\kokoro\voices-v1.0.bin"

# 利用可能ボイス一覧
VOICES = {
    "af_heart": "Heart （女性・明るく元気）",
    "af_alloy": "Alloy（女性・明るくクリア）",
    "af_nova": "Nova（女性・柔らかく自然）",
    "af_sarah": "Sarah（女性・落ち着いたトーン）",
    "am_adam": "Adam（男性・標準的）",
    "am_eric": "Eric（男性・低めナレーション向け）",
    "bm_george": "George（男性・UK）",
    "bf_emma": "Emma（女性・UK）",
}

@app.route("/", methods=["GET", "POST"])
def index():
    output_file = None
    if request.method == "POST":
        text = request.form["text"]
        voice = request.form["voice"]

        input_path = f"input_{uuid.uuid4().hex}.txt"
        output_path = f"static/output_{uuid.uuid4().hex}.wav"

        # テキストファイル作成
        with open(input_path, "w", encoding="utf-8") as f:
            f.write(text)

        # kokoro_ttsコマンド実行
        cmd = [
            "python", "-m", "kokoro_tts",
            input_path, output_path,
            "--model", MODEL_PATH,
            "--voices", VOICES_PATH,
            "--voice", voice
        ]
        subprocess.run(cmd, check=True)

        os.remove(input_path)  # 一時ファイル削除
        output_file = output_path

    return render_template("index.html", voices=VOICES, output_file=output_file)


@app.route("/download/<path:filename>")
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
