from bokeh.document import Document

from bokeh.models import ColumnDataSource, LabelSet
from bokeh.plotting import figure
from bokeh.models.glyphs import HBar
from bokeh.server.server import Server
from bokeh.palettes import Spectral4
from tornado.ioloop import IOLoop

from . import data_holder

# fix timezone
import os
os.system("tzutil /s \"Pacific Standard Time\"")



addr = 'localhost'
port = 5006
app_name = 'seqdiag'
url = f'http://{addr}:{port}/{app_name}'


def start_server(addr, port):
    allow = [f'localhost:{port}', f'0.0.0.0:{port}', f'{addr}:{port}']
    server = Server({f'/{app_name}': modify_doc}, io_loop=IOLoop(), allow_websocket_origin=allow)
    server.start()
    server.io_loop.start()


def modify_doc(doc: Document):
    source = ColumnDataSource(data=data_holder.get_data())
        
    _keys = data_holder.get_keys()
    plot = figure(
                plot_height=600, plot_width=1200, title='Sequence Diagram',
                x_axis_type='datetime',               
                y_range=_keys,
                tools="xwheel_zoom,xpan,box_zoom,hover,reset",
                active_scroll="xwheel_zoom", 
                active_drag="xpan")

    glyph = HBar(y="who", left="t_start_ms", right="t_end_ms",
                height=0.4, fill_color="green", fill_alpha=0.5)
    plot.add_glyph(source, glyph)

    labels = LabelSet(x="t_start_ms", y="who", text="func", 
                  text_font_size="8pt",
                  source=source, text_align='left')
    plot.add_layout(labels)

    plot.hover.tooltips = [
                        ("func", "@func"),
                        ("in", "@in"),
                        ("out", "@out"),
                        # ("msg", "@msg"),
                        
                        ]

    def callback():
        #source.stream(new_data=data_holder.get_data(), rollover=1000) # todo: how to use stream
        source.data = ColumnDataSource(data=data_holder.get_data()).data
    doc.add_periodic_callback(callback, 1000)

    doc.add_root(plot)
