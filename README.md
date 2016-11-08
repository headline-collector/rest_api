![logo](https://github.com/yiakwy/Siganture-Authentication-Package/raw/master/static/logo.png)
----------------------------------------------------------------------------------------------
Signautre Authentication Package
================================

> SDK(sign5) + Django-Rest based Authentication.py and Django based QueryBackend.py + Generic Dynamic Serializer Manager(third-party.serializer.py) to support dynamic fields select, and password clean up.
> The Signature Authentication implements stardard proposed in 2015, [draft-cavage-http-signature](https://www.ietf.org/archive/id/draft-cavage-http-signatures-05)

[TOC]

# Usage
![Authorization Scheme](https://github.com/yiakwy/Siganture-Authentication-Package/raw/master/static/Authorization.png)


### Authentication located in "api.auth".
> api.auth.authentication : This implements Django-Rest based Signautre Authentication scheme
> api.auth.backends: This implements Django based authentication backends
> SDK is used as a client to issue or initiate a signature authentication. 

- authorized
![authorized example](https://github.com/yiakwy/Siganture-Authentication-Package/raw/master/static/authorized.png)

- unauthorized
![unauthorized example](https://github.com/yiakwy/Siganture-Authentication-Package/raw/master/static/unauthorized.png)

### We also provide several tools in api to help you setup the project.
> api.models.App, which establishes a one to one relationship with exsiting auth model
> api.utils.parser for fields extraction

### Generic Serializer Manager Descripter

It fascilitate your development, typically you can use it this way as demonstrated in api.view.py
```python
class `ABC`ViewSet(ViewRouter):
	serializer = SerializerManager(`ABC`Serializer)
	...

	@list_router(method=['GET'], permission_classes=[IsAuthenticated])
	def abc(req, verbose_key=None)
        queryset = self.get_queryset()
        page = self.paginated_queryset(queryset)
        data = self.serializer(page, manay=True)
        if page is None or \
                len(page) < self.page_slot:
			return Response(data=data)
		else:
			return self.get_paginated_response(data=data)
```

# Support Passport Implementation
## workflow
> After initialing a authentication, server requires signature before issuing an token for successive authentication in case of different behaviors.
> Once Signature successful, the package will grant a token to the existing Auth User model's instance.

# demo project 增删(改)?查
1. 订阅号:
	创建一个订阅, 返回订阅object，可以查询其资源位置:
	```javascript
	POST : http://127.0.0.1:8000/api/0.1.4/subcribe/?username=haha&website_name=HN
	```
	
	销毁一个:
	```javascript
	DELETE http://127.0.0.1:8000/api/0.1.4/subcribe/{record_id}/
	```
	
	获取所有订阅:
	```javascript
	GET http://127.0.0.1:8000/api/0.1.4/subcribe/list/{user_name}/
	```
	
	如果想要把json数据弄出来, 请加format=json:
	```javascript
	GET http://127.0.0.1:8000/api/0.1.4/subcribe/list/haha/?format=json
	```
2. 用户号
	取得所有用户
	```javascript
	GET http://127.0.0.1:8000/api/0.1.4/user/
	```
	
	取得所有用户，并按用户名排序
	```javascript
	GET http://127.0.0.1:8000/api/0.1.4/user?ordering=username
	```
	
	取得某个用户号
	```javascript
	GET http://127.0.0.1:8000/api/0.1.4/user/{username}/
	```
	
	创建一个用户
	```javascript
	POST http://127.0.0.1:8000/api/0.1.4/user/jack/?password=123&email=yiak.222@gmail.com
	alias: 
	POST http://127.0.0.1:8000/api/0.1.4/register?username=gege&password=asfdase&email=jiakechong@jiake.com
	```
3. 网站列表
	获取网站
	```javascript
	GET http://127.0.0.1:8000/api/0.1.4/website/
	```
	获取网站X
	```javascript
	GET http://127.0.0.1:8000/api/0.1.4/website/HN/
	```

	创建网站X
	```javascript
	POST http://127.0.0.1:8000/api/0.1.4/website/Obama/?tags=100&url=www.obama.com
	```
	删除网站X
	```javascript
	DELETE http://127.0.0.1:8000/api/0.1.4/website/HN/
	```
（4）获取文章
	```javascript
	GET http://127.0.0.1:8000/api/0.1.4/headline/
	```
... ...
