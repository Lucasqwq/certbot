# 簡介
API 文檔: https://cloud.tencent.com/document/api/1427/56194

API Explorer: https://console.cloud.tencent.com/api/explorer?Product=dnspod&Version=2021-03-23&Action=CreateRecord

tencentcloud-sdk-python : https://github.com/TencentCloud/tencentcloud-sdk-python

dnspod可選擇帳號:'account1,account2'

先實例化client選項 再透過寫好的function去達到想要的功能

| Script Name | 功能說明 | 備註 |
| - | - | - |
|[domain.py](./domain.py)|新增、取得、刪除域名|
|[add_record.py](./add_record.py)|新增、取得、刪除各類型record|