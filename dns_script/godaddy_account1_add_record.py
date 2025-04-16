#!/usr/bin/python3
import json
import sys
import requests
import os
import time

domain = os.getenv('CERTBOT_DOMAIN')  # Main domain
sub_domain = "_acme-challenge"  # Subdomain for resolving
value = os.getenv('CERTBOT_VALIDATION') # resolve value

class GoDaddy:
    """ GoDaddy DNS record administration for domain """
    host = "api.godaddy.com"
    endpoint = "https://" + host + "/v1/domains"
    api_key = 'api-key'
    api_secret = 'api-secret'
    headers = {
        'Authorization': 'sso-key ' + api_key + ':' + api_secret,
        'Content-Type': 'application/json'
    }

    @staticmethod
    def add_dnsauth_record(domain: str, key: str, value: str):
        full_domain = key + '.' + domain
        print('{}: {} -> {}'.format(domain, key, value))
        data = [
            {
                "data": value,
                "name": key,
                "type": "TXT",
                "ttl": 600
            }
        ]
        resp = requests.put(
            url = GoDaddy.endpoint + "/" + domain + "/records/TXT/" + key,
            headers = GoDaddy.headers,
            data = json.dumps(data)
        )
        
        print('{}: {} -> {}'.format(domain, key, resp.text))
        time.sleep(120)

def main():
    GoDaddy.add_dnsauth_record(
        domain=domain,
        key=sub_domain,
        value=value
    )

if __name__ == "__main__":
    main()