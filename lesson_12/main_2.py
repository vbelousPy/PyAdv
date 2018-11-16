from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST", "PUT", "DELETE", "HEAD"])
def index():
    if request.method == "GET":
        # return "This is GET"
        return "<html>bla-bla-bla</html>"


if __name__ == "__main__":
    app.run()
