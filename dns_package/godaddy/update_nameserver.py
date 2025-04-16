def update_nameserver(self, options: map):
    self.method="patch"
    self.url = options['main_domain']
    self.Data = {
        "nameServers" : [
            options['name_servers'][0], 
            options['name_servers'][1]
        ]
    }

def set_to_ns1_nameserver(self, options: map):
    self.method="patch"
    self.url = options['main_domain']
    self.Data = {
        "nameServers" : [
            "dns1.g01.ns1global.org",
            "dns2.g01.ns1global.org", 
            "dns3.g01.ns1global.org",
            "dns4.g01.ns1global.org",
            "dns1.c01.nsone.net.cn",
            "dns2.c01.nsone.net.cn",
            "dns3.c01.nsone.net.cn",
            "dns4.c01.nsone.net.cn",
            "dns5.c01.nsone.net.cn"
        ]
    }

def set_to_dnspod_nameserver(self, options: map):
    self.method="patch"
    self.url = options['main_domain']
    self.Data = {
        "nameServers" : [
            "raincoat.dnspod.net",
            "generous.dnspod.net", 
        ]
    }