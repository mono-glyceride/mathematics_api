from flask import Flask, jsonify

from route.fib import fib
app = Flask(__name__)

app.register_blueprint(fib)

@app.errorhandler(404)
def error_404(error):
  return set_error(404,'Not found. The requested resource does not exist.')

@app.errorhandler(405)
def error_405(error):
  return set_error(405,'The method is not allowed for the requested URL.')

def set_error(status, message):
  return jsonify({
  'status': status,
  'message': message
  }), status

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)
