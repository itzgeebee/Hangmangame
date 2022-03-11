# A simple game to practice flask routing using gifs.
import random

from flask import Flask



app = Flask(__name__)


@app.route("/")
def start_page():
    return f"<h1>Guess a number between 0 and 9</h1><img src " \
           f"='https://media0.giphy.com/media/8Lc5xmvzRhlLy/100.webp?cid" \
           f"=ecf05e47vrig2tibd30r289i065hgmhphjqkob2i5sd4dfwv&rid=100.webp&ct=g'> "


num = random.choice(range(10))
print(num)


@app.route("/<int:number>")
def enter_num(number):
    answer = int(number)
    if num == number:
        return f"<h1>You are correct</h1>" \
               f"<img src = 'https://media2.giphy.com/media/YZX4FWwOJTK5W/200w.webp?cid" \
               f"=ecf05e476oeln0ldqwlnn7deb7vod69snba9slysz27d0ckh&rid=200w.webp&ct=g'> "
    elif num > number:
        return f"<h1>Too low! Try again</h1>" \
               f"<img src = 'https://media4.giphy.com/media/12nAroWqMbb8Bi/giphy.webp?cid" \
               f"=ecf05e4737c488230aayd6h8kj4qlus0gr237z1shntvhx68&rid=giphy.webp&ct=g'> "
    elif num < number:
        return f"<h1>Too High! Try again</h1>" \
               f"<img src = 'https://media4.giphy.com/media/KI14N7D3AJ4SA/200w.webp?cid" \
               f"=ecf05e475y1sty494u2cvghb5uws74i18jfi2qgz6oiv0wlh&rid=200w.webp&ct=g'> "


if __name__ == "__main__":
    app.run(debug=True)
