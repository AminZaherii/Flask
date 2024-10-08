from flask import Flask
from flask import request
import controller

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to Flask app'


@app.route('/categories')
def get_categories():
    return controller.get_categories()


@app.route('/categories/add', methods=['POST'])
def add_category():
    category_name = request.json.get('name')
    if not category_name:
        return 'Bad Request'
    return controller.add_category(category_name)


@app.route('/categories/<category_id>')
def get_category_by_id(category_id):
    return controller.get_category_by_id(category_id)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=True)
