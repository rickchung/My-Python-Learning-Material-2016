class my_decorator(object):
    def __init__(self, f):
        print('inside my_decorator.__init__()')
        f()
    def __call__(self):
        print('inside my_decorator.__call__()')

@my_decorator
def a_function():
    print('inside a_function()')

print('Finished decorating a_function()')

a_function()