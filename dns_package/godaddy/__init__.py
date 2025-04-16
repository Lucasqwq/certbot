import sys
import requests
import json
from .domain import *
from .update_nameserver import *

class Godaddy:

    def __init__(self, key1):
        self.host = "https://api.godaddy.com/v1/domains/"
        self.url = ""
        self.Data = ""
        self.headers = {
            'Authorization': key1,
            'Content-Type': 'application/json',
            'X-Shopper-Id': 'Shopper-Id'
        }
        self.info = {}

    def req(self, func, options:map=None):
        eval(func + "(self, options)")
        if   "patch" == self.method:
            try:
                resp = requests.patch(self.host + self.url, timeout=30, headers=self.headers, data=json.dumps(self.Data))
                if resp.status_code != 204:
                    print(resp)
                    print("patch 执行失败请排查原因")
                    #sys.exit(0)
                else:
                    print("patch 执行成功")
            except json.decoder.JSONDecodeError as e:
                print("JSON 解析错误：", str(e))
            except Exception as e:
                raise e
        elif "get" == self.method:
            resp = requests.get(url=self.url, headers=self.headers)
        elif "post" == self.method:
            resp = requests.post(url=self.url, headers=self.headers, data=self.Data)

        if resp.text == "":
            return 
        else: 
            return resp.json()
