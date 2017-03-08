class WriteFile:
    def __init__(self, filename, servers_in):
        servers = []
        for server in servers_in:
            if len(server.videos_server) > 0:
                servers.append(server)
        f = open("tests/output/" + filename + ".out", "w")

        f.write(str(len(servers)) + "\n")
        for server in servers:
            f.write(str(server.server_id))
            for video in server.videos_server:
                f.write(" " + str(video.video_id))
            f.write("\n")
        f.close()
