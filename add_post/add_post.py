from flask import render_template, Blueprint, request
from utils import DataWorker

add_post_blueprint = Blueprint('add_post_blueprint', __name__,
                               template_folder='templates', static_folder='../static')
added_post_blueprint = Blueprint('added_post_blueprint', __name__,
                                 template_folder='templates', static_folder='../static')


@add_post_blueprint.route('/add_post')
def add_post():
    return render_template('add_post.html')


@added_post_blueprint.route('/added_post', methods=['POST'])
def added_post():
    author = request.form["author_name"]
    header = request.form["header_text"]
    picture = request.files.get("picture")
    text = request.form["textarea"]

    DataWorker().add_new_post(author, header, picture, text)

    return render_template('added_post.html')


def do_main():
    pass
    
    
if __name__ == '__main__': 
    do_main()
