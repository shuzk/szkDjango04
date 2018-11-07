class my_mid:
    def __init__(self):
        print("--------------init")

    def process_request(self, request):
        print("----------------request")

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print("----------------view")

    def process_response(self, request, response):
        print("-----------response")
        return response


class exp1:
    def process_exception(self, request, exception):
        print("----------exp1")


class exp2:
    def process_exception(self, exception):
        print("-----------exp2")
