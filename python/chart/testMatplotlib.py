import cStringIO

from bottle import run, get, HTTPResponse
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

fig = Figure(figsize=[6,6])
ax = fig.add_axes([.1,.1,.8,.8])
ax.scatter([0.2, 0.3], [0.25, 0.35])
canvas = FigureCanvasAgg(fig)

buf = cStringIO.StringIO()
canvas.print_png(buf)
data = buf.getvalue()

headers = {
    'Content-Type': 'image/png',
    'Content-Length': len(data)
}

@get('/')
def hello():
    return HTTPResponse(body=data, headers=headers,)

run(port=8080)