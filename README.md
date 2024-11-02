### Init Django Api
```
git clone https://github.com/David-labs/init-django-api
cd init-django-sqlite
python -m pip install Django
python3 manage.py runserver
```

接口访问地址
http://127.0.0.1:8000/api/v1/hello

后台管理
http://127.0.0.1:8000/admin/
admin
admin@admin

##### 修改
- 接口文件 /api/apis.py
  修改签名key
```
def require_sign(view_func):
    @wraps(view_func)
    def decorated_function(request, *args, **kwargs):
        # 替换key
        key = 'secretKey'
```

#### APIs
http://127.0.0.1:8000/api/docs

### 安装详情
1.安装Django
python -m pip install Django

2.创建项目
django-admin startproject init_django_api

3.创建后台管理用户
python manage.py createsuperuser
创建用户名和密码即可

4.启动
python3 manage.py runserver


### 数据库Sqlite
python manage.py makemigrations api
python manage.py migrate





