from flask import Blueprint, jsonify, request
import sympy as sym
from cerberus import Validator

fib = Blueprint('fib', __name__)

@fib.route('/fib')

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
