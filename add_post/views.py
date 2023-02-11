from flask import render_template, Blueprint, request
from add_post.dao.add_post_dao import AddPostDAO
import logging


add_post_blueprint = Blueprint('add_post_blueprint', __name__,
                               template_folder='templates', static_folder='../static')


@add_post_blueprint.route('/add_post')
def add_post():
    logging.info("Запрошена страничка добавления поста")
    return render_template('add_post.html')


@add_post_blueprint.route('/added_post', methods=['POST'])
def added_post():
    extensions = ["jpg", "jpeg", "png"]

    author = request.form["author_name"]
    author_id = request.form["author_id"]
    header = request.form["header_text"]
    picture = request.files.get("picture")
    text = request.form["textarea"]

    picture_extension = picture.filename.split(".")[-1]
    if picture_extension not in extensions:
        logging.error("У файла неправильное расширение")
        return render_template('add_post.html')

    if not (author and header and picture and text):
        logging.error("Заполнены не все поля")
        return render_template('add_post.html')

    AddPostDAO().add_new_post(author, author_id, header, picture, text)
    logging.info("Запрошена страничка добавленного поста")
    return render_template('added_post.html')


def do_main():
    pass
    
    
if __name__ == '__main__': 
    do_main()
