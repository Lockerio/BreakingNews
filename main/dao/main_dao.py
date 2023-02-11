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

    def get_posts_data_for_main_page(self):
        posts_for_main_page = []
        data = self.get_posts()
        for post in data:
            posts_for_main_page.append({
                "id": post["id"],
                "author_id": post["author_id"],
                "author": post["author"],
                "header": post["header"],
                "picture": post["picture"]
            })
        return posts_for_main_page

    def get_post_data_for_post_page(self, post_id):
        data = self.get_posts()
        post_data = data[post_id]
        post_for_post_page = {
            "id": post_data["id"],
            "author": post_data["author"],
            "header": post_data["header"],
            "text": post_data["text"],
            "tags": post_data["tags"]
        }
        return post_for_post_page

    def find_posts_headers_with_user_text(self, user_text):
        posts = self.get_posts()
        founded_posts_data = []

        for post in posts:
            if user_text in post["header"]:
                founded_posts_data.append(post)
            else:
                for tag in post["tags"]:
                    if user_text in tag:
                        founded_posts_data.append(post)

        founded_posts = []
        for post in founded_posts_data:
            founded_posts.append({
                "id": post["id"],
                "author_id": post["author_id"],
                "author": post["author"],
                "header": post["header"],
                "picture": post["picture"]
            })
        return founded_posts


def do_main():
    data = MainDAO().get_posts_data_for_main_page()
    print(data)


if __name__ == '__main__':
    do_main()
