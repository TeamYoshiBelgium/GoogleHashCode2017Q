from endpoint import EndPoint
from video import Video
from request import Request
from caching_server import CachingServer


class ReadFile:
    def __init__(self, fp):
        """Read one file to an string"""
        string = fp.read()
        fp.close()

        lines = string.splitlines()

        # Analyse the first line of the input
        lijn = lines[0].split()
        aantalVideos = int(lijn[0])
        aantalEndP = int(lijn[1])
        aantalReq = int(lijn[2])
        aantalCach = int(lijn[3])
        cachList = []  # List of caching servers
        for i in range(aantalCach):  # make caching servers
            cach = CachingServer(i, int(lijn[4]))  # lijn[int(4)] = size of the servers
            cachList.append(cach)

        # Analyse the second line of the input
        # Each element describes the size of the video
        lijn = lines[1].split()
        videoList = []  # List of videos
        for i in range(aantalVideos):
            video = Video(i, int(lijn[i]))
            videoList.append(video)

        nr = 2  # iteration variable

        # The next lines of the input contain the description of the endpoints
        epList = []  # List of endpoints
        for ep in range(aantalEndP):
            lijn = lines[
                nr].split()  # The first line contains the latency to the datacenter and the number of connected caches
            nr += 1
            datacLatency = int(lijn[0])
            epCache = int(lijn[1])
            cach = {}
            for i in range(epCache):
                lijn = lines[nr].split()  # The next i lines describe the latency from the endpoint to each cache
                nr += 1
                cach[int(lijn[0])] = int(lijn[1])
                cachList[int(lijn[0])].endpoints_count += 1
            epObject = EndPoint(i, datacLatency, cach)
            epList.append(epObject)

        # The last lines of the input contain the description of the requests.
        # Each line contains the concerning video, endpoint and number of requests.
        rqList = []  # List of requests
        for rq in range(aantalReq):
            lijn = lines[nr].split()
            nr += 1
            rqObject = Request(int(lijn[0]), int(lijn[1]), int(lijn[2]), epList[int(lijn[1])].latency)
            rqList.append(rqObject)
            videoList[rqObject.video].addRequest(rqObject)  # add the request to the video (for scoring algoritm)

        # return videoList,epList,rqList,cachList
        self.videoList = videoList
        self.epList = epList
        self.rqList = rqList
        self.cachList = cachList
