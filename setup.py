import setuptools


setuptools.setup(
    name="patchfly", 
    version="0.0.5", 
    author="ljt", 
    author_email="1196680037@qq.com",
    description="Let image patch fly.", 
    long_description='Divide the image into patches according to the specified size and restore it to the original image.',
    long_description_content_type="text/markdown",
    url="https://gitee.com/lijitao/patchfly.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7', 
)