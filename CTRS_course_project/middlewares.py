from django.shortcuts import render


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code >= 500:
            return render(request, '404.html')
        return response

    return middleware
