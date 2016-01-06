import socket

from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    redis.incr('hits')
    hostname = socket.gethostname()
    return 'hostname:{} count:{}'.format(hostname, redis.get('hits'))


if __name__ == "__main__":
    app.run()
