"""
Jordan Smith's Flask API.
"""

from flask import Flaski, render_template
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

@app.route("/<request>")
def return_page(request):
    return render_template(f"{request}")

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def file_forbidden(e):
    return render_template('403.html'), 403

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
