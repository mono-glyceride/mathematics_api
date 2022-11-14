from flask import Flask, jsonify, request
import sympy as sym
from cerberus import Validator

app = Flask(__name__)

@app.route('/fib', methods=['GET'])

def return_fib_number_by_json():
  if 1 < len(dict(request.args)):
    message = {
      "params": ['too many parameters, only one parameter can be passed']
      }
    return error_status_code_400(message)

  v = Validator(get_schema())
  params = get_params()
  if not v.validate(params):
    return error_status_code_400(v.errors)

  n = int(params['n'])
  fib_number = int(calculate_fib_number(n))
  return jsonify({"result": fib_number})

def get_params():
  params = {}
  params['n'] = request.args.get('n')
  return params

def get_schema():
  schema = {
        'n': {
            'type': 'integer',
            'required': True,
            'coerce': int,
            'min': 1
        }
    }
  return schema

# 一般項を用いてn番目のフィボナッチ数を返す
def calculate_fib_number(n):
  x = sym.symbols('x', nonnegative=True, integer=True)
  nth_fib_number = 1 / sym.sqrt(5) * (((1+sym.sqrt(5))/2)**n - ((1-sym.sqrt(5))/2)**n)
  # n_th_fibonacci_numberの式のxにnを代入し簡略化
  result = sym.simplify(nth_fib_number.subs(x, n))
  return result

def error_status_code_400(message):
  return jsonify({
    "status": 400,
    "message": message
    }), 400

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
