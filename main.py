from flask import Flask
from gevent import monkey, pywsgi

app = Flask(__name__)
monkey.patch_all()


@app.route("/", methods=["GET"])
def index():
    return {"msg": "welcome chen page"}


http_server = pywsgi.WSGIServer(('0.0.0.0', 8888), app)

app.debug = False
if app.debug:
    from werkzeug.serving import run_with_reloader


    @run_with_reloader
    def run_server():
        http_server.serve_forever()
else:
    http_server.serve_forever()

#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=9999, debug=True)
