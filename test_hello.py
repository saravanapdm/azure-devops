from hello import toyou, add, subtract


def setup_function(function):
^Iprint("Running Setup: %s" % function.__name__)
^Ifunction.x = 10


def teardown_function(function):
^Iprint("Running Teardown: %s" % function.__name__)
^Idel function.x


### Run to see failed test
#def test_hello_add():
#    assert add(test_hello_add.x) == 12

def test_hello_subtract():
^Iassert subtract(test_hello_subtract.x) == 9
