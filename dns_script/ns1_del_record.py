#!/usr/bin/python3
import sys
sys.path.append('../..')
import packages.dns.ns1 as ns1
from packages.tool import tool
import os
import inquirer
import configparser

domain = os.getenv('CERTBOT_DOMAIN')  # Main domain
sub_domain = "_acme-challenge."  # Subdomain for resolving
value = os.getenv('CERTBOT_VALIDATION') # resolve value

ns1_config = configparser.ConfigParser()

ns1_config.read(os.path.join('../../config/dns', 'ns1.ini'))

NS1_API_KEY = ns1_config.get("ns1","api_key")

ns1 = ns1.NS1(NS1_API_KEY)

config = {  'domain': '',
            'status': True,
            'record_type': 'TXT'
         }

for dn in domain.split('\n'):
    if dn == "":
        continue

    config['domain'] = sub_domain + dn
    config['main_domain'] = tool.check_domain(dn)[0]
    print("Current configure domain： " + config['domain'])

    result = ns1.req("del_record", config)
    print(result)
