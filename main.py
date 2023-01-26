from flask import Flask
from main.view_posts import main_page_blueprint, post_page_blueprint
from add_post.add_post import add_post_blueprint, added_post_blueprint

app = Flask(__name__)
app.register_blueprint(main_page_blueprint)
app.register_blueprint(post_page_blueprint)
app.register_blueprint(add_post_blueprint)
app.register_blueprint(added_post_blueprint)


def do_main():
    app.run(debug=True)


if __name__ == '__main__':
    do_main()
