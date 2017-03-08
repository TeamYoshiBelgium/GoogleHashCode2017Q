import os
import time
import math
from read import ReadFile
from tqdm import tqdm
from write import WriteFile
import argparse


def main():
    parser = argparse.ArgumentParser(description='Process an map to an route.')
    parser.add_argument('-f', '--filename', type=argparse.FileType('r'),
                        required=True, dest="file", help="Path to the input map file")

    args = parser.parse_args()
    filename = os.path.splitext(args.file.name)[0].split("/")[-1]
    read = ReadFile(args.file)

    # Read the input
    videos = read.videoList
    endpoints = read.epList
    requests = read.rqList
    servers = read.cachList

    start = time.time()

    # Solution
    # Sort server that are most connected with endpoints
    servers.sort(key=lambda x: x.endpoints_count, reverse=True)

    # Fill all the servers
    for server in tqdm(servers):
        server.update_videos(videos, endpoints)
        server.vullen(endpoints)
    stop = time.time()
    print("===========================================")
    print("| Time needed: %s ms" % ((stop - start) * 1000))
    # print(str(servers))

    WriteFile(filename, servers)
    calculateScore(requests, endpoints, filename)
    print("Problem solved!")


def calculateScore(requests, endpoints, filename):
    score = 0
    totalReqs = 0
    for r in requests:
        ep = endpoints[r.endpoint]
        score += r.aantal * (ep.latency - r.minLatency) * 1000
        totalReqs += r.aantal

    totalScore = math.floor(score / totalReqs)
    print("| Total Score:" + str(totalScore) + " - File: " + filename)
    print("===========================================")


if __name__ == "__main__":
    main()
