import pytest
import numpy as np


@pytest.fixture(scope="module")
def vec1():
    vec = np.array([0, 1, 2, 3, 4])
    yield vec  # provide the fixture value
    print("teardown vec1")
