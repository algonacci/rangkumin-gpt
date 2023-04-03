from flask import Flask, render_template, request
import module as md

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "POST":
        prompt = request.form["prompt"].strip()
        if prompt == "":
            error = "Please enter prompt"
            return render_template("index.html", error=error)
        else:
            print(prompt)
            result = md.generate(prompt=prompt)
        return render_template("index.html", result=result)
    else:
        return render_template("index.html")


@app.errorhandler(400)
def bad_request(error):
    return {
        "status": {
            "code": 400,
            "message": "Client side error!"
        }
    }, 400


@app.errorhandler(404)
def not_found(error):
    return {
        "status": {
            "code": 404,
            "message": "URL Not Found!"
        }
    }, 404


@app.errorhandler(405)
def method_not_allowed(error):
    return {
        "status": {
            "code": 405,
            "message": "Request method not allowed!"
        }
    }, 405


@app.errorhandler(500)
def internal_server_error(error):
    return {
        "status": {
            "code": 500,
            "message": "Server error!"
        }
    }, 500


if __name__ == "__main__":
    app.run()
