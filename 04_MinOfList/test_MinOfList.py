from MinOfList import minimum, o_minimum, minimum_r

# Prebaked lists.
listy0 = []
listy1 = [1, 2, 3]
listy2 = [1, -1, 0, 0, 3]
listy3 = [-50, -5, -0.5, 50, 100]

# Test out minimum function.
def test_minimum_0():
    assert (minimum(listy0) == "None")
def test_minimum_1():
    assert (minimum(listy1) == 1)
def test_minimum_2():
    assert (minimum(listy2) == -1)
def test_minimum_3():
    assert (minimum(listy3) == -50)


# Test out o_minimum function.
def test_o_minimum_0():
    assert (o_minimum(listy0) == None)
def test_o_minimum_1():
    assert (o_minimum(listy1) == 1)
def test_o_minimum_2():
    assert (o_minimum(listy2) == -1)
def test_o_minimum_3():
    assert (o_minimum(listy3) == -50)


# Test out the minimum_r function.
def test_minimumr_0():
    assert (minimum_r(listy0) == None)
def test_minimumr_1():
    assert (minimum_r(listy1) == 1)
def test_minimumr_2():
    assert (minimum_r(listy2) == -1)
def test_minimumr_3():
    assert (minimum_r(listy3) == -50)