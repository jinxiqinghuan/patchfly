import numpy as np
import math

""" 
# Thought: Define the patch matrix, slide over the original image, 
# and get the value of the corresponding position. 
# Stop sliding when (num + 1) * patch_size[0]> img.shape[0], 
# and repeat the above operation from the next column. 
# When (num + 1) * patch_size[0]> img.shape[0] and 
# (num + 1) * patch_size[1]> img.shape[1] are satisfied, 
# the sliding is completed. The value of each swipe is retained
"""

def patchfly(img_array, patch_size):
    """split image to patches

    Args:
        img_array ([numpy array]): [The original image array]
        patch_size ([type]): [description]

    Returns:
        [Tuple]: [The target patch size.]
    """
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
                else:
                    patch = img_array[h*patch_size[1]:(h+1)*patch_size[1], -1 * (patch_size[0] + 1) : -1, :]
                    patch = patch.reshape(1, 1, 1, patch_size[0], patch_size[1], 3)
                    img_patches[h:h+1, w:w+1, :, :, :, :] = patch
        else:
            for w in range(patches_width):             
                if (w+1) != patches_width:
                    patch = img_array[-1 * (patch_size[1]+1):-1, w * patch_size[0] : (w+1)*patch_size[0], :]
                    patch = patch.reshape(1, 1, 1, patch_size[0], patch_size[1], 3)
                    img_patches[h:h+1, w:w+1, :, :, :, :] = patch
                else:
                    patch = img_array[-1 * (patch_size[1] + 1):-1, -1 * (patch_size[0] + 1) : -1, :]
                    patch = patch.reshape(1, 1, 1, patch_size[0], patch_size[1], 3)
                    img_patches[h:h+1, w:w+1, :, :, :, :] = patch
    return img_patches
