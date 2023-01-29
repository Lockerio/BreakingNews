from flask import render_template, Blueprint, request
from utils import DataWorker

main_page_blueprint = Blueprint('main_page_blueprint', __name__, template_folder='templates', static_folder='../static')
post_page_blueprint = Blueprint('post_page_blueprint', __name__, template_folder='templates', static_folder='../static')
search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates', static_folder='../static')


@search_blueprint.route('/search')
def search():
    text = request.args['user_text']
    posts = DataWorker().find_posts_headers_with_user_text(text)
    amount = len(posts)
    return render_template('search.html', posts=posts, amount=amount)


@main_page_blueprint.route('/post/<int:post_id>')
def post_page(post_id):
    data = DataWorker().convert_json_to_data()
    post = data[post_id]
    return render_template('post.html', post=post)


@main_page_blueprint.route('/')
def main_page():
    data = DataWorker().convert_json_to_data()
    return render_template('main.html', posts=data)


def do_main():
    pass


if __name__ == '__main__':
    do_main()
