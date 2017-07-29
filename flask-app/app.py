from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "http://www.ynetnews.com/PicServer4/2016/05/10/6995374/11.jpg",
    "http://s3.amazonaws.com/iexplore_web/images/assets/000/006/295/original/israel.jpg?1443185316"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5556)
