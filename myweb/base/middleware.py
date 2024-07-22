def new_middleware(get_response):
    def middleware(request):
        print("before")
        response = get_response(request)
        print("after")
        return response

    return middleware


class NewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("before")
        response = self.get_response(request)
        print("after")
        return response


