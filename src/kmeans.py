import sys

cluster = []
k = 3

class KMeansClustering:

    def __init__(self): # constructor
        self.data = data

    def ermittleExtremwert(self):

    def zentrenZufaelligSetzen(self):

    def datenpunkteZuordnen(self):

    def datenpunktZuordnen(data):
        global cluster
        minDist = sys.float_info.max
        clusterId = -1

        for i in range(k):
            d = distanz(data, cluster[i][0])  # mit mittelpunkten vergleichen
            if d < minDist:
                minDist = d
                clusterId = i

        cluster[clusterId].append(data)

    def initCluster(self):
        global cluster
        cluster = []
        for i in range(k):
            cluster.append([])  # cluster initialisieren

    def distanz(a, b):
        deltaX = a[0] - b[0]
        deltaY = a[1] - b[1]
        return pow(pow(deltaX, 2) + pow(deltaY,2), 0.5)

    def zentrenNeuBerechnen(self):

    def mittelwert(cluster):
        return