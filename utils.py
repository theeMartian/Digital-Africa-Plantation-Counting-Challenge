
# Downloading Image files directly to google colab.
# Import libraries
import requests
from tqdm.auto import tqdm

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