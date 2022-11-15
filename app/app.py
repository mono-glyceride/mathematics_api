from flask import Flask, jsonify
import sympy as sym
import os
from dotenv import load_dotenv
load_dotenv()

# 開発環境、テスト、本番環境でfibを読み込むのに必要な記述が異なるため
if os.environ['ENV'] == 'development':
  from route.fib import fib
else:
  from app.route.fib import fib
app = Flask(__name__)

app.register_blueprint(fib)

@app.errorhandler(404)
def error_404(error):
  return set_error(404,'Not found. The requested resource does not exist.')

@app.errorhandler(405)
def error_405(error):
  return set_error(405,'The method is not allowed for the requested URL.')

@app.errorhandler(406)
def error_406(error):
  return set_error(406,'This service does not support the format requested in the Accept header.')

@app.errorhandler(409)
def error_409(error):
  return set_error(409,'Request cannot be completed because it conflicts with current resources.')

@app.errorhandler(410)
def error_410(error):
  return set_error(410,'The requested resource is no longer available at the server.')

@app.errorhandler(411)
def error_411(error):
  return set_error(411,'Content-Length header is required for requests.')

@app.errorhandler(413)
def error_413(error):
  return set_error(413,'Request size exceeds limit.')

@app.errorhandler(415)
def error_415(error):
  return set_error(415,'The content type of the request is in a format not supported by the service.')

@app.errorhandler(416)
def error_416(error):
  return set_error(416,'Requested range not satisfiable.')

@app.errorhandler(422)
def error_422(error):
  return set_error(422,'Unprocessable entity.')

@app.errorhandler(423)
def error_423(error):
  return set_error(423,'Locked.')

@app.errorhandler(429)
def error_429(error):
  return set_error(429,'The requested resource does not exist.')

@app.errorhandler(500)
def error_500(error):
  return set_error(500,'An error occurred on the server when processing the URL.')

@app.errorhandler(503)
def error_503(error):
  return set_error(503,'Service is temporarily unavailable due to maintenance or overload.')

@app.errorhandler(504)
def error_504(error):
  return set_error(504,'The gateway did not receive a response within the specified time period.')

def set_error(status, message):
  return jsonify({
  'status': status,
  'message': message
  }), status

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)
