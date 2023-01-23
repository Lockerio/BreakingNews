import json


class DataWorker:
    def __init__(self):
        self.data = self.convert_json_to_data()

    @staticmethod
    def convert_json_to_data():
        with open('C:/Users/Lockerio/PycharmProjects/NetWork/posts.json', 'r', encoding='utf-8') as file:
            data = json.load(file,)
        return data


def do_main():
    data = DataWorker().data
    print(data)


if __name__ == '__main__':
    do_main()
