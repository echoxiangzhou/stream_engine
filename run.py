# from engine import main
# main.app.run(debug=True)

# from gevent.wsgi import WSGIServer
# from engine import main
#
# http_server = WSGIServer(('', 5000), main.app)
# http_server.serve_forever()

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import tornado.log
from engine import routes
import logging


def main():

    tornado.log.enable_pretty_logging()
    server = HTTPServer(WSGIContainer(routes.app))
    server.bind(5000)
    server.start(0)
    logging.getLogger('tornado.application').setLevel(logging.DEBUG)
    IOLoop.current().start()

if __name__ == '__main__':
    main()
