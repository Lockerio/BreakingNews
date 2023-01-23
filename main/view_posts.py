from flask import render_template, Blueprint
from main.utils import DataWorker

main_page_blueprint = Blueprint('main_page_blueprint', __name__, template_folder='templates', static_folder='../static')
post_page_blueprint = Blueprint('post_page_blueprint', __name__, template_folder='templates', static_folder='../static')

__data = DataWorker().data


@main_page_blueprint.route('/post/<int:post_id>')
def post_page(post_id):
    post = __data[post_id]
    return render_template('post.html', post=post)


@main_page_blueprint.route('/')
def main_page():
    return render_template('main.html', posts=__data)


def do_main():
    pass


if __name__ == '__main__':
    do_main()
