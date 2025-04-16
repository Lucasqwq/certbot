import json

def check_domain_available(self, options: map):
    self.method = "post"
    if len(options['domains']) <= 1:
        self.Data='[ "' + '"'.join(options['domains']) + '" ]'
    else:
        self.Data='[ "' + '" ,"'.join(options['domains']) + '" ]'

    self.url = 'https://api.godaddy.com/v1/domains/available?checkType=FULL'

def __get_domain_info(self, domain):
    self.method = "get"
    self.url = 'https://api.godaddy.com/v1/domains/' + domain

def __set_var_domain_info(self, domain, tld):
    self.result = self.__get_domain_info(self, domain)

    self.info['contactAdmin'] = self.r.json()['contactAdmin']
    self.info['contactBilling'] = self.r.json()['contactBilling']
    self.info['contactRegistrant'] = self.r.json()['contactRegistrant']
    self.info['contactTech'] = self.r.json()['contactTech']
    self.info['period'] = 1
    self.info['privacy'] = False
    self.info['renewAuto'] = False
    # Variable should be used to set nameserver.
    self.info['nameServers'] = ['dns1.g01.ns1global.org, dns2.g01.ns1global.org']
    # Variable should be used to set date and IP.
    self.info['consent'] = {
        "agreedAt": "2023-03-17T00:00:00Z",
        "agreedBy": "125.227.36.99",
        "agreementKeys": [
        # Should be use `__get_agreements_key` to get key.
           "DNRA",
           self.__get_tld_agreements_key(self, tld)
        ]
    }
    # Does not meet maximum length of 41.'
    self.info['contactAdmin']['addressMailing']['address1'] =  self.info['contactAdmin']['addressMailing']['address1'][:41]
    self.info['contactBilling']['addressMailing']['address1'] =  self.info['contactBilling']['addressMailing']['address1'][:41]
    self.info['contactRegistrant']['addressMailing']['address1'] =  self.info['contactRegistrant']['addressMailing']['address1'][:41]
    self.info['contactTech']['addressMailing']['address1'] =  self.info['contactTech']['addressMailing']['address1'][:41]

def __get_tld_agreements_key(self, tld):
    self.method = "get"
    self.url = 'https://api.godaddy.com/v1/domains/agreements?privacy=false&tlds=' + tld
    self.headers['X-Market-Id'] = "en-PK"

def purchase_domain(self, options: map):
    self.method = "post"
    self.url = 'https://api.godaddy.com/v1/domains/purchase'
    # It should be confirmed whether the `info`` is not empty.
    self.__set_var_domain_info(self, options['tld'])
    self.Data.update(self.info)
    self.Data['domain'] = options['domain']
    self.Data = json.dumps(self.Data)
    
def get_domain_list(self, options: map):
    self.method = "get"
    self.url = 'https://api.godaddy.com/v1/domains'

#for i in temp_domains:
#    for j in i:
#        options['domain'] = temp_domains[i][j]
#        options['tld'] = suffixes[i]
#        req('purchase_domain', options)
