from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


### Test with number 0
def test_0():
    test_num = 0
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 0, 
        'number_before_in_series': None, 
        'number_after_in_series': 1
    }

### Test with number 1
def test_1():
    test_num = 1
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 1, 
        'number_before_in_series': 1, 
        'number_after_in_series': 2
    }

### Test with number 2
def test_2():
    test_num = 2
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 2, 
        'number_before_in_series': 1, 
        'number_after_in_series': 3
    }

### Test with number 3
def test_3():
    test_num = 3
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 3, 
        'number_before_in_series': 2, 
        'number_after_in_series': 5
    }

### Test with number 4
def test_4():
    test_num = 4
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 3, 
        'number_before_in_series': 2, 
        'number_after_in_series': 5
    }

### Test with number 5
def test_5():
    test_num = 5
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 5, 
        'number_before_in_series': 3, 
        'number_after_in_series': 8
    }

### Test with number 6
def test_6():
    test_num = 6
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 5, 
        'number_before_in_series': 3, 
        'number_after_in_series': 8
    }

### Test with number 7
def test_7():
    test_num = 7
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 8, 
        'number_before_in_series': 5, 
        'number_after_in_series': 13
    }

### Test with number 8
def test_8():
    test_num = 8
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 8, 
        'number_before_in_series': 5, 
        'number_after_in_series': 13
    }

### Test with number 9
def test_9():
    test_num = 9
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 8, 
        'number_before_in_series': 5, 
        'number_after_in_series': 13
    }

### Test with number 10
def test_10():
    test_num = 10
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 8, 
        'number_before_in_series': 5, 
        'number_after_in_series': 13
    }

### Test with number 11
def test_11():
    test_num = 11
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 13,
        'number_before_in_series': 8, 
        'number_after_in_series': 21
    }

### Test with number 12
def test_12():
    test_num = 12
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 13, 
        'number_before_in_series': 8, 
        'number_after_in_series': 21
    }

### Test with number 13
def test_13():
    test_num = 13
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 13, 
        'number_before_in_series': 8, 
        'number_after_in_series': 21
    }

### Test with number 14
def test_14():
    test_num = 14
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 13, 
        'number_before_in_series': 8, 
        'number_after_in_series': 21
    }

### Test with number 15
def test_15():
    test_num = 15
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 13, 
        'number_before_in_series': 8, 
        'number_after_in_series': 21
    }

### Test with number 16
def test_16():
    test_num = 16
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 13, 
        'number_before_in_series': 8, 
        'number_after_in_series': 21
    }

### Test with number 17
def test_17():
    test_num = 17
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 13, 
        'number_before_in_series': 8, 
        'number_after_in_series': 21
    }

### Test with number 18
def test_18():
    test_num = 18
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 21, 
        'number_before_in_series': 13, 
        'number_after_in_series': 34
    }

### Test with number 19
def test_19():
    test_num = 19
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 21, 
        'number_before_in_series': 13, 
        'number_after_in_series': 34
    }

### Test with number 20
def test_20():
    test_num = 20
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 21, 
        'number_before_in_series': 13, 
        'number_after_in_series': 34
    }

### Test with number 21
def test_21():
    test_num = 21
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 21, 
        'number_before_in_series': 13, 
        'number_after_in_series': 34
    }

### Test with number 22
def test_22():
    test_num = 22
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 21, 
        'number_before_in_series': 13, 
        'number_after_in_series': 34
    }

### Test with number 23
def test_23():
    test_num = 23
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 21, 
        'number_before_in_series': 13, 
        'number_after_in_series': 34
    }

### Test with number 24
def test_24():
    test_num = 24
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 21, 
        'number_before_in_series': 13, 
        'number_after_in_series': 34
    }

### Test with number 25
def test_25():
    test_num = 25
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 21, 
        'number_before_in_series': 13, 
        'number_after_in_series': 34
    }

### Test with number 26
def test_26():
    test_num = 26
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 21, 
        'number_before_in_series': 13, 
        'number_after_in_series': 34
    }

### Test with number 27
def test_27():
    test_num = 27
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 21, 
        'number_before_in_series': 13, 
        'number_after_in_series': 34
    }

### Test with number 28
def test_28():
    test_num = 28
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 34, 
        'number_before_in_series': 21, 
        'number_after_in_series': 55
    }

### Test with number 233
def test_233():
    test_num = 233
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 233, 
        'number_before_in_series': 144, 
        'number_after_in_series': 377
    }

### Test with number 234
def test_234():
    test_num = 234
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 233, 
        'number_before_in_series': 144, 
        'number_after_in_series': 377
    }

### Test with number 10946
def test_10946():
    test_num = 10946
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 10946, 
        'number_before_in_series': 6765, 
        'number_after_in_series': 17711
    }

### Test with number 10947
def test_10947():
    test_num = 10947
    response = client.get(f'/api/v1/FindInFibonacci/{test_num}')
    assert response.status_code == 200
    assert response.json() == {
        'nearest_fibonacci': 10946, 
        'number_before_in_series': 6765, 
        'number_after_in_series': 17711
    }
