#!/usr/bin/python3
import sys
sys.path.append('../..')
import packages.dns.dnspod as dnspod
from packages.tool import tool
import os
import inquirer
import configparser

domain = os.getenv('CERTBOT_DOMAIN')  # Main domain
sub_domain = "_acme-challenge"  # Subdomain for resolving
value = os.getenv('CERTBOT_VALIDATION') # resolve value

with open('/data/script/tool/certbot/dns_script/dnspod_record_id.txt', 'r') as f:
    record_id = f.read().strip()
with open('/data/script/tool/certbot/dns_script/dnspod_record_id.txt', 'w') as f:
    f.write('')

dnspod_config = configparser.ConfigParser()

dnspod_config.read(os.path.join('../../config/dns', 'dnspod.ini'))

DNSPOD_SECRET_ID = dnspod_config.get("account1","secret_id")
DNSPOD_SECRET_KEY = dnspod_config.get("account1","secret_key")

dnspod = dnspod.Dnspod(DNSPOD_SECRET_ID,DNSPOD_SECRET_KEY)

config = {  'domain': domain,
            'record_id': int(record_id),
         }

for dn in domain.split('\n'):
    if dn == "":
        continue

    config['domain'] = dn
    config['main_domain'] = tool.check_domain(dn)[0]
    print("Current configure domain: " + config['main_domain'])

    result = dnspod.reqs("del_record", config)