RESTFUL 增删改查

(1) 订阅号
创建一个订阅：返回订阅object，可以查询其资源位置
POST : http://127.0.0.1:8000/api/0.1.4/subcribe/?username=haha&website_name=HN
销毁一个：
DELETE http://127.0.0.1:8000/api/0.1.4/subcribe/{record_id}/
获取所有订阅：
GET http://127.0.0.1:8000/api/0.1.4/subcribe/list/{user_name}/

[
    {
        "id": 3,
        "importance": null,
        "user": {
            "id": 2,
            "username": "haha",
            "auth_id": {
                "id": 1,
                "created_at": 1476515594,
                "app_key": "YAK151320160713293917828",
                "app_name": "yak",
                "username": "haha",
                "auth_type": null,
                "app_secret": "716c8c4e1ae2b1f66bf9ff677b99a71038512199831e11cc330736f54b3bb12e",
                "callback_url": null,
                "is_available": false,
                "email": "yiak.wy@gmail.com",
                "latest_update_time": null,
                "token": "",
                "expire_date": null,
                "password": "163512108403620369"
            }
        },
        "website": {
            "id": 4,
            "url": "https://github.com/trending",
            "name": "github",
            "tags": "developer"
        }
    },
    {
        "id": 4,
        "importance": null,
        "user": {
            "id": 2,
            "username": "haha",
            "auth_id": {
                "id": 1,
                "created_at": 1476515594,
                "app_key": "YAK151320160713293917828",
                "app_name": "yak",
                "username": "haha",
                "auth_type": null,
                "app_secret": "716c8c4e1ae2b1f66bf9ff677b99a71038512199831e11cc330736f54b3bb12e",
                "callback_url": null,
                "is_available": false,
                "email": "yiak.wy@gmail.com",
                "latest_update_time": null,
                "token": "",
                "expire_date": null,
                "password": "163512108403620369"
            }
        },
        "website": {
            "id": 1,
            "url": "https://news.ycombinator",
            "name": "HN",
            "tags": "developer"
        }
    }
]

如果想要把json数据弄出来：请加format=json
GET http://127.0.0.1:8000/api/0.1.4/subcribe/list/haha/?format=json

[{"id":3,"importance":null,"user":{"id":2,"username":"haha","auth_id":{"id":1,"created_at":1476515594,"app_key":"YAK151320160713293917828","app_name":"yak","username":"haha","auth_type":null,"app_secret":"716c8c4e1ae2b1f66bf9ff677b99a71038512199831e11cc330736f54b3bb12e","callback_url":null,"is_available":false,"email":"yiak.wy@gmail.com","latest_update_time":null,"token":"","expire_date":null,"password":"163512108403620369"}},"website":{"id":4,"url":"https://github.com/trending","name":"github","tags":"developer"}},{"id":4,"importance":null,"user":{"id":2,"username":"haha","auth_id":{"id":1,"created_at":1476515594,"app_key":"YAK151320160713293917828","app_name":"yak","username":"haha","auth_type":null,"app_secret":"716c8c4e1ae2b1f66bf9ff677b99a71038512199831e11cc330736f54b3bb12e","callback_url":null,"is_available":false,"email":"yiak.wy@gmail.com","latest_update_time":null,"token":"","expire_date":null,"password":"163512108403620369"}},"website":{"id":1,"url":"https://news.ycombinator","name":"HN","tags":"developer"}}]

(2) 用户号
取得所有用户
GET http://127.0.0.1:8000/api/0.1.4/user

[
  {
    "id": 1,
    "username": "yadfdk",
    "auth_id": {
      "id": 3,
      "created_at": 1476515897,
      "app_key": "YADFDK151820160718241986379",
      "app_name": null,
      "username": "yadfdk",
      "auth_type": null,
      "app_secret": "d1b0ef415c6e4339ff8ac6718e2175760937b955f0b8358199c7474e2f761c54",
      "callback_url": null,
      "is_available": false,
      "email": "yiakfdfdfd.wy@gmail.com",
      "latest_update_time": null,
      "token": null,
      "expire_date": null,
      "password": "163512108403620369"
    }
  },
  {
    "id": 2,
    "username": "haha",
    "auth_id": {
      "id": 1,
      "created_at": 1476515594,
      "app_key": "YAK151320160713293917828",
      "app_name": "yak",
      "username": "haha",
      "auth_type": null,
      "app_secret": "716c8c4e1ae2b1f66bf9ff677b99a71038512199831e11cc330736f54b3bb12e",
      "callback_url": null,
      "is_available": false,
      "email": "yiak.wy@gmail.com",
      "latest_update_time": null,
      "token": "",
      "expire_date": null,
      "password": "163512108403620369"
    }
  }
]

取得所有用户，并按用户名排序
GET http://127.0.0.1:8000/api/0.1.4/user?ordering=username
[
  {
    "id": 2,
    "username": "haha",
    "auth_id": {
      "id": 1,
      "created_at": 1476515594,
      "app_key": "YAK151320160713293917828",
      "app_name": "yak",
      "username": "haha",
      "auth_type": null,
      "app_secret": "716c8c4e1ae2b1f66bf9ff677b99a71038512199831e11cc330736f54b3bb12e",
      "callback_url": null,
      "is_available": false,
      "email": "yiak.wy@gmail.com",
      "latest_update_time": null,
      "token": "",
      "expire_date": null,
      "password": "163512108403620369"
    }
  },
  {
    "id": 1,
    "username": "yadfdk",
    "auth_id": {
      "id": 3,
      "created_at": 1476515897,
      "app_key": "YADFDK151820160718241986379",
      "app_name": null,
      "username": "yadfdk",
      "auth_type": null,
      "app_secret": "d1b0ef415c6e4339ff8ac6718e2175760937b955f0b8358199c7474e2f761c54",
      "callback_url": null,
      "is_available": false,
      "email": "yiakfdfdfd.wy@gmail.com",
      "latest_update_time": null,
      "token": null,
      "expire_date": null,
      "password": "163512108403620369"
    }
  }
]

取得某个用户号
GET http://127.0.0.1:8000/api/0.1.4/user/{username}/

{
  "id": 2,
  "username": "haha",
  "auth_id": {
    "id": 1,
    "created_at": 1476515594,
    "app_key": "YAK151320160713293917828",
    "app_name": "yak",
    "username": "haha",
    "auth_type": null,
    "app_secret": "716c8c4e1ae2b1f66bf9ff677b99a71038512199831e11cc330736f54b3bb12e",
    "callback_url": null,
    "is_available": false,
    "email": "yiak.wy@gmail.com",
    "latest_update_time": null,
    "token": "",
    "expire_date": null,
    "password": "163512108403620369"
  }
}

创建一个用户

POST http://127.0.0.1:8000/api/0.1.4/user/jack/?password=123&email=yiak.222@gmail.com
alias: 
POST http://127.0.0.1:8000/api/0.1.4/register?username=gege&password=asfdase&email=jiakechong@jiake.com

{
  "id": null,
  "username": "jack",
  "auth_id": {
    "id": 10,
    "created_at": 1476555808,
    "app_key": "JACK1523201618231308864920",
    "app_name": null,
    "username": "jack",
    "auth_type": null,
    "app_secret": "9d3c70c5a9c082fb5735df9e87f050c9fe5e49ee3d7322faf0d932f62285d23c",
    "callback_url": null,
    "is_available": false,
    "email": "yiak.222@gmail.com",
    "latest_update_time": null,
    "token": null,
    "expire_date": null,
    "password": "163512108404620371"
  }
}


(3) 网站列表
获取网站
GET http://127.0.0.1:8000/api/0.1.4/website/

[
    {
        "id": 0,
        "url": "https://www.v2x.com",
        "name": "v2ex",
        "tags": "developer"
    },
    {
        "id": 1,
        "url": "https://news.ycombinator",
        "name": "HN",
        "tags": "developer"
    },
    {
        "id": 2,
        "url": "https://www.producthunt.com",
        "name": "productHunt",
        "tags": "product"
    },
    {
        "id": 3,
        "url": "https://wwwdouban.com/doulist/16163/",
        "name": "douban_movie",
        "tags": "entertainment"
    },
	
获取网站X
GET http://127.0.0.1:8000/api/0.1.4/website/HN/
{
    "id": 1,
    "url": "https://news.ycombinator",
    "name": "HN",
    "tags": "developer"
}

创建网站X
POST http://127.0.0.1:8000/api/0.1.4/website/Obama/?tags=100&url=www.obama.com

删除网站X
DELETE http://127.0.0.1:8000/api/0.1.4/website/HN/

（4）获取文章
GET http://127.0.0.1:8000/api/0.1.4/headline/

[
    {
        "id": 1,
        "url": "https://news.ycombinator.com/item?id=12417290",
        "post_date": null,
        "digest": null,
        "title": "An account of a serious medical emergency on a transoceanic flig789",
        "score": 789,
        "website_id": {
            "id": 1,
            "url": "https://news.ycombinator",
            "name": "HN",
            "tags": "developer"
        }
    },
    {
        "id": 2,
        "url": "https://news.ycombinator.com/item?id=12421687",
        "post_date": null,
        "digest": null,
		
		
。。。
