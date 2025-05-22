from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/watch/<video_id>')
def watch(video_id):
    video_url = {
        "1": "https://some-fake-url.com/fake.mp4",
        "2": "https://netflix-mini-demo.s3.us-east-1.amazonaws.com/War2.mp4",  # Your real video
        "3": "https://some-fake-url.com/fake3.mp4"
    }.get(video_id, "")

    return render_template("player.html", video_url=video_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

