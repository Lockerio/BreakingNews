import json


class MainDAO:
    @staticmethod
    def get_posts():
        """
        Функция для чтения и перезаписи данных из JSON файла в переменную.
        :return: Список словарей постов.
        """
        with open('data/posts.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def find_posts_headers_with_user_text(self, user_text):
        posts = self.get_posts()
        founded_posts = []

        for post in posts:
            if user_text in post["header"]:
                founded_posts.append(post)
        return founded_posts


def do_main():
    pass


if __name__ == '__main__':
    do_main()
