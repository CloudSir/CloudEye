'''
Author: CloudSir
@Github: https://github.com/cloudsir
Date: 2022-03-24 15:22:32
LastEditTime: 2022-03-24 18:03:03
LastEditors: CloudSir
Description: 
'''

import setuptools
from setuptools import find_packages

VERSION = '0.0.3'

setuptools.setup(
    name='cloudeye',
    version=VERSION,
    description='A simple computer vision package',
    long_description="A simple computer vision package",
    author='CloudSir',
    packages=find_packages(),
    author_email="2301029643@qq.com",
    keywords=['computer vision', 'gesture recognition'],
    install_requires=[
        'paddlex==2.0.0',
        'paddlepaddle==2.1.2'
    ],
    url="https://github.com/cloudsir/CloudEye",
    project_urls={
    "Documentation": "https://github.com/cloudsir/CloudEye",
    "Code": "https://github.com/cloudsir/CloudEye",
    "Issue tracker": "https://github.com/cloudsir/CloudEye",
    },
    package_data={
        "cloudeye": ["*/model/*"]
    }
)

