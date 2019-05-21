from DoublingNumbers import rice, rice_r

# Test out the rice function.
def test_rice_0():
    assert (rice(0) == 0)
def test_rice_1():
    assert (rice(1) == 1)
def test_rice_2():
    assert (rice(2) == 3)
def test_rice_4():
    assert (rice(4) == 15)


# Test out the rice_r function.
def test_ricer_0():
    assert (rice_r(0) == 0)
def test_ricer_1():
    assert (rice_r(1) == 1)
def test_ricer_2():
    assert (rice_r(2) == 3)
def test_ricer_4():
    assert (rice_r(4) == 15)