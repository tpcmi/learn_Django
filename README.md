## Todo

- [ ] [django-admin和manage.py详细](https://docs.djangoproject.com/zh-hans/3.2/ref/django-admin/)
- [ ] [setting.py配置](https://docs.djangoproject.com/zh-hans/3.2/topics/settings/)
- [ ] [url.py调度器](https://docs.djangoproject.com/zh-hans/3.2/topics/http/urls/)
- [ ] [asgi.py](https://docs.djangoproject.com/zh-hans/3.2/howto/deployment/asgi/)
- [ ] [wsgi.py](https://docs.djangoproject.com/zh-hans/3.2/howto/deployment/wsgi/)


## Notes

### 项目VS应用

-  Django 中，每一个应用都是一个 Python 包
- 项目则是一个网站使用的配置和应用的集合

### 添加新应用
#### include()
它的作用是截断原先的路由，插入新的匹配url部分