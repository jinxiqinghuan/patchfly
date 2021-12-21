import numpy as np

"""
Idea: Similar to the idea of sub-patch, the definition is derived from the size of the matrix, 
and the slide is copied. If there is overlap, the last copy shall prevail.
"""
def unpatchfly(img_patches, img_size):
    """ Let the patches recon to the original image.

    Args:
        img_patches ([numpy array]): [The output of patchfly]
        img_size ([Tuple]): [The recon image size]
        patch_size ([Tuple]): []

    Returns:
        [type]: [description]
    """
    patch_size = [img_patches.shape[-3], img_patches.shape[-2]]
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