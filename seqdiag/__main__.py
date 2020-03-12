from threading import Thread
from . import data_renderer
from . import flask_app

def main():
       t_bokeh = Thread(target=data_renderer.start_server,
              args=(flask_app.addr, flask_app.port))
       t_bokeh.daemon =True
       t_bokeh.start()

       flask_app.app.run(flask_app.addr, flask_app.port)

if __name__ == '__main__':
       main()