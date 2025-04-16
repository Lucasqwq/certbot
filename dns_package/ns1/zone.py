def get_zone_list(self, options: map):
    self.method = "get"
    self.url = ""
    self.Data = ""

def del_zone(self, options: map):
    self.method = "delete"
    self.url = "/" + options['main_domain']
    self.Data = ""

def add_zone(self, options: map):
    self.method = "put"
    self.url = "/" + options['main_domain']
    self.Data = {
        "zone": options['main_domain'],
        "nx_ttl": 600,
        "networks": [0,5],
    }

def get_a_zone(self, options: map):
    self.method = "get"
    self.url = "/" + options['main_domain']