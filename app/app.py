from flask import Flask, jsonify, request
import sympy as sym
from cerberus import Validator

app = Flask(__name__)

@app.route('/fib', methods=['GET'])

def return_fib_number_by_json():
  if 1 < len(dict(request.args)):
    return jsonify({
      "status": 400,
      "message": {
        "params": 'Too many parameters, only one parameter can be passed'
      }
      }), 400
  v = Validator(get_schema())
  params = get_params()
  if v.validate(params):
    n = int(params['n'])
    fib_number = int(calculate_fib_number(n))
    return jsonify({"result": fib_number})
  else:
    return jsonify({
      "status": 400,
      "message": v.errors
      }), 400

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

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)
