import requests


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        text = "Someone view your record with ID=5"
        api_key = "bot679416085:AAGrJ1N5NoZiWJFl6H-LdbNSi-zwf4iqUbk"

        if request.path.startswith('/student/5'):
            requests.post(
                f'https://api.telegram.org/{api_key}/sendMessage?chat_id=697362059&text={text}')

        # Code to be executed for each request/response after
        # the view is called.

        return response
