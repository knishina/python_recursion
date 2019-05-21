from MaxOfList import maximum, o_maximum, maximum_r

# Prebaked lists.
listy0 = []
listy1 = [1, 2, 3]
listy2 = [-1, 0, 1, 3, -5]
listy3 = [-2, 2, -1, 1, 3, -3, 5, -5, 100]

# Test out minimum function.
def test_maximum_0():
    assert (maximum(listy0) == None)
def test_maximum_1():
    assert (maximum(listy1) == 3)
def test_maximum_2():
    assert (maximum(listy2) == 3)
def test_maximum_3():
    assert (maximum(listy3) == 100)


# Test out o_minimum function.
def test_o_maximum_0():
    assert (o_maximum(listy0) == None)
def test_o_maximum_1():
    assert (o_maximum(listy1) == 3)
def test_o_maximum_2():
    assert (o_maximum(listy2) == 3)
def test_o_maximum_3():
    assert (o_maximum(listy3) == 100)


# Test out the minimum_r function.
def test_maximumr_0():
    assert (maximum_r(listy0) == None)
def test_maximumr_1():
    assert (maximum_r(listy1) == 3)
def test_maximumr_2():
    assert (maximum_r(listy2) == 3)
def test_maximumr_3():
    assert (maximum_r(listy3) == 100)