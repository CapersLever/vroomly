from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ms22902107.txt")
def test():
    return render_template("ms22902107.txt")

if __name__ == "__main__":
    app.run(debug=False)