import time

import requests
import torch

url = 'http://localhost:12023/predict'

start = time.time()
post_response = requests.post(url, json={'images': torch.rand(1, 3, 32, 32).tolist()})
post_response.raise_for_status()
print(f'POST response [{time.time()-start}]:', post_response.json())

with open('image_example.png', 'rb') as f:
    start = time.time()
    post_image_response = requests.post(url, files={'image': f})
    post_image_response.raise_for_status()
    print(f'POST image response [{time.time()-start}]:', post_image_response.json())
