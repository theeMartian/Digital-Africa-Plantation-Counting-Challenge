import requests
import shutil
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
from tqdm.auto import tqdm
import csv 

# Downloading Image files directly to google colab.
# Import libraries
data_url = ''
token = {}

def zindi_data_downloader(url, token, file_name):
    # get the comptetition data
    comp_data = requests.url(url = data_url, 
                             data = token,
                             stream = True
                             )
    
    # progress bar monitor download
    pbar = tqdm(desc=file_name, total = int(comp_data.headers.get('content-length', 0)), 
                unit='B', unit_scale=True, unit_divisor=512)
    # create and write the data to colab drive in chunks
    handle = open(file_name, 'wb')
    for chunk in comp_data.iter_content(chunk_size = 512):
        if chunk:   #filter out keep-alive new chunks
            handle.write(chunk)
        pbar.update(len(chunk))
    handle.close()
    pbar.close()



# Display some images
def display_some_images(examples, labels):
    plt.figure(figsize=(10, 10))
    
    # generate 10 images
    for i in range(10):
        index = np.random.randint(0, examples.shape[0]-1)
        image = examples[index]
        label = labels[index]

        plt.subplot(5, 5, i +1)
        plt.title(str(label))
        plt.imshow(image)
    plt.show()


def order_datasets(path_to_images, path_to_csv, folder_name = ''):
    """
    Orders our images into Train and Test Folders
    """
    try:
        with open(path_to_csv, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            
            for i, row in enumerate(reader):
                
                # skip the headers
                if i == 0:
                    continue

                image_id = row[0]

                path_to_folder = os.path.join(path_to_images, folder_name)

                if not os.path.isdir(path_to_folder):
                    os.makedirs(path_to_folder)
                
                image_full_path = os.path.join(path_to_images, image_id)
                shutil.move(image_full_path, path_to_folder)

    except:
        print("[INFO] Error reading csv file")
        

