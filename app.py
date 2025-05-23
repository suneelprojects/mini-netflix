from flask import Flask, render_template

app = Flask(__name__)

# Replace with your CloudFront base URL
CLOUDFRONT_BASE_URL = "https://d1b8sjr5qh3aka.cloudfront.net"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/watch/<video_id>')
def watch(video_id):
    # Use video file names (must match S3 object names)
    video_map = {
        "1": f"{CLOUDFRONT_BASE_URL}/movie1.mp4",
        "2": f"{CLOUDFRONT_BASE_URL}/War2.mp4",
        "3": f"{CLOUDFRONT_BASE_URL}/movie3.mp4"
    }

    video_url = video_map.get(video_id, "")
    return render_template("player.html", video_url=video_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
