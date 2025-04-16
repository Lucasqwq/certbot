import json
from tencentcloud.dnspod.v20210323 import dnspod_client, models
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

def add_cname_record(self, options):
    self.req = models.CreateRecordRequest()
    self.params = {
        "Domain": options['main_domain'],
        "SubDomain": options['two_level_domain'],
        "RecordType": "CNAME",
        "RecordLine": "默认",
        "Value": options['value']
    }
    self.req.from_json_string(json.dumps(self.params))
    try:
        self.resp = self.client.CreateRecord(self.req)
        print(self.resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)

def add_a_record(self, options):
    self.req = models.CreateRecordRequest()
    self.params = {
        "Domain": options['main_domain'],
        "SubDomain": options['two_level_domain'],
        "RecordType": "A",
        "RecordLine": "默认",
        "Value": options['value']
    }
    self.req.from_json_string(json.dumps(self.params))
    try:
        self.resp = self.client.CreateRecord(self.req)
        print(self.resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)

def add_record(self, options):
    self.req = models.CreateRecordRequest()
    self.params = {
        "Domain": options['main_domain'],
        "SubDomain": options['two_level_domain'],
        "RecordType": options['record_type'],
        "RecordLine": "默认",
        "Value": options['value']
    }
    self.req.from_json_string(json.dumps(self.params))
    try:
        self.resp = self.client.CreateRecord(self.req)
        print(self.resp.to_json_string())
        return self.resp
    except TencentCloudSDKException as err:
        print(err)

def get_record(self, options):
    self.req = models.DescribeRecordListRequest()
    self.params = {
        "Domain": options['main_domain'],
        "SubDomain": options['two_level_domain'],
        "RecordType": options['record_type'],
        "RecordLine": "默认"
    }
    self.req.from_json_string(json.dumps(self.params))
    try:
        self.resp = self.client.DescribeRecordList(self.req)
        print(self.resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)

def del_record(self, options):
    self.req = models.DeleteRecordRequest()
    self.params = {
        "Domain": options['main_domain'],
        "RecordLine": "默认",
        "RecordId": options['record_id']
    }
    self.req.from_json_string(json.dumps(self.params))
    try:
        self.resp = self.client.DeleteRecord(self.req)
        print(self.resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)