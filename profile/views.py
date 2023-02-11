from flask import render_template, Blueprint, request
from profile.dao.profile_data_dao import ProfileDataDAO


profile_blueprint = Blueprint('profile_blueprint', __name__, template_folder='templates', static_folder='../static')


@profile_blueprint.route('/profile/<int:profile_id>')
def profile(profile_id):
    profile_data_dao = ProfileDataDAO()
    user_profile = profile_data_dao.get_profile(profile_id)
    profile_posts = profile_data_dao.get_profile_posts(user_profile["posts"])
    grouped_posts = profile_data_dao.get_profile_posts_grouped_by_three_ones(profile_posts)
    return render_template('profile.html', profile=user_profile, grouped_posts=grouped_posts)


def do_main():
    pass
    
    
if __name__ == '__main__': 
    do_main()
