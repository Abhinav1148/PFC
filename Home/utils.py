import matplotlib.pyplot as plt
import base64
from io import BytesIO
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek (0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
def get_plot1(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6,5))
    plt.title('bmi variation')
    plt.plot(x,y)
    plt.xticks (rotation=45)
    plt.xlabel('date')
    plt.ylabel('bmi')
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot2(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6,5))
    plt.title('weight variation')
    plt.plot(x,y)
    plt.xticks (rotation=45)
    plt.xlabel('date')
    plt.ylabel('weight')
    plt.tight_layout()
    graph = get_graph()
    return graph