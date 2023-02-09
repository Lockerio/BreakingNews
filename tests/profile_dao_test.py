from profile.dao.profile_data_dao import ProfileDataDAO
import pytest


profile_dao = ProfileDataDAO()
profile_parameters = [
    (1, {
        "id": 1,
        "name": "Олег Араб",
        "photo": "static/resources/images/profile/Oleg_Arab.jpg",
        "posts": [1]
    })
]


class ProfileDAOTest:
    @staticmethod
    @pytest.mark.parametrize("profile_id", "profile_data", )
    def get_profile_test(profile_id, profile_data):
        assert profile_dao.get_profile(profile_id) == profile_data


def do_main():
    pass


if __name__ == '__main__':
    do_main()
