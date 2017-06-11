from mypkg import myfunc as f


def test_avg1(vec1):
    assert len(vec1) == 5
    assert f.avg(vec1) == 2

def test_avg2(vec2):
    assert len(vec2) == 5
    assert f.avg(vec2) == 4
