# 1. Install and configure virtualenv.
----
## 1.1 Install virtualenv if you haven't.

## 1.2 Create a virtual env under the projects folder.
Make sure you are using python3.
```
$ virtualenv -p python3 myenv
```

## 1.3 Activate virtualenv

```
$ source myenv/bin/activate
```

## 1.4 install packages
```
$ pip install -r requirements.txt
```

# 2. Daily development

```
$ git pull # 获取最新代码， 每次开发前，都要做一下。 免得产生一大堆冲突
$ source myenv/bin/activate # 激活python虚拟环境
$ pip install -r requirements.txt # 如果其他人安装了新包， 这个命令可以让你也自动装好
$ pip freeze > requirements.txt # 如果你安装了新的pip包, 用这个命令把新包的信息同步到requirements.txt中
```