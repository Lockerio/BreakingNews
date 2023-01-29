import logging
from flask import Flask
from main.view_posts import main_page_blueprint
from add_post.add_post import add_post_blueprint

app = Flask(__name__)
app.register_blueprint(main_page_blueprint)
app.register_blueprint(add_post_blueprint)
logging.basicConfig(filename="basic.log", encoding="utf-8")


def do_main():
    app.run(debug=True)


if __name__ == '__main__':
    do_main()
