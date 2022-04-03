

class CallObject:
    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        args[0]()
        return self.count


call_object = CallObject()


@call_object
def test_call():
    print('test call')


print(test_call)