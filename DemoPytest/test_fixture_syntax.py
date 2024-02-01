# Fixture function
import pytest

'''fixtures are a powerful feature that allows you to set up and tear down 
resources or states before and after your tests. Fixtures help in organizing
 and managing the test setup and provide a clean way to share resources among
multiple tests.'''


@pytest.fixture
def setup_and_teardown():
    # Setup code before the test
    print("\nSetting up resources for the test")

    # Yielding allows the test to run
    yield

    # Teardown code after the test
    print("\nTearing down resources after the test")


# Test function using the fixture
def test_example(setup_and_teardown):
    # Test code using the fixture
    print("Running the test")


# Another test function using the same fixture
def test_another_example(setup_and_teardown):
    # Test code using the fixture
    print("Running another test")
