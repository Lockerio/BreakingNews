import json


class DataWorker:
    @staticmethod
    def convert_json_to_data():
        """
        Функция для чтения и перезаписи данных из JSON файла в переменную.
        :return: Список словарей постов.
        """
        with open('Data/posts.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def add_new_post(self, author, header, picture, text):
        """
        Функция для добавления нового поста. Фактически это перезапись старых данных
        с добавлением нового поста в уже существующий файл.
        :param author: Имя автора
        :param header: Заголовок
        :param picture: Объект, картинка.
        :param text: Текст статьи.
        """
        data = self.convert_json_to_data()
        new_id = data[-1]["id"] + 1  # Вычисление нового id поста.

        picture_filename = picture.filename
        picture_path = f"static/resources/images/posts/{picture_filename}"
        picture.save(picture_path)

        data.append({
            "id": new_id,
            "author": author,
            "header": header,
            "picture": picture_path,
            "text": text
        })

        with open('Data/posts.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)

    def find_posts_headers_with_user_text(self, user_text):
        posts = self.convert_json_to_data()
        founded_posts = []

        for post in posts:
            if user_text in post["header"]:
                founded_posts.append(post)
        return founded_posts


def do_main():
    pass


if __name__ == '__main__':
    do_main()
