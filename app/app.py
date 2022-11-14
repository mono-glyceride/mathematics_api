from flask import Flask, jsonify, request
import sympy as sym

app = Flask(__name__)

@app.route('/fib', methods=['GET'])

def return_fib_number_by_json():
  param = int(request.args.get('n'))
  fib_number = int(calculate_fib_number(param))
  return jsonify({"result": fib_number})

# 一般項を用いてn番目のフィボナッチ数を返す
def calculate_fib_number(n):
  x = sym.symbols('x', nonnegative=True, integer=True)
  nth_fib_number = 1 / sym.sqrt(5) * (((1+sym.sqrt(5))/2)**n - ((1-sym.sqrt(5))/2)**n)
  # n_th_fibonacci_numberの式のxにnを代入し簡略化
  result = sym.simplify(nth_fib_number.subs(x, n))
  return result

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)
