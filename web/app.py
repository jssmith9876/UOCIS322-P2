"""
Jordan Smith's Flask API.
"""

from flask import Flask, render_template
import os

app = Flask(__name__)
docroot = "templates/"


@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

@app.route("/<request>")
def return_page(request):
    if ('~' in request or '..' in request):
        return file_forbidden()
    elif (os.path.exists(docroot + request)):
        return render_template(f"{request}")
    else:
        return not_found()

def not_found():
    return render_template('404.html'), 404

def file_forbidden():
    return render_template('403.html'), 403
"""
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def file_forbidden(e):
    return render_template('403.html'), 403
"""

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
