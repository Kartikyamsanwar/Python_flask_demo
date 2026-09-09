from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>🐍 Python Bootcamp 2026</h1>
    <p>Welcome to our Flask application!</p>
    """


@app.route("/about")
def about():
    return """
    <h2>About</h2>
    <p>This website is built using Python and Flask.</p>
    """


@app.route("/student")
def student():
    return {
        "name": "Python Student",
        "course": "Python Bootcamp",
        "status": "Learning"
    }


if __name__ == "__main__":
    app.run(debug=True)

#pip install -r requirements.txt
#python app.py