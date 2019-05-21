from SumOfList import summ, o_summ, summ_r

# Prebaked lists of numbers.
listy0 = []
listy1 = [1, 2, 3, 4, 5]
listy2 = [3, 5, 7, 9, 11]
listy3 = [2, 4, 6, 8, 10, 10]

# Test out the summ function.
def test_summ0():
    assert (summ(listy0) == 0)
def test_summ1():
    assert (summ(listy1) == 15)
def test_summ2():
    assert (summ(listy2) == 35)
def test_summ3():
    assert (summ(listy3) == 40)


# Test out the o_summ function.
def test_osumm0():
    assert (o_summ(listy0) == 0)
def test_osumm1():
    assert (o_summ(listy1) == 15)
def test_osumm2():
    assert (o_summ(listy2) == 35)
def test_osumm3():
    assert (o_summ(listy3) == 40)


# Test out the summ_r function.
def test_summr0():
    assert (summ_r(listy0) == 0)
def test_summr1():
    assert (summ_r(listy1) == 15)
def test_summr2():
    assert (summ_r(listy2) == 35)
def test_summr3():
    assert (summ_r(listy3) == 40)