from CounterOfList import counter, o_counter, counter_r

# Prebaked lists.
listy0 = []
listy1 = [1, 1, 1, 1, 1, 1, 1]
listy2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listy3 = [0, 1, 0, 1, 0, 2, 0, 2, 0, 3, 0, 3]

# Try out the counter function.
def test_counter0():
    assert (counter(listy0) == 0)
def test_counter1():
    assert (counter(listy1) == 7)
def test_counter2():
    assert (counter(listy2) == 9)
def test_counter3():
    assert (counter(listy3) == 12)


# Try out the o_counter function.
def test_ocounter0():
    assert (o_counter(listy0) == 0)
def test_ocounter1():
    assert (o_counter(listy1) == 7)
def test_ocounter2():
    assert (o_counter(listy2) == 9)
def test_ocounter3():
    assert (o_counter(listy3) == 12)


# Try out the counter_r function.
def test_counterr0():
    assert (counter_r(listy0) == 0)
def test_counterr1():
    assert (counter_r(listy1) == 7)
def test_counterr2():
    assert (counter_r(listy2) == 9)
def test_counterr3():
    assert (counter_r(listy3) == 12)
