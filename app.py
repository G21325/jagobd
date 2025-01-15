from flask import Flask, request, render_template_string

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
  <title>Jagobd Channel Preview and Play</title>
  <script src="//content.jwplatform.com/libraries/SAHhwvZq.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/clappr@latest/dist/clappr.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/level-selector@0.2.0/dist/level-selector.min.js"></script>
  <script disable-devtool-auto src='https://cdn.jsdelivr.net/npm/disable-devtool@latest'></script>
  <script src="https://cdn.jsdelivr.net/npm/@clappr/hlsjs-playback@1.0.1/dist/hlsjs-playback.min.js"></script>
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
    #player {
      width: 100%;
      height: 60vh;
      background: #000;
    }
  </style>
</head>

<body>
  <div id="channel-list">
    {% for channel in channels %}
    <div class="channel" onclick="playChannel('{{ channel.id }}')">
      <img src="{{ channel.logo }}" alt="{{ channel.name }}">
      <div class="channel-name">{{ channel.name }}</div>
    </div>
    {% endfor %}
  </div>

  <div id="player"></div>

  <script>
    function playChannel(channelId) {
      const m3u8_link = `{{ base_url }}${channelId}/playlist.m3u8`;

      // Clear the existing player
      document.getElementById('player').innerHTML = '';

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
    }
  </script>
</body>

</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, channels=CHANNELS, base_url=BASE_URL)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
