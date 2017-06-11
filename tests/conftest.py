import pytest
import numpy as np
import os
import sys
sys.path.append('{}/repos/mypkg/src'.format(os.getenv('HOME')))


@pytest.fixture(scope="module")
def vec1():
    vec = np.array([0, 1, 2, 3, 4])
    yield vec  # provide the fixture value
    print("Teardown goes here")

@pytest.fixture(scope="module")
def vec2():
    vec = np.array([0, 2, 4, 6, 8])
    yield vec  # provide the fixture value
    print("Teardown goes here")
