from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    files = os.listdir("/raspitracks")
    return render_template("index.html", files=files)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    file.save(os.path.join("/raspitracks", file.filename))
    return "File uploaded successfully!"

if __name__ == "__main__":
    app.run()
