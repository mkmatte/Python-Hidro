import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y,title,ylabel):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6,4))
    plt.title(title)
    plt.plot(x, y, 'go--')
    plt.xticks(rotation=70)
    plt.xlabel('Período')
    plt.ylabel(ylabel)
    text = "Última Leitura: " + str(int(y[0])) + ' - Data: ' + str(x[0])
    _x = min(x)
    _y = max(y)
    plt.text(_x, _y, text, size=8, color='red')   
    #plt.gca().invert_yaxis()
    plt.tight_layout()
    graph = get_graph()
    return graph
