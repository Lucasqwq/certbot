from .record import *
from .domain import *

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.dnspod.v20210323 import dnspod_client

class Dnspod:

    def __init__(self, secret_id, secret_key):
        self.cred = credential.Credential(secret_id, secret_key)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        self.httpProfile = HttpProfile()
        self.httpProfile.endpoint = "dnspod.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        self.clientProfile = ClientProfile()
        self.clientProfile.httpProfile = self.httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        self.client = dnspod_client.DnspodClient(self.cred, "", self.clientProfile)

    def reqs(self, func, options=None):
        result = eval(func + "(self, options)")
        return result