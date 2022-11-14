import pytest
from app.app import app

def test_fail_too_small_1():
  result = app.test_client().get('/fib?n=-1')
  body = result.get_json()
  assert 'min value is 1' == body['message']['n'][0]
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_too_small_2():
  result = app.test_client().get('/fib?n=0')
  body = result.get_json()
  assert 'min value is 1' == body['message']['n'][0]
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_not_integer_1():
  result = app.test_client().get('/fib?n=あ')
  body = result.get_json()
  assert "field 'n' cannot be coerced: invalid literal for int() with base 10: 'あ'" == body['message']['n'][0]
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_not_integer_2():
  result = app.test_client().get('/fib?n=u')
  body = result.get_json()
  assert "field 'n' cannot be coerced: invalid literal for int() with base 10: 'u'" == body['message']['n'][0]
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_not_integer_3():
  result = app.test_client().get('/fib?n=0E')
  body = result.get_json()
  assert "field 'n' cannot be coerced: invalid literal for int() with base 10: '0E'" == body['message']['n'][0]
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_not_integer_4():
  result = app.test_client().get('/fib?n=null')
  body = result.get_json()
  assert "field 'n' cannot be coerced: invalid literal for int() with base 10: 'null'" == body['message']['n'][0]
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_correct_parameter_not_exist_1():
  result = app.test_client().get('/fib')
  body = result.get_json()
  assert "field 'n' cannot be coerced: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'" == body['message']['n'][0]
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_correct_parameter_not_exist_2():
  result = app.test_client().get('/fib?m=1')
  body = result.get_json()
  assert "field 'n' cannot be coerced: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'" == body['message']['n'][0]
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_incorrect_parameter_exists():
  result = app.test_client().get('/fib?n=4&p=4')
  body = result.get_json()
  assert 400 == body['status']
  assert 400 == result.status_code

# 改行コードを含む攻撃的なリクエスト
def test_fail_HTTP_header_injection():
  result = app.test_client().get('/fib?n=9%0d%0aSet-Cookie%20SID=ABCD1234')
  body = result.get_json()
  assert 400 == body['status']
  assert False == hasattr(result.headers, 'Set-Cookie')
  assert 400 == result.status_code
