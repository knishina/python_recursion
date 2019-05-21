from Factorial import factorial, o_factorial, factorial_r

# Test out the factorial function.
def test_factorial_0():
    assert (factorial(0) == 0)
def test_factorial_1():
    assert (factorial(1) == 1)
def test_factorial_2():
    assert (factorial(2) == 2)
def test_factorial_3():
    assert (factorial(5) == 120)


# Test out the o_factorial function.
def test_ofactorial_0():
    assert (o_factorial(0) == 0)
def test_ofactorial_1():
    assert (o_factorial(1) == 1)
def test_ofactorial_2():
    assert (o_factorial(2) == 2)
def test_ofactorial_5():
    assert (o_factorial(5) == 120)


# Test out the factorial_r function.
def test_factorialr_0():
    assert (factorial_r(0) == 0)
def test_factorialr_1():
    assert (factorial_r(1) == 1)
def test_factorialr_2():
    assert (factorial_r(2) == 2)
def test_factorialr_5():
    assert (factorial_r(5) == 120)