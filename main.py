from genericpath import isdir, isfile
import os
from bs4 import BeautifulSoup
import requests
import time

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

# remove_incident_file('product')
# add_images('product')
ctr = 1
def get_detail_info(parent_folder):
    """
        saves detail characteristics of a product.
    """
    dirs = os.listdir(parent_folder)
    
    
    # ignoring secret dirs
    for dir in dirs:
        if '.' in dir:  
            continue
        
        # ignore files which is in parent dir
        if not (os.path.isdir(f"{parent_folder}/{dir}")):
            continue
        
        # test_url = f"https://www.ozon.ru/product/mobilnyy-telefon-texet-tm-408-krasnyy-236474939/features/"
        url = f"https://www.ozon.ru/product/{dir}/features/"
        headers = {
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
                  }
        cookies = {
                    'cookie': 'cookie: visid_incap_1101384=Qy35wsk8QW+LoLaPHm2DkeNLDmEAAAAAQUIPAAAAAAC0voE+SwVn9TjUpuVd4Gds; nlbi_1101384=6OpWSCxq6V1AXwMQyZtWRQAAAABa2edYPNa9l6f1bvImbL+E; __Secure-ab-group=19; __Secure-user-id=0; xcid=e7060b61846e9af8508248dafdf88e67; __Secure-ext_xcid=e7060b61846e9af8508248dafdf88e67; _gcl_au=1.1.2063103561.1628326888; cnt_of_orders=0; isBuyer=0; tmr_lvid=f8b40971a5890b1b85a52832106329a1; tmr_lvidTS=1628326888835; _fbp=fb.1.1628326889201.167900671; __exponea_etc__=6943a77d-d5f1-49fc-aec8-fac373b8b18d; visid_incap_2317293=c5SO1DF9T/q/2mbp/ia80tFrD2EAAAAAQUIPAAAAAAA1Jv3CiC1zlPfv6Yri0dXQ; nlbi_2317293=BEskWIMXbyn1im2dQ1ZdBQAAAACh8vTYngc+eld8/b4d09Tm; incap_ses_1339_1101384=ZHA4J3xFTFAxFWikyRWVEkHIHGEAAAAAGeJJ4aVPvQKY5vRk+ajjnA==; incap_ses_631_1101384=85svXuBOQlgx2RyanMPBCKrYHWEAAAAAYiJ0beHjcaOsgm9lqlt/vw==; _gid=GA1.2.949092585.1629565476; tmr_lvid=f8b40971a5890b1b85a52832106329a1; tmr_lvidTS=1628326888835; tmr_reqNum=313; incap_ses_584_1101384=7wWYBdRWGBp+Nh/dn8kaCKw0ImEAAAAAozUjGPcSox0Hec3tpvG5ew==; __Secure-access-token=3.0.LMKZNelrR9OtsmtEhpn1zA.19.l8cMBQAAAABhDkvkHbPLwqN3ZWKgAICQoA..20210823061915.gMQwrlzrLWi96pu-ezAIpHNDhs1BxC37mzQwSm_47Nk; __Secure-refresh-token=3.0.LMKZNelrR9OtsmtEhpn1zA.19.l8cMBQAAAABhDkvkHbPLwqN3ZWKgAICQoA..20210823061915.dzMLRtxJZnADL3u1zRQ9arQFRlrJ0FEP5ukiYR3kquA; incap_ses_379_1101384=b0rrTjJUxkfYmBwJDHtCBcMhI2EAAAAAXrma6A2z0BKUwsSjC5Co/w==; _ga_JNVTMNXQ6F=GS1.1.1629692358.22.0.1629692358.0; _ga=GA1.2.1654334305.1628326888; __exponea_time2__=0.06847333908081055; cto_bundle=j9c3pl9yRXJKbW5ZekVJSGxPSXdqTU9JWlJITHRMZTM0b2RyZkRpYjMyWXd2TU9oZ1FqOEU5UnI0SzJMY2RxWVQ0NjRWTWtMM0p2SHRKSU9sJTJGOFg1Y3hUaWxqQkRkcDBHMWhxNm50NUpzak4lMkJrQm82NyUyRldySnRCV2prTFZrTURZMDdaOTFmN0ZsYWwyU1BWN0VaTnFFSnJCb2pERDVOaUQzc2wlMkJWcjEzMkE5YTJ5cW5aZTZjNXVVUWglMkJvb3A0Wnl0R240; tmr_detect=0%7C1629692360995; RT="z=1&dm=ozon.ru&si=7b3f7d31-800f-48d5-96fb-37c883bb9ae5&ss=kso4r133&sl=0&tt=0&bcn=%2F%2F684dd307.akstat.io%2F&ul=1is2"; tmr_reqNum=321'
                  }

        # add delay
        # time.sleep(50)

        files = os.listdir(f"{parent_folder}/{dir}/")
        if not 'features.html' in files:
            time.sleep(5)
            response = requests.get(url=url, headers=headers, cookies=cookies)
            print(f'{parent_folder}/{dir}/')
            soup = BeautifulSoup(response.text, 'lxml')
            all_info = soup.select('div.da3')
            if len(all_info) != 0:
                with open(f'{parent_folder}/{dir}/features.html', 'w') as fl:
                    fl.write(response.text)

            
            print(len(all_info))
            print(response.status_code)
        global ctr
        if ctr % 15 == 0:
            print(ctr)
        ctr += 1
get_detail_info('product')
