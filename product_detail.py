from bs4 import BeautifulSoup
import os, json

# list all product directories
def get_product_chars(parent_folder):
    """
        gets all characteristics of a product and stores them into features.json file
    """

    products = os.listdir(parent_folder)

    # ignoring secret dirs
    for product in products:
        if '.' in product:  
            continue
        
        # ignore files which is in product dir
        if not (os.path.isdir(f"{parent_folder}/{product}")):
            continue
        
        product_files = os.listdir(f"{parent_folder}/{product}")

        # ignore product which does not have features.html
        if not 'features.html' in product_files:
            continue
        
        
        with open(f'{parent_folder}/{product}/features.html', 'r') as fl:
            content = fl.read()
            soup = BeautifulSoup(content, 'lxml')
            try:
                all_info = soup.select('div.da3')[1:]
                titles = soup.select('div.da3>div.da5')
                data = []
                for i in range(len(all_info)):
                    child_data = dict()
                    attrs = [attr.text for attr in all_info[i].select('span.db6')]
                    chars = [char.text for char in all_info[i].select('dd.db5')]
                    child_data['title'] = titles[i].text
                    child_data['data'] = dict(zip(attrs, chars))
                    data.append(child_data)
                with open(f'{parent_folder}/{product}/features.json', 'w') as fl:
                    json.dump(data, fl, indent=4, ensure_ascii=False)

            except:
                print(f"{parent_folder}/{product} does not have information about its characteristics.")
            
get_product_chars('product')