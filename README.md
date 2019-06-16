# Django 
- [python3-cookbook](https://python3-cookbook.readthedocs.io/zh_CN/latest/chapters/p01_data_structures_algorithms.html)  
- [Django REST Framework教程](https://www.django.cn/course/show-20.html)  
- [django-rest-framework](https://www.django-rest-framework.org/)  
- [Django 文档](https://docs.djangoproject.com/zh-hans/2.2/)
- [webpack 文档](https://www.webpackjs.com/concepts/)
- [jinja2 文档](http://docs.jinkan.org/docs/jinja2/)
- [Django 文档](https://code.ziqiangxuetang.com/django/django-nginx-deploy.html)
- [Django+Bootstrap+Mysql 搭建个人博客（一）](https://www.cnblogs.com/derek1184405959/p/9060981.html)
- [将Django项目部署到服务器](https://www.jianshu.com/p/36ef6557c910)



## 创建项目
```
# 查看django版本号，如果你得到的是一个“No module named django”的错误提示，则表明你还未安装。
$ python -m django --version
# 创建一个 mysite 项目(生成的是一个目录)
$ django-admin startproject mysite
```

## 创建投票应用
```buildoutcfg
$ cd mysite
$ python manage.py startapp polls
```

## 运行服务
```buildoutcfg
# 在manage.py所在的目录下运行下面的命令：
$ python manage.py runserver

$ python manage.py runserver 8080

$ python manage.py runserver 0:8000
```

```buildoutcfg
# migrate 命令检查 INSTALLED_APPS 设置，为其中的每个应用创建需要的数据表
$ python manage.py migrate
# 通过运行 makemigrations 命令，Django 会检测你对模型文件的修改，并且把修改的部分储存为一次 迁移。
$ python manage.py makemigrations polls
# sqlmigrate 命令接收一个迁移的名称，然后返回对应的 SQL
$ python manage.py sqlmigrate polls 0001
# migrate 命令 - 自动执行数据库迁移并同步管理你的数据库结构的命令；
# 再次运行 migrate 命令，在数据库里创建新定义的模型的数据表
$ python manage.py migrate
# 进入交互式 Python 命令行
# 使用这个命令而不是简单的使用 "Python" 是因为 manage.py 会设置 DJANGO_SETTINGS_MODULE 环境变量，
# 这个变量会让 Django 根据 mysite/settings.py 文件来设置 Python 包的导入路径。
$ python manage.py shell
```