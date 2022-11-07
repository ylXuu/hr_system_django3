# 人力资源管理系统简易示例
## 部署
### 环境
+ python >= 3.6
+ mysql 8
### python package
+ django == 3.2.7
+ pymysql

### 配置
1. 将项目pull到本地
2. 在本地mysql创建用于本项目的空数据库，并在settings.py中配置
3. 在项目根目录执行命令用于数据迁移
```
python manage.py makemigrations
python manage.py migrate
```
4. 在项目根目录执行命令，运行项目
```
python manage.py runserver
```

## 说明
本项目仅为django3与mysql的实例框架，项目中的模型、功能等实现均不完全且不代表最优实现方式。可以基于本项目框架基础上进行丰富与修改。

