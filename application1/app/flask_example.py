from flask import Flask, jsonify
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Counter, Histogram
from datetime import datetime
import time

app = Flask(__name__)

number_of_value_errors = Counter(
    'number_of_value_errors',
    'The number of value errors'
)

# Create a metric to track time spent and requests made.
request_time = Histogram(
    'request_processing_seconds', 
    'Time spent processing request'
)


@app.route('/delay')
@app.route('/delay/<delay_s>')
@number_of_value_errors.count_exceptions(ValueError)
@request_time.time()
def delayed_response(delay_s: int = 0):
    time1 = datetime.now()
    delay_s = int(delay_s) # throws ValueError when parsing non int literals
        
    delay_s = max(0, delay_s)
    time.sleep(delay_s)
    time2 = datetime.now()
    return jsonify({
           "Starttime" : time1,
            "Endtime":  time2
        })


# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})