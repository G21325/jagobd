from flask import Flask, render_template_string

app = Flask(__name__)

# Base URL for m3u8 links
BASE_URL = "https://app.ncare.live/live-orgin/"

# Channel data
CHANNELS = [
    {
        "name": "ATN MUSIC",
        "id": "atnmusic.stream",
        "logo": "https://i.postimg.cc/tC3qfCTK/ATN-Music.jpg",
    },
    {
        "name": "EKHON TV",
        "id": "globaltv.stream",
        "logo": "https://i.ibb.co/TWkfx37/20240430-223232.png",
    },
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jagobd Channel Preview</title>
  <style>
    body {
      margin: 0;
      background: #000;
      color: #fff;
      font-family: Arial, sans-serif;
    }
    #channel-list {
      display: flex;
      flex-wrap: wrap;
      padding: 10px;
      gap: 10px;
    }
    .channel {
      cursor: pointer;
      width: 150px;
      text-align: center;
    }
    .channel img {
      width: 100%;
      border-radius: 8px;
    }
    .channel-name {
      margin-top: 5px;
    }
  </style>
</head>

<body>
  <div id="channel-list">
    {% for channel in channels %}
    <div class="channel">
      <a href="/play?id={{ channel.id }}" target="_blank">
        <img src="{{ channel.logo }}" alt="{{ channel.name }}">
        <div class="channel-name">{{ channel.name }}</div>
      </a>
    </div>
    {% endfor %}
  </div>
</body>

</html>
"""

PLAY_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Playing {{ channel_name }}</title>
  <script src="//content.jwplatform.com/libraries/SAHhwvZq.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/clappr@latest/dist/clappr.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/level-selector@0.2.0/dist/level-selector.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@clappr/hlsjs-playback@1.0.1/dist/hlsjs-playback.min.js"></script>
  <style>
    body {
      margin: 0;
      background: #000;
    }
    #player {
      height: 100vh;
      width: 100%;
    }
  </style>
</head>

<body>
  <div id="player"></div>

  <script>
    const m3u8_link = "{{ m3u8_link }}";

    // Initialize Clappr player
    new Clappr.Player({
      source: m3u8_link,
      width: '100%',
      height: '100%',
      autoPlay: true,
      stretching: "exactfit",
      aspectratio: "16:9",
      plugins: [HlsjsPlayback, LevelSelector],
      mimeType: "application/x-mpegURL",
      mediacontrol: { seekbar: "red", buttons: "#fff" },
      parentId: "#player"
    });
  </script>
</body>

</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, channels=CHANNELS)

@app.route('/play')
def play():
    channel_id = request.args.get('id')
    if not channel_id:
        return "Error: No channel ID provided.", 400
    
    # Find channel details
    channel = next((ch for ch in CHANNELS if ch['id'] == channel_id), None)
    if not channel:
        return "Error: Channel not found.", 404

    m3u8_link = f"{BASE_URL}{channel_id}/playlist.m3u8"
    return render_template_string(PLAY_TEMPLATE, m3u8_link=m3u8_link, channel_name=channel['name'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
