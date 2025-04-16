def add_cname_record(self, options: map):
    self.method = "put"
    self.url = "/" + options['main_domain'] + "/" + options['domain'] + "/CNAME"
    self.Data = '{"zone":"' + options['main_domain'] + '","domain":"' + options['domain'] + '","ttl": 600,"type":"CNAME","answers":[{"answer":["' + '{}.cdn-ng.net.'.format(options['vhost']) + '"]}]}'

def add_cname(self, options: map):
    self.method = "put"
    self.url = "/" + options['main_domain'] + "/" + options['domain'] + "/CNAME"
    self.Data = {
        "zone": options['main_domain'],
        "domain": options['domain'],
        "type":"CNAME",
        "ttl": 600,
        "answers":[
            {"answer":[ options['value'] ]}
       ]
    }

def add_vhost_cname(self, options: map):
    self.method = "put"
    self.url = "/" + options['main_domain'] + "/" + options['domain'] + "/CNAME"
    self.Data = {
        "zone": options['main_domain'],
        "domain": options['domain'],
        "type":"CNAME",
        "ttl": 600,
        "answers":[
            {"answer":[ options['vhost'] + ".cdn-ng.net." ]}
       ]
    }

def edit_ns_record(self, options: map):
    self.method = "post"
    self.url = "/" + options['main_domain'] + "/" + options['main_domain'] + "/NS"
    self.Data = {
        "zone" : options['main_domain'],
        "domain": options['main_domain'],
        "type": "NS",
        "ttl": 600,
        "answers":[
            {"answer": ["dns1.g01.ns1global.org"]}, 
            {"answer": ["dns2.g01.ns1global.org"]}, 
            {"answer": ["dns3.g01.ns1global.org"]}, 
            {"answer": ["dns4.g01.ns1global.org"]}, 
            {"answer": ["dns1.c01.nsone.net.cn"]}, 
            {"answer": ["dns2.c01.nsone.net.cn"]}, 
            {"answer": ["dns3.c01.nsone.net.cn"]}, 
            {"answer": ["dns4.c01.nsone.net.cn"]}, 
            {"answer": ["dns5.c01.nsone.net.cn"]}
        ]
    }

def del_ns_record(self, options: map):
    self.method = "delete"
    self.url = "/" + options['main_domain'] + "/" + options['domain'] + "/NS"

def add_ns_record(self, options: map):
    self.method = "put"
    self.url = "/" + options['main_domain'] + "/" + options['main_domain'] + "/NS"
    self.Data = {
        "zone" : options['main_domain'],
        "domain": options['main_domain'],
        "type": "NS",
        "ttl": 600,
        "answers":[
            {"answer": ["dns1.g01.ns1global.org"]}, 
            {"answer": ["dns2.g01.ns1global.org"]}, 
            {"answer": ["dns3.g01.ns1global.org"]}, 
            {"answer": ["dns4.g01.ns1global.org"]}, 
            {"answer": ["dns1.c01.nsone.net.cn"]}, 
            {"answer": ["dns2.c01.nsone.net.cn"]}, 
            {"answer": ["dns3.c01.nsone.net.cn"]}, 
            {"answer": ["dns4.c01.nsone.net.cn"]}, 
            {"answer": ["dns5.c01.nsone.net.cn"]}
        ]
    }

def del_record(self, options: map):
    self.method = "delete"
    self.url = "/" + options['main_domain'] + "/" + options['domain'] + "/" + options['record_type']

def get_record(self, options: map):
    self.method = "get"
    self.url = "/" + options['main_domain'] + "/" + options['domain'] + "/" + options['record_type']

def add_record(self, options: map):
    self.method = "put"
    self.url = "/" + options['main_domain'] + "/" + options['domain'] + "/" + options['record_type']
    if options['value2'] == "":
        self.Data = {
            "zone": options['main_domain'],
            "domain": options['domain'],
            "type": options['record_type'],
            "ttl": 600,
            "answers":[
                {"answer": [ options['value'] ]}
           ]
        }
    else:
        self.Data = {
            "zone": options['main_domain'],
            "domain": options['domain'],
            "type": options['record_type'],
            "ttl": 600,
            "answers":[
                {"answer": [ options['value'] ]},
                {"answer": [ options['value2'] ]}
           ]
        }

def edit_record(self, options: map):
    self.method = "post"
    self.url = "/" + options['main_domain'] + "/" + options['domain'] + "/" + options['record_type']
    if options['value2'] == "":
        self.Data = {
            "zone": options['main_domain'],
            "domain": options['domain'],
            "type": options['record_type'],
            "ttl": 600,
            "answers":[
                {"answer": [ options['value'] ]}
           ]
        }
    else:
        self.Data = {
            "zone": options['main_domain'],
            "domain": options['domain'],
            "type": options['record_type'],
            "ttl": 600,
            "answers":[
                {"answer": [ options['value'] ]},
                {"answer": [ options['value2'] ]}
           ]
        }