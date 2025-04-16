#!/usr/bin/python3
import json
import sys
import requests
import os
import time

domain = os.getenv('CERTBOT_DOMAIN')  # Main domain
sub_domain = "_acme-challenge"  # Subdomain for resolving
value = os.getenv('CERTBOT_VALIDATION') # resolve value

class NS1:
    """ NS1 DNS record administration for domain """
    host = "api.nsone.net"
    endpoint = "https://" + host + "/v1/zones"
    secret_key = 'secret_key'
    header = {
        'X-NSONE-Key': '' + secret_key +'',
    }

    def add_dnsauth_record(host: str, key, value):
        if len(host.split('.')) == 2:
            domain = host
            host_record = ''
        else:
            host_record = host.split('.')[0]
            domain = host[host.index('.') + 1:]
        print('{}: {} -> {}'.format(domain, host_record, value))
        resp = requests.put(
            url = NS1.endpoint + "/"+ domain + "/" + key + "." + domain + "/TXT",
            headers = NS1.header,
            data = '{"zone":"' + domain + '","domain":"' + key + '.' + domain + '","type":"TXT","answers":[{"answer":["' + str(value) + '"]}]}'
        )
        time.sleep(10)
        print('{}: {} -> {}'.format(domain, host_record, json.loads(resp.text)))


def main():
    NS1.add_dnsauth_record(
        host=domain,
        key=sub_domain,
        value=value
    )

if __name__ == "__main__":
    main()