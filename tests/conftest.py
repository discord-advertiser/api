import os
import pytest


@pytest.fixture
def files():
    files = os.listdir(path="tests/snapshots")

    f = dict()
    for file in files:
        try:
            content = open("tests/snapshots/" + file, "r").read()
            f[file] = content
        except IsADirectoryError:
            pass
    yield f
