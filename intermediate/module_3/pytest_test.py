import pytest

def evenMethod(num):
    return num % 2 == 0
  
def test_even():
    assert evenMethod(22) == True
    with pytest.raises(AssertionError):
        assert evenMethod(7) == True

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_sum(sample_data):
    assert sum(sample_data) == 6
        
if __name__ == "__main__":
    pytest.main()
    