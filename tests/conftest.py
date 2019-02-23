import pytest

# https://docs.pytest.org/en/latest/skipping.html
# https://docs.pytest.org/en/latest/example/markers.html


def pytest_addoption(parser):
    parser.addoption(
        "-E",
        action="store",
        metavar="NAME",
        help="only run tests matching the environment NAME.")


# def pytest_addoption(parser):
#     parser.addoption("--sound", action="store_true",
#                      help="run the tests only in case of that command line (marked with marker @sound)")


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line(
        "markers", "env(name): mark test to run only on named environment")


def pytest_runtest_setup(item):
    envnames = [mark.args[0] for mark in item.iter_markers(name='env')]
    if envnames:
        if item.config.getoption("-E") not in envnames:
            pytest.skip("test requires env in %r" % envnames)
