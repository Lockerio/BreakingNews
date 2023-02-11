import json


class ProfileDataDAO:
    @staticmethod
    def get_profiles():
        """
        Функция для чтения и перезаписи данных из JSON файла профилей в переменную.
        :return: Список всех профилей.
        """
        with open('data/profiles.json', 'r', encoding='utf-8') as file:
            profiles = json.load(file)
        return profiles

    def get_profile(self, profile_id):
        """
        Функция, которая возвращает информацию о конкретном профиле.
        :param profile_id: Id профиля.
        :return: Словарь информации о профиле.
        """
        profiles = self.get_profiles()
        profile = profiles[profile_id]
        return profile

    @staticmethod
    def get_posts():
        """
        Функция для чтения и перезаписи данных из JSON файла в переменную.
        :return: Список словарей постов.
        """
        with open('data/posts.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_profile_posts(self, profile_posts_id):
        posts = self.get_posts()
        profile_posts = [post for post in posts if post["id"] in profile_posts_id]
        return profile_posts

    @staticmethod
    def get_profile_posts_grouped_by_three_ones(posts):
        posts_amount_in_group = 3
        grouped_posts = [posts[i:i + posts_amount_in_group] for i in range(0, len(posts), posts_amount_in_group)]
        return grouped_posts


def do_main():
    pass

    
if __name__ == '__main__': 
    do_main()
