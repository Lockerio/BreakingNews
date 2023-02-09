import json


class AddPostDAO:
    @staticmethod
    def convert_posts_json_to_data():
        """
        Функция для чтения и перезаписи данных из JSON файла в переменную.
        :return: Список словарей постов.
        """
        with open('data/posts.json', 'r', encoding='utf-8') as file:
            posts_data = json.load(file)
        return posts_data

    @staticmethod
    def convert_profile_json_to_data():
        """
        Функция для чтения и перезаписи данных из JSON файла в переменную.
        :return: Список словарей профилей.
        """
        with open('data/profiles.json', 'r', encoding='utf-8') as file:
            profiles_data = json.load(file)
        return profiles_data

    def add_new_post(self, author_name, author_id, header, picture, text):
        """
        Функция добавления нового поста. Добавляет данные нового поста в JSON файл
        постов, добавляет id нового поста в JSON файл профилей, конкретно тому профилю,
        кто автор поста.
        :param author_id: Id автора.
        :param author_name: Имя автора.
        :param header: Заголовок
        :param picture: Объект, картинка.
        :param text: Текст статьи.
        """
        posts_data = self.convert_posts_json_to_data()
        profiles_data = self.convert_profile_json_to_data()
        new_post_id = posts_data[-1]["id"] + 1  # Вычисление id нового поста.

        self.add_post_to_posts_json(posts_data, new_post_id, author_name, author_id, header, picture, text)
        self.add_post_to_profiles_json(profiles_data, author_id, new_post_id)

    @staticmethod
    def add_post_to_posts_json(posts_data, new_id, author_name, author_id, header, picture, text):
        """
        Функция для добавления нового поста. Фактически это перезапись старых данных
        с добавлением нового поста в уже существующий файл.
        :param posts_data: Информация о всех постах.
        :param new_id: Id поста.
        :param author_id: Id автора.
        :param author_name: Имя автора.
        :param header: Заголовок
        :param picture: Объект, картинка.
        :param text: Текст статьи.
        """

        picture_filename = picture.filename
        picture_path = f"static/resources/images/posts/{picture_filename}"
        picture.save(picture_path)

        posts_data.append({
            "id": new_id,
            "author_id": author_id,
            "author": author_name,
            "header": header,
            "picture": picture_path,
            "text": text
        })

        with open('data/posts.json', 'w', encoding='utf-8') as outfile:
            json.dump(posts_data, outfile, ensure_ascii=False, indent=4)

    @staticmethod
    def add_post_to_profiles_json(profiles_data, author_id, new_post_id):
        """
        Функция для добавления id нового поста. Фактически это перезапись старых данных
        с добавлением id нового поста в уже существующий файл профилей.
        :param profiles_data: Информация о всех профилях.
        :param author_id: Id автора.
        :param new_post_id: Id нового поста.
        :return:
        """
        profiles_data[author_id]["posts"].append(new_post_id)
        with open('data/profiles.json', 'w', encoding='utf-8') as outfile:
            json.dump(profiles_data, outfile, ensure_ascii=False, indent=4)


def do_main():
    pass
    
    
if __name__ == '__main__': 
    do_main()
