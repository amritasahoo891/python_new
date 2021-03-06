from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis')
#redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    # count = redis.incr('hits')
    return 'Hello World! Im running in a docker Container - Version 0.0.2 redis'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
