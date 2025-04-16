import json
from tencentcloud.dnspod.v20210323 import models
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

def add_domain(self, options):
    self.req = models.CreateDomainRequest()
    self.params = {
        "Domain": options['main_domain']
    }
    self.req.from_json_string(json.dumps(self.params))
    try:
        self.resp = self.client.CreateDomain(self.req)
        print(self.resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)

def get_domain(self, options):
    self.req = models.DescribeDomainRequest()
    self.params = {
        "Domain": options['main_domain']
    }
    self.req.from_json_string(json.dumps(self.params))
    try:
        self.resp = self.client.DescribeDomain(self.req)
        print(self.resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)

def del_domain(self, options):
    self.req = models.DeleteDomainRequest()
    self.params = {
        "Domain": options['main_domain']
    }
    self.req.from_json_string(json.dumps(self.params))
    try:
        self.resp = self.client.DeleteDomain(self.req)
        print(self.resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)