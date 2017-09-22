from flask import Flask, render_template, request, url_for, redirect, session, app

app = Flask(__name__, static_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

if __name__=='__main__':
    app.run(host='0.0.0.0', port=2809, debug=True, threaded=True)