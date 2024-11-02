from typing import Any, Mapping

import orjson
from django.conf import settings
from django.http import HttpRequest
from ninja import NinjaAPI, Swagger
from ninja.responses import JsonResponse
from ninja.renderers import JSONRenderer, BaseRenderer
from api.apis import router as api_router

class ORJSONRenderer(JSONRenderer):
    def render(self, request: HttpRequest, data: Any, *, response_status: int) -> Any:
        ret = {
            'code': response_status,
            'success': False,
            'data': data
        }
 
        if isinstance(data, dict):
            # 管理平台跟服务器接口
            if 'error' in data or 'result' in data or 'version' in data:
                print(data)
                ret = data
            else:
                # 客户端接口
                ret['message'] = data.pop('detail', '请求成功')
                ret['code'] = data.pop('code',response_status)
                # if 200 <= response_status < 300:
                if response_status == 200:
                    ret['success'] = True

        return orjson.dumps(ret, **self.json_dumps_params)


api = NinjaAPI(
    title='xx APIs',
    description='desc',
    renderer=ORJSONRenderer(),
    urls_namespace='api',
    docs=Swagger(settings={"persistAuthorization": True})
)


api.add_router('v1', api_router)
