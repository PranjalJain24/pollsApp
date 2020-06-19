from django.conf import settings 

class pollsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_request(self, request, view_func, *view_args, **view_kargs):
        if (request.votes < 0):
            request.votes = 0

    def process_exception(self, request, exception):
        if settings.DEBUG:
            print(exception.__class__.__name__)
            print(exception.message)
        return None