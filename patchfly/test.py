from patchify import patchify, unpatchify
from matplotlib import image as mpimg
from matplotlib import pyplot as plt
import cv2 as cv
from PIL import Image
import numpy as np
from patchfly import patchfly

# ----------------------
#  get a image from internet
# ----------------------

# url = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.petsid.us%2Fwp-content%2Fuploads%2F2018%2F07%2FCats-Health-The-Dos-And-Donts-For-Cat-owners.jpg&refer=http%3A%2F%2Fwww.petsid.us&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1642598122&t=976acf48cb6e5dc77b17048b24efdaa8"
# def request_download(IMAGE_URL):
#     import requests
#     r = requests.get(IMAGE_URL)
#     with open('./data/img.png', 'wb') as f:
#         f.write(r.content)   
# request_download(url)


# ----------------------
#  My patchfly
# ----------------------
img = Image.open(r"/mnt/4t/ljt/project/patchfly/data/img.png")
img_copy = img.copy()
img_array = np.array(img_copy)


img_patches = patchfly(img_array, (256, 256, 3), 1)
