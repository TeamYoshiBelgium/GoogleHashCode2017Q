class Request:
    def __init__(self, video, endpoint, aantal, latency):
        self.video = video
        self.endpoint = endpoint
        self.aantal = aantal
        self.minLatency = latency
        self.saved = 0

    def __str__(self):
        string = str(self.video) + " x " + str(self.aantal) + " ->" + str(self.endpoint)
        return string

    def latencySaved(self):
        # Saved latency = self.saved, self.latency = real latency
        # dataLatency = latency (endpoint -> datacenter)
        data_latency = self.endpoint.latency
        self.saved = self.aantal * (data_latency - self.latency)

    def __repr__(self):
        return str(self.video)