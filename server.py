from mapbox import Directions
from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = "ABC"


@app.route('/')
def homepage():
    """Register page."""
    # return "Welcome to SendACard"
    return render_template("mapboxfun.html")




if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000)
