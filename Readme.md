# Patchfly
Let image patch fly.

## Introduction
The function of this library is to divide the image into patches, and then merge the patches into the original image. The division and splicing of images are mainly based on the position index of the image.

## How to use it?
```
pip install patchfly
```

### patchfly


    Args:
        img_array ([numpy array]): [The original image array]
        patch_size ([type]): [description]

    Returns:
        [Tuple]: [The target patch size.]


### unpatchfly

    Args:
        img_patches ([numpy array]): [The output of patchfly]
        img_size ([Tuple]): [The recon image size]
        patch_size ([Tuple]): []

    Returns:
        [np.array]: [recon image]
    """

## For example

```
    >>> from patchfly import patchfly
    >>> from patchfly import unpatchfly
    >>> import numpy as np
    >>> img = np.ones((3333, 3333, 3))
    >>> img.shape
    (3333, 3333, 3)
    >>> patches = patchfly(img, (256, 256, 3))
    >>> patches.shape
    (14, 14, 1, 256, 256, 3)
    >>> recon = unpatchfly(patches, img.shape)
    >>> recon.shape
    (3333, 3333, 3)
```