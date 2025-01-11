from flask import Flask, request, render_template_string

app = Flask(__name__)

# Base URL for m3u8 links
BASE_URL = "https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jagobd Danamicaly Play Script</title>
  <script src="//content.jwplatform.com/libraries/SAHhwvZq.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/clappr@latest/dist/clappr.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/level-selector@0.2.0/dist/level-selector.min.js"></script>
  <script disable-devtool-auto src='https://cdn.jsdelivr.net/npm/disable-devtool@latest'></script>
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
    const player = new Clappr.Player({
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
    channel_id = request.args.get('id')
    if not channel_id:
        return "Error: No channel ID provided.", 400

    m3u8_link = f"{BASE_URL}{channel_id}/playlist.m3u8"
    return render_template_string(HTML_TEMPLATE, m3u8_link=m3u8_link)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
