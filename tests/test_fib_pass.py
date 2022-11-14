import pytest
from app.app import app

def test_pass_1():
  result = app.test_client().get('/fib?n=1')
  body = result.get_json()
  assert 1 == body['result']
  assert 200 == result.status_code

def test_pass_2():
  result = app.test_client().get('/fib?n=9')
  body = result.get_json()
  assert 34 == body['result']
  assert 200 == result.status_code

def test_pass_3():
  result = app.test_client().get('/fib?n=1000')
  body = result.get_json()
  expected_value = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
  assert expected_value == body['result']
  assert 200 == result.status_code
