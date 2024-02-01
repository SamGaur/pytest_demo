import pytest


# Fixture providing data
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]


# Test function using the fixture-provided data
def test_data_sum(sample_data):
    result = sum(sample_data)
    assert result == 15, "Sum is not as expected"


'''
In this example, the sample_data fixture provides a list of numbers, 
and the test_data_sum function uses this data for testing.
Pytest will automatically discover and run your test functions,
and it will handle the fixture setup and teardown for you. 
Fixtures are a flexible and powerful feature that can greatly enhance the maintainability 
and structure of your test code.
'''
