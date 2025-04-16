import sys
import requests
import json
from .records_answers import *
from .zone import *

class NS1:

    def __init__(self, ns_api_key):
        self.host = "https://api.nsone.net/v1/zones"
        self.url = ""
        self.Data = ""
        self.headers = {
            'X-NSONE-Key': ns_api_key
        }

    def req(self, func, options=None):
        eval(func + "(self, options)")
        if 'status' in options:
            if True == options['status']:
                if   "get" == self.method:
                    resp = requests.get(self.host + self.url, timeout=30, headers=self.headers)
                elif "put" == self.method:
                    resp = requests.put(self.host + self.url, timeout=30, headers=self.headers, data=json.dumps(self.Data))
                elif "post" == self.method:
                    resp = requests.post(self.host + self.url, timeout=30, headers=self.headers, data=json.dumps(self.Data))
                elif "delete" == self.method:
                    resp = requests.delete(self.host + self.url, timeout=30, headers=self.headers, data=json.dumps(self.Data))
                return resp.json()
        else:
            if  "put" == self.method:
                try:
                    r = requests.put(self.host + self.url, timeout=30, headers=self.headers, data=self.Data)
                    resp_json = json.loads(r.text)
                    if r.status_code != 200:
                        print("put 执行失败请排查原因")
                        print(resp_json)
                        sys.exit(0)
                    else:
                        print("put 执行成功")

                    return r                    
                except Exception as e:
                    raise e
            elif "post" == self.method:
                try:
                    r = requests.post(self.host + self.url, timeout=30, headers=self.headers, data=self.Data)
                    resp_json = json.loads(r.text)
                    if r.status_code != 200:
                        print("post 执行失败请排查原因")
                        print(resp_json)
                        sys.exit(0)
                    else:
                        print("post 执行成功")

                    return r                    
                except Exception as e:
                    raise e            
            elif "get" == self.method:
                try:
                    r = requests.get(self.host + self.url, timeout=30, headers=self.headers, data=self.Data)
                    resp_json = json.loads(r.text)
                    if r.status_code != 200:
                        print("get 执行失败请排查原因")
                        print(resp_json)
                        sys.exit(0)
                    else:
                        print("get 执行成功")

                    return r                    
                except Exception as e:
                    raise e            
            elif "delete" == self.method:
                try:
                    r = requests.delete(self.host + self.url, timeout=30, headers=self.headers, data=self.Data)
                    resp_json = json.loads(r.text)
                    if r.status_code != 200:
                        print("delete 执行失败请排查原因")
                        print(resp_json)
                        sys.exit(0)
                    else:
                        print("delete 执行成功")

                    return r                    
                except Exception as e:
                    raise e   