import os
import base64

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<html>
<body>
<h1>Dolphins</h1>

<h2>Coolness of Dolphins</h2>
Very cool.

<h2>Dangers of Dolphins</h2>
Their melodious songs have tempted several sailors into the sea: wear earplugs near dolphins.

<script>
var somethingNefarious = function(data) {
    console.log(data);
}

fetch("https://www.facebook.com/").then(
  function(response) {
    somethingNefarious(response.body);
  }
);
</script>
</body>
    """


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

