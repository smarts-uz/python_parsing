import requests

from bs4 import BeautifulSoup


class YandexMarketProductDetail:

    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def fetch(self):
        with open(self.file_path, 'r') as fl:
            html = fl.read()
        return html
    
    def parse(self):
        html = self.fetch()
        soup = BeautifulSoup(html, 'lxml')
        description = soup.select_one('div._1uLae').text
        divisions = soup.select('div.la3zd')
        data = {}
        dic_list = []
        for division in divisions:
            title = division.find('h2').text
            keys_object = division.find_all('span')
            values_object = division.find_all('dd')
            # removing empty text element
            keys = [key.text for key in keys_object if key.text != '']
            values = [value.text for value in values_object if value.text != '']
            dt = {}
            for i in range(len(keys)):
                dt[keys[i]] = values[i]
            dic = {
                "title": title,
                "data": [dt]
            }
            dic_list.append(dic)
        data["description"] = description
        data["data"] = dic_list
        with open(f"{self.file_path.split('.')[0]}_data.txt", 'w') as fl:
            fl.write(str(data))

obj = YandexMarketProductDetail(file_path='yandex_a50_detail.html')
obj.parse()