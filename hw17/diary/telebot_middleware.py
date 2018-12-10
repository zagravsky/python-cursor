from urllib import request as urllibreq

class TelegramBotMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def ping_bot(self):
        bot_token = "642553332:AAFHqUeU5SHg0sfs4dE_o6-Lj7eoasZ0qf4"
        chat_id = '-1001122990938'
        text = 'Someone viewed your record with ID=5'

        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?text={text}&chat_id={chat_id}"
        bot_request = urllibreq.urlopen(url)
        return bot_request

    def __call__(self, request):
        print(request.get_full_path())
        print("Caught request: ", request)
        if str(request.get_full_path()) == '/posts/5':
            self.ping_bot()
        response = self.get_response(request)
        print("Caught response: ", response)
        return response




