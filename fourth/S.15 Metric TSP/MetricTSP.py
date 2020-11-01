import sys
import math

def readInput():
    cities = []
    for line in sys.stdin.readlines():
        name, coords = line.split(",")
        lat, lon = coords.split("/")
        cities.append((name, float(lat), float(lon)))
    return cities

def buildGraph(cities):
    graph = []
    for c1 in cities:
        for c2 in cities:
            if not c1==c2:
                _,lon1,lat1 = c1
                _,lon2,lat2 = c2
                weight = haversineDistance((lon1, lat1), (lon2, lat2))
                graph.append((c1,c2, weight))
                graph.append((c1,c2, weight))
    return graph

def haversineDistance(u:float, v:float):
    lat1, lon1 = u
    lat2, lon2  = v
    pi180 = math.pi/180
    phi1 = lat1 * pi180
    phi2 = lat2 * pi180
    dPhi = (lat2-lat1) * pi180
    dLambda = (lon1-lon2) * pi180

    R = 6371e3 # metres
    a = math.sin(dPhi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dLambda/2)**2 # Haversine
    c = 2 * math.atan2(math.sqrt(a), math.sqrt((1-a)))
    d = R*c
    # print(d)
    return d

def computeMST(G):
    return None

def main():
    cities = readInput()
    graph = buildGraph(cities)
    # print(cities)
    # print(graph)

    # haversineDistance((50.0359, 5.4253), (58.3838, 3.0412))




main()