#!/usr/bin/env python
# encoding: utf-8
import logging

import requests

import config


def query_express(number: str):
    """
    查询物流信息
    :param number: 物流单号
    :return:
    """
    url = f'https://slypass3.market.alicloudapi.com/express3?number={number}'
    headers = {"Authorization": f"APPCODE {config.WL.app_code}"}
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        logging.error(res.request.url)
        logging.error(res.request.headers)
    re_res = res.json()
    re_res['number'] = number
    #return res.json()
    return re_res

def query_express2(number: str):
    """
    查询物流信息
    :param number: 物流单号
    :return:
    """
    host = 'https://wuliu.market.alicloudapi.com'
    path = '/kdi'
    method = 'GET'
    appcode = config.WL.app_code
    querys = f"no={number}"
    url = host + path + '?' + querys
    header = {"Authorization": 'APPCODE ' + appcode}
    res = requests.get(url, headers=header)
    if res.status_code != 200:
        logging.error(res.request.url)
        logging.error(res.request.headers)
    re_res = res.json()
    re_res['number'] = number
    #return res.json()
    return re_res