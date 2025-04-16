#!/usr/bin/python3
import sys
sys.path.append('../..')
import packages.dns.dnspod as dnspod
from packages.tool import tool
import os
import inquirer
import configparser
import time
import json

domain = os.getenv('CERTBOT_DOMAIN')  # Main domain
sub_domain = "_acme-challenge"  # Subdomain for resolving
value = os.getenv('CERTBOT_VALIDATION') # resolve value

dnspod_config = configparser.ConfigParser()

dnspod_config.read(os.path.join('../../config/dns', 'dnspod.ini'))

DNSPOD_SECRET_ID = dnspod_config.get("account1","secret_id")
DNSPOD_SECRET_KEY = dnspod_config.get("account1","secret_key")

dnspod = dnspod.Dnspod(DNSPOD_SECRET_ID,DNSPOD_SECRET_KEY)

config = {  'main_domain': domain,
            'two_level_domain': sub_domain,
            'value': value,
            'record_type': "TXT"
         }

def main():
    result = dnspod.reqs("add_record", config)
    result1 = str(result)
    data = json.loads(result1)
    with open('/data/script/tool/certbot/dns_script/dnspod_record_id.txt', 'w') as f:
        f.write(str(data['RecordId']))

    

if __name__ == "__main__":
    main()
    time.sleep(10)