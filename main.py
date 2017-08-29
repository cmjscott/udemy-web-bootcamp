from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("imageGallery.html")





if __name__ == '__main__':
    app.run()
