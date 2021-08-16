from bs4 import BeautifulSoup

def ozon_product_info(file_path):
    with open(file_path, 'r') as fl:
        file_content = fl.read()
    soup = BeautifulSoup(file_content, 'lxml')
    char_info = soup.select_one('div.da3')
    rows = char_info.select('dl.db8')
    data = []
    for row in rows:
        pairs = {}
        attr = row.find('span').text
        char = row.find('dd').text 
        pairs['attr'] = attr
        pairs['char'] = char
        data.append(pairs)
    return data
print(ozon_product_info('ozon.html'))