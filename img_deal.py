#!usr/bin/python
# encoding:utf-8
# author:masako
# date:2018/05/23

import base64
import requests


def img_url_to_base64(url):
    """
    img url to base64 string
    :param url: img url
    :return: base64 string
    """
    try:
        response = requests.get(url, timeout=3, verify=False)
    except Exception as e:
        print e
        return ''

    img_bin = response.content
    img_b64 = base64.b64encode(img_bin)
    # print img_b64
    return img_b64


def b64_to_img_file(b64_str, path):
    """
    save base64 string to image file
    :param b64_str:
    :param path: image file's name, full path
    :return: None
    """
    img_str = base64.b64decode(b64_str)
    with open(path, 'wb') as f:
        f.write(img_str)

