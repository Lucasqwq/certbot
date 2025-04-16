#!/usr/bin/python3
import json
import sys
import requests
import os
import time
import inquirer

#domain = os.getenv('CERTBOT_DOMAIN')  # Main domain
domain = "domain"
sub_domain = "_acme-challenge"  # subdomain for resolving


class GoDaddy:
    """ GoDaddy DNS record administration for domain """
    host = "api.godaddy.com"
    endpoint = "https://" + host + "/v1/domains"
    api_key = 'api_key'
    api_secret = 'api_secret'
    headers = {
        'Authorization': 'sso-key ' + api_key + ':' + api_secret,
        'Content-Type': 'application/json'
    }

    @staticmethod
    def del_domain_record():

        data = [
            {
               "domain": domain,
               "type": "TXT",
               "name": sub_domain
            }
        ]
        
        resp = requests.delete(
            url = GoDaddy.endpoint + "/" + domain + "/records" + "/" + "TXT" + "/" + sub_domain ,
            headers = GoDaddy.headers,
            data = json.dumps(data),
        )
        print(resp.text)

def main():
    GoDaddy.del_domain_record()

if __name__ == "__main__":
    main()