import pytest
import numpy as np
from src.handle_data import load_data, load_and_append, parse_input_content

class TestLoadData:
    def test_returns_numpy_arrays(self):
        X, Y = load_data(1, 1)

        assert isinstance(X, np.ndarray)
        assert isinstance(Y, np.ndarray)

    def test_shapes_match(self):
        X, Y = load_data(1, 1)
        assert X.shape[0] == Y.shape[0]  # same number of rows

class TestLoadAndAppend:
    def test_returns_initial_inputs(self):
        X, Y = load_data(1, 1)
        
        xTest, yTest = load_and_append(1, 1)
        assert xTest is not None
        assert yTest is not None
        assert len(X) == len(xTest)
        assert len(Y) == len(yTest)

    def test_returns_week4_data(self):
        X, Y = load_data(1, 1)
        
        xTest, yTest = load_and_append(1, 4)
        assert xTest is not None
        assert yTest is not None
        assert len(X)+3 == len(xTest)
        assert len(Y)+3 == len(yTest)

