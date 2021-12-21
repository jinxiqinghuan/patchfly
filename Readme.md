# Patchfly
Let image patch fly.

## Introduction
The function of this library is to divide the image into patches, and then merge the patches into the original image. The division and splicing of images are mainly based on the position index of the image.

## How to use it?
'''shell
 pip install patchfly
'''

### patchfly

'''python
def patchfly(img_array, patch_size):
    """split image to patches

    Args:
        img_array ([numpy array]): [The original image array]
        patch_size ([type]): [description]

    Returns:
        [Tuple]: [The target patch size.]
    """
'''


'''python
def unpatchfly(img_patches, img_size):
    """ Let the patches recon to the original image.

    Args:
        img_patches ([numpy array]): [The output of patchfly]
        img_size ([Tuple]): [The recon image size]
        patch_size ([Tuple]): []

    Returns:
        [type]: [description]
    """
'''