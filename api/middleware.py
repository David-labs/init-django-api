from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class OptionsMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        super().__init__(get_response)

    def __call__(self, request):
        '''处理每个请求'''
        if request.method == 'OPTIONS':
            allowed_methods = self.get_allowed_methods(request.path)
            response = JsonResponse(
                data={},
                status=200
            )
            response["Allow"] = ", ".join(allowed_methods)
            response["Content-Type"] = "application/json"
            # return response
        
        response = self.get_response(request)
        return response

    def get_allowed_methods(self, path):
        if path == '/init':
            return ["OPTIONS", "POST"]
        else:
            return ["OPTIONS"]