from FibonacciSequence import fibbs, fibbs_r

# Test out the fibbs function.
def test_fibbs_0():
    assert (fibbs(0) == 0)
def test_fibbs_1():
    assert (fibbs(1) == 1)
def test_fibbs_2():
    assert (fibbs (2) == 1)
def test_fibbs_3():
    assert (fibbs(3) == 2)
def test_fibbs_5():
    assert (fibbs(5) == 5)
def test_fibbs_9():
    assert (fibbs(9) == 34)

# Test out the fibbs_r function.
def testr_fibbs_0():
    assert (fibbs_r(0) == 0)
def testr_fibbs_1():
    assert (fibbs_r(1) == 1)
def testr_fibbs_2():
    assert (fibbs_r(2) == 1)
def testr_fibbs_3():
    assert (fibbs_r(3) == 2)
def testr_fibbs_5():
    assert (fibbs_r(5) == 5)
def testr_fibbs_9():
    assert (fibbs_r(9) == 34)