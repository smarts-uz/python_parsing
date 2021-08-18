from genericpath import isdir, isfile
import os
from bs4 import BeautifulSoup
import requests

def remove_incident_file(parent_folder):
    """
        removes all incident id errors, 
        structure of this parent folder should be parent_folder/folders/pages
    """
    dirs = os.listdir(parent_folder)
    for dir in dirs:
        if '.' in dir:  # ignoring secret dirs
            continue

        # ignore files which is in parent dir
        if not (os.path.isdir(f"{parent_folder}/{dir}")):
            continue
        
        files = os.listdir(f'{parent_folder}/{dir}')
        for file in files:
            
            # if inside of folder there is another folder ignore that folder
            if not(os.path.isfile(f"{parent_folder}/{dir}/{file}")):
                continue
            with open(f"{parent_folder}/{dir}/{file}", 'r') as f:
                try:
                    content = f.read()
                    if ('Incapsula' in content):
                        os.remove(f"{parent_folder}/{dir}/{file}")
                except UnicodeDecodeError:
                    # remove not relevant file
                    os.remove(f"{parent_folder}/{dir}/{file}")


def get_file_content(path):
    with open(path, 'r') as fl:
        content = fl.read()
        if (len(content) < 5):
            return None
        return content




def get_image_url(product_path):
    html = get_file_content(path=product_path)
    try:
        soup = BeautifulSoup(html, 'lxml')
        image_div = soup.select_one('div.e0u1')
        image_url = image_div.select_one('div.e9r7 img[src]')['src']
        return image_url
    except:
        print(html, '\n\n', product_path)


def download_image(url, path_to_store, image_name):
    """
        downloads image according to given url and stores it into given path with the name of image.png
    """
    response = requests.get(url)

    file = open(f"{path_to_store}/{image_name}.png", "wb")
    file.write(response.content)
    file.close()


def get_thumbnail_urls(product_path):
    html = get_file_content(path=product_path)
    soup = BeautifulSoup(html, 'lxml')
    thumbnails = soup.select('div.e9q6 img._3Ugp')
    thumbnail_urls = [t['src'] for t in thumbnails]
    return thumbnail_urls



def add_image_to_product(product_path, product_folder):
    """
        it stores images and thumbnails according to given product
    """
    image_url = get_image_url(product_path=product_path)
    image_folder = f'{product_folder}/image'
    thumbnail_urls = get_thumbnail_urls(product_path=product_path)
    thumbnail_folder = f'{product_folder}/thumbnails'
    # make a directory to store the image
    try: 
        os.mkdir(image_folder) 
        os.mkdir(thumbnail_folder)

        download_image(url=image_url, path_to_store=image_folder, image_name='image')

    # download thumbnail images and save it
        if (len(thumbnail_urls) > 0):
            ctr = 1
            for thumbnail_url in thumbnail_urls:
                url = thumbnail_url.replace('c50', 'c1000')
                download_image(url=url, path_to_store=thumbnail_folder, image_name=f'thumbnail{ctr}')
                ctr += 1

    except OSError as error: 
        print(error)  
    
    # download a product image and save it
    


# add_image_to_product(product_path='product/mobilnyy-telefon-vertex-k213-chernyy-serebristyy-199643880/@asb=BCRBR5_25252FCrku5mPfrucePsyqOfn4Uvu2HFq2QcQvVDJU_25253D&asb2=gdfsE5Sz90hB7s3vXLH1veU_ekwB3MNn8aK1sJS1-qk', 
#                     product_folder='product/mobilnyy-telefon-vertex-k213-chernyy-serebristyy-199643880'
#                     )

def add_images(parent_folder):
    """
        adds images and thumbnails to a certain product
        structure of this parent folder should be parent_folder/folders/pages
    """
    dirs = os.listdir(parent_folder)
    
    # ignoring secret dirs
    for dir in dirs:
        if '.' in dir:  
            continue
        
        # ignore files which is in parent dir
        if not (os.path.isdir(f"{parent_folder}/{dir}")):
            continue

        files = os.listdir(f'{parent_folder}/{dir}')
        for file in files:
            
            # if inside of folder there is another folder ignore that folder
            if not(os.path.isfile(f"{parent_folder}/{dir}/{file}")):
                continue
            
            add_image_to_product(product_path=f"{parent_folder}/{dir}/{file}", 
                                product_folder=f'{parent_folder}/{dir}'
                                )

remove_incident_file('product')
add_images('product')

