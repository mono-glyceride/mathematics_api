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
