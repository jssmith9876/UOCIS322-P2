"""
Jordan Smith's Flask API.
"""

from flask import Flask, render_template, abort, send_from_directory
import os
import configparser

app = Flask(__name__)

# Load the docroot from credentials file
config = configparser.ConfigParser()
config.read("credentials.ini")
docroot = config["DEFAULT"]["DOCROOT"]

# For a generic request
@app.route("/<path:request>")
def return_page(request):
    # If the request has a bad character => 403
    if ('~' in request or '..' in request):
        abort(403)

    # If the request exists in the docroot => Return the requested page
    elif (os.path.exists(docroot + request)):
        return send_from_directory(docroot, request)

    # Otherwise, the file doesn't exist => 404
    else:
        abort(404)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def file_forbidden(e):
    return render_template('403.html'), 403


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
