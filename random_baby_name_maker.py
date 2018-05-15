import os
import base64
import uuid

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """
    Returns a random baby name.

    The fact that it returns a uuid is a joke.
    """

    return str(uuid.uuid4())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6426))
    app.run(host='0.0.0.0', port=port)

