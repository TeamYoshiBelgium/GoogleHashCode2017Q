class Video:
    def __init__(self, video_id, groote):
        self.video_id = video_id
        self.groote = groote
        self.servers = []
        self.requests = []

    def __str__(self):
        string = str(self.video_id) + " groote: " + str(self.groote)
        return string

    def __repr__(self):
        return str(self.video_id)

    def addRequest(self, request):
        self.requests.append(request)

    def requestPerCache(self, cache_id, endpoints):
        # This function calculates the time that is saved when this video
        # is hosted on the cache server with id cache_id.
        # A score will be given to this video, depending on the saved time and the size of the video.
        # This score will be returned.
        delaySaved = 0
        for i in self.requests:
            if cache_id in endpoints[i.endpoint].caching_servers:
                delaySaved += i.aantal * max(i.minLatency - endpoints[i.endpoint].caching_servers[cache_id], 0)
        return delaySaved ** 2 / self.groote

    def add_caching_server(self, server, endpoints):
        # Adds the server to the list of servers that host this video.
        # If an endpoint, that request this video, is connected to the server,
        # the server is added to the caching_servers_in_use of the endpoint.
        # If the adding of this new server results in a smaller minLatency, minLatency is updated.
        self.servers.append(server)
        for i in self.requests:
            ep = endpoints[i.endpoint]
            if server.server_id in ep.caching_servers:
                ep.caching_servers_in_use.append(server)
                i.minLatency = min(i.minLatency, ep.caching_servers[server.server_id])

