class CachingServer:
    def __init__(self, server_id, max_size):
        self.server_id = server_id
        self.max_size = max_size
        self.endpoints_count = 0
        self.videos_server = []
        self.lijst = []
        self.size_gebruikt = 0

    def __str__(self):
        string = str(self.server_id) + " " + str(self.max_size)
        for i in self.videos_server:
            string += "\n" + str(i)
        return string

    def __repr__(self):
        return str(self.server_id)

    def update_videos(self, videos, endpoints):
        # This function makes a list of all posible videos that this server can host.
        # This list is sorted, so the videos with the highest score will be put in position 0.
        self.lijst = []
        for video in videos:
            score_berekend = video.requestPerCache(self.server_id, endpoints)
            if score_berekend == 0:
                continue
            self.lijst.append((video, score_berekend))
        self.lijst.sort(key=lambda x: x[1], reverse=True)

    def vullen(self, endpoints):
        # This function fills the server with the videos that received the highest score.
        i = 0
        while True:
            if i >= len(self.lijst):
                break
            video = self.lijst[i][0]
            if self.size_gebruikt + video.groote > self.max_size:
                i += 1
                continue
            self.videos_server.append(video)
            video.add_caching_server(self, endpoints)
            self.size_gebruikt += video.groote
            i += 1
