import random
from flask import Flask, render_template

from data import get_data_in_rows, authors


app = Flask(__name__, template_folder='templates', static_folder='static')

data = get_data_in_rows()


@app.get('/')
def home():
    random_text = random.choice(random.choice(data))
    random_author = random.choice(authors)
    kwargs = {'row1': data[0], 'row2': data[1], 'row3': data[2],
              'random_text': random_text, 'random_author': random_author}
    return render_template('home.html', **kwargs)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
