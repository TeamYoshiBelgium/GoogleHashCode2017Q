class EndPoint:
    def __init__(self, endpoint_id, latency, caching_servers):
        self.endpoint_id = endpoint_id
        self.latency = latency
        self.caching_servers = caching_servers
        self.caching_servers_in_use = []

    def __str__(self):
        string = str(self.endpoint_id) + " " + str(self.latency)
        for key, val in self.caching_servers.items():
            string += "\n " + str(key) + " " + str(val)
        return string

    def __repr__(self):
        return self.endpoint_id
