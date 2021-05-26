#! /usr/bin/env python3
#-- all rights: @fey --#
#-- py-version: 3.*  --#

'''
This open source code based on ipinfo.io's api.
'''
from termcolor import colored
import country_converter as cc
import pandas as pd
import requests as rq
import json
import sys

'''
request the ipinfo.io's api
'''
def request_api(ip):
    url = "https://ipinfo.io/" + ip
    resp = rq.get(url=url)
    res_js = json.loads(resp.text)

    return res_js

'''
Parse api's response
'''
def get_info(json):
    region    = json['region']
    city      = json['city']
    code_post = json['postal']
    country   = json['country']

    df = pd.DataFrame({'code': [country]})
    df['short name'] = df.code.apply(lambda x:
                       cc.convert(names=x, to='name_short', not_found=None))
    country = df['short name'][0]

    return (country, region, code_post, city)


'''
pretty print informations
'''
def print_infos(ip, infos):

    (country, region, code_post, city) = infos

    print(colored("[*]", "yellow"), 'IP address',
          colored(ip, "yellow"), "is located:")
    print(colored("[+]", "green"), 'country: ', colored(country, "green"))
    print(colored("[+]", "green"), 'region: ', colored(region, "green"))
    print(colored("[+]", "green"), 'postal code: ', colored(code_post, "green"))
    print(colored("[+]", "green"), 'city: ', colored(city, "green"))


if __name__ == "__main__":
    argc = len(sys.argv)
    help_ = False

    for arg in sys.argv:
        if (arg == "--help" or arg == "-h"):
            help_ = True

    if (argc != 2 or help_):
        print(colored("[-]", ("red", "cyan")[help_]),"Usage: %s <IPv4 address>" % sys.argv[0])
        exit(1)

    ip = sys.argv[1]
    json = request_api(ip)
    infos = get_info(json)

    print_infos(ip, infos)


