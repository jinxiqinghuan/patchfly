from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import math
import os



# ----------------------
#  思想：和分patch的思想类似，定义源于大小的矩阵，滑动进行复制
#  如果重合的地方以最后复制为准
# ----------------------

def unpatchfly(img_patches, img_size, patch_size):
    recon_img = np.zeros(img_size, dtype=np.uint8)
    for h in range(img_patches.shape[0]):
        if (h+1) != img_patches.shape[0]:
            for w in range(img_patches.shape[1]):
                if (w+1) != img_patches.shape[1]:
                    recon_img[h*patch_size[1]:(h+1)*patch_size[1], w * patch_size[0] : (w+1)*patch_size[0], :] = img_patches[h][w][0]
                else:
                    recon_img[h*patch_size[1]:(h+1)*patch_size[1], -1 * (patch_size[0] + 1) : -1, :] = img_patches[h][w][0]
        else:
            for w in range(img_patches.shape[1]):             
                if (w+1) != img_patches.shape[1]:
                    recon_img[-1 * (patch_size[1]+1):-1, w * patch_size[0] : (w+1)*patch_size[0], :] = img_patches[h][w][0]
                else:
                    recon_img[-1 * (patch_size[1] + 1):-1, -1 * (patch_size[0] + 1) : -1, :] = img_patches[h][w][0]
            
    return recon_img