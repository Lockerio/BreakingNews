import json


class DataWorker:
    @staticmethod
    def convert_json_to_data():
        with open('posts.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def convert_data_to_json(self, author, header, picture, text):
        data = self.convert_json_to_data()
        new_id = data[-1]["id"] + 1

        picture_filename = picture.filename
        picture_path = f"static/resources/images/{picture_filename}"
        picture.save(picture_path)

        data.append({
            "id": new_id,
            "author": author,
            "header": header,
            "picture": picture_path,
            "text": text
        })

        with open('posts.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)


def do_main():
    pass


if __name__ == '__main__':
    do_main()
