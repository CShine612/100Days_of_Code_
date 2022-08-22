from flask import Flask
import random

app = Flask(__name__)


def get_rand_int():
    return random.randint(1, 10)


@app.route("/")
def home_page():
    return "<h1>Pick a number between 1 and 9</h1>" \
           '<iframe src="https://giphy.com/embed/l378khQxt68syiWJy" width="480" height="480" frameBorder="0" ' \
           'class="giphy-embed" allowFullScreen></iframe><p>' \
           '<a href="https://giphy.com/gifs/animation-illustration-retro-l378khQxt68syiWJy">via GIPHY</a></p>'

@app.route("/<int:num>")
def display(num, rand_num=get_rand_int()):
    if num == rand_num:
        return '<h1 style="color:green">You found me!</h1>' \
               '<iframe src="https://giphy.com/embed/UAXK9VGoJTbdcPgmcJ" width="480" ' \
               'height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p>' \
               '<a href="https://giphy.com/gifs/primevideo-2020-borat-subsequent-moviefilm-UAXK9VGoJTbdcPgmcJ">via GIPHY</a></p>'
    elif num < rand_num:
        return '<h1 style="color:red">Too low, Try again!</h1>' \
               '<iframe src="https://giphy.com/embed/PR3585ZZSvcHO9pa76" width="480" ' \
               'height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p>' \
               '<a href="https://giphy.com/gifs/abcnetwork-abc-joel-mchale-card-sharks-PR3585ZZSvcHO9pa76">via GIPHY</a></p>'
    else:
        return '<h1 style="color:blue">Too high, Try again!<h1>' \
               '<iframe src="https://giphy.com/embed/UVsEApdS35zdJitRBd" ' \
               'width="480" height="270" frameBorder="0" class="giphy-embed" ' \
               'allowFullScreen></iframe><p>' \
               '<a href="https://giphy.com/gifs/abcnetwork-abc-to-tell-the-truth-totellthetruth-UVsEApdS35zdJitRBd">via GIPHY</a></p>'



if __name__ == "__main__":
    app.run()
