from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import math
import os



# 暂时只考虑，二维三通道的图片

""" 
# 思想：定义patch矩阵，从原图上滑过， 并获取对应位置的值。当(num + 1) * patch_size[0] > img.shape[0]时
# 停止滑动，并从下一列，重复上述操作。当满足 (num + 1) * patch_size[0] > img.shape[0] 且 
#  (num + 1) * patch_size[1] > img.shape[1]时，完成滑动。每次滑动的值都保留
"""

def patchfly(img_array, patch_size, step):
    save_path = "/mnt/4t/ljt/project/patchfly/data/patch/"
    size = 256
    assert img_array.shape >= patch_size, "The patch size must bigger than image size."
    patches_height = math.ceil(img_array.shape[0] / patch_size[0])
    patches_width = math.ceil(img_array.shape[1]/ patch_size[1])
    img_patches = np.zeros((patches_height, patches_width, 1, patch_size[0], patch_size[1], 3), dtype=np.uint8)
    
    for h in range(patches_height):
        if (h+1) != patches_height:
            for w in range(patches_width):
                if (w+1) != patches_width:
                    patch = img_array[h*patch_size[1]:(h+1)*patch_size[1], w * patch_size[0] : (w+1)*patch_size[0], :]
                    patch = patch.reshape(1, 1, 1, patch_size[0], patch_size[1], 3)
                    img_patches[h:h+1, w:w+1, :, :, :, :] = patch
                    # plt.imsave(save_path + "a{}{}.jpg".format(h, w), patch.reshape(size, size, 3))
                else:
                    patch = img_array[h*patch_size[1]:(h+1)*patch_size[1], -1 * (patch_size[0] + 1) : -1, :]
                    patch = patch.reshape(1, 1, 1, patch_size[0], patch_size[1], 3)
                    img_patches[h:h+1, w:w+1, :, :, :, :] = patch
                    # plt.imsave(save_path + "b{}{}.jpg".format(h, w), patch.reshape(size, size, 3))
        else:
            for w in range(patches_width):             
                if (w+1) != patches_width:
                    patch = img_array[-1 * (patch_size[1]+1):-1, w * patch_size[0] : (w+1)*patch_size[0], :]
                    patch = patch.reshape(1, 1, 1, patch_size[0], patch_size[1], 3)
                    img_patches[h:h+1, w:w+1, :, :, :, :] = patch
                    # plt.imsave(save_path + "c{}{}.jpg".format(h, w), patch.reshape(size, size, 3))
                else:
                    patch = img_array[-1 * (patch_size[1] + 1):-1, -1 * (patch_size[0] + 1) : -1, :]
                    patch = patch.reshape(1, 1, 1, patch_size[0], patch_size[1], 3)
                    img_patches[h:h+1, w:w+1, :, :, :, :] = patch
                    # plt.imsave(save_path + "d{}{}.jpg".format(h, w), patch.reshape(size, size, 3))
    return img_patches
