from src import kmeans

def setup():
    kmeans = KMeansClustering(data, 4)
    GUI.erzeugeGUI()
    GUI.zeichne(kmeans)

def kGewaehlt():
    kmeans = KMeansClustering(data, int(GUI.kWaehler.value()))
    GUI.zeichne(kmeans)

def zentrenNeuBerechnen():
    kmeans.zentrenNeuBerechnen()

def datenpunkteZuordnen():
    kmeans.datenpunkteZuordnen()

def schritt():
    kMeans.datenpunkteZuordnen()
    kmeans.zentrenNeuBerechnen()

def zentrenZufaelligSetzen():
    kmeans.zentrenZufaelligSetzen()
    kmeans.datenpunkteZuordnen()

def mouseReleased():
    GUI.zeichne(kmeans)