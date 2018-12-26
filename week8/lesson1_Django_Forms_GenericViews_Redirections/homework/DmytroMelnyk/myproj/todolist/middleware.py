import requests


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called. (request, view_func, view_args, view_kwargs

        return response

    def bot_send_message(self):
        """
        func for middleware to send a messages into telegram bot named @CursortaskBot
        :return: response status code
        """
        token = '609646021:AAFsEP0pjSaQdsveTZpLWI4xz9jPQzsPqOY'
        chat_id = 464902368
        message = "Someone view your record with ID=52"
        response = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path == '/todos/details/52':
            self.bot_send_message()
