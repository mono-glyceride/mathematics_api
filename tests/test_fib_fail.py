import pytest
from app.app import app

def test_fail_too_small_1():
  result = app.test_client().get('/fib?n=-1')
  body = result.get_json()
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_too_small_2():
  result = app.test_client().get('/fib?n=0')
  body = result.get_json()
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_not_integer_1():
  result = app.test_client().get('/fib?n=あ')
  body = result.get_json()
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_not_integer_2():
  result = app.test_client().get('/fib?n=u')
  body = result.get_json()
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_not_integer_3():
  result = app.test_client().get('/fib?n=0E')
  body = result.get_json()
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_not_integer_4():
  result = app.test_client().get('/fib?n=null')
  body = result.get_json()
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_correct_parameter_not_exist_1():
  result = app.test_client().get('/fib')
  body = result.get_json()
  assert 400 == body['status']
  assert 400 == result.status_code

def test_fail_correct_parameter_not_exist_2():
  result = app.test_client().get('/fib?m=1')
  body = result.get_json()
  assert 400 == body['status']
  assert 400 == result.status_code
