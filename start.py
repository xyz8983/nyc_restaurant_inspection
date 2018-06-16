from flask import Flask, request, render_template

app = Flask(__name__)

from utils import clean_data


@app.route('/')
def index():
    df = clean_data()
    params ={
        'name': 'Friday',
        'task': 'Fun envent',
        'df': df.head()
    }
    return render_template('index.html', params=params)
#
# if __name__ == '__main__':
#     app.run()