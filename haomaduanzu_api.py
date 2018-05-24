#!usr/bin/python
# encoding:utf-8
# author:masako
# date:2018/05/24

import requests


def login(username, password):
    url = "http://api.jmyzm.com/http.do?action=loginIn&uid=%s&pwd=%s" % (username, password)
    result = {}
    try:
        response = requests.get(url)
    except Exception as e:
        result['msg'] = str(e)
        return result

    info = response.content
    if username in info:
        try:
            name, token = info.split('|')
        except Exception as e:
            result['msg'] = str(e)
            return result

        result['name'] = name
        result['token'] = token
        return result

    result['msg'] = info
    return result


def get_phone(pid, username, token, size=1):
    url = "http://api.jmyzm.com/http.do?action=getMobilenum&pid=%s&uid=%s&token=%s&mobile=&size=%s" \
          % (pid, username, token, size)
    result = {}
    try:
        response = requests.get(url)
    except Exception as e:
        result['msg'] = str(e)
        return result

    r = response.content

    if token in r:
        try:
            phone_number, token = r.split('|')
        except Exception as e:
            result['msg'] = str(e)
            return result

        phone_list = phone_number.split(';')

        result['phone'] = phone_list
        result['token'] = token
        return result

    result['msg'] = r
    return result


def get_code(username, token, phone):
    url = "http://api.jmyzm.com/http.do?action=getVcodeAndReleaseMobile&uid=%s&token=%s&mobile=%s" \
          % (username, token, phone)
    result = {}
    try:
        response = requests.get(url)
    except Exception as e:
        result['msg'] = str(e)
        return result

    print response.content




if __name__ == "__main__":
    # print login("asdqwer", "123")
    token = "54f78da204cc3c7825287c7be1bcf017"
    print get_phone(693, 'asdpwd123', token)
    get_code()
