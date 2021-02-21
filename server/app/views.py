from flask import render_template, send_from_directory

from app import app

# @app.route('/<path:path>', methods=['GET'])
# def static_proxy(path):
#   return send_from_directory('./', path)

@app.route('/', methods=['GET'])
def root():
    return render_template('index.html') # Return index.html 


# @app.route('/about')
# def about():
#     return render_template("about.html")