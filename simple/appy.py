from flask import Flask, render_template


appy = Flask(__name__)


@appy.route('/')
def index():
    return render_template('index.html', name='Visitor')


if __name__ == '__main__':
    appy.run(host='0.0.0.0', port=5000, debug=True)