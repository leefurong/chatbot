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

# 3. Q&A

Q: 虚拟环境中安装的包， vscode不认识？导致Pylint报警之类
A: 如果您使用了pyenv和虚拟环境，并且在虚拟环境中安装了一个包，但是在VS Code中无法识别该包，可能是因为VS Code没有将其与虚拟环境关联起来。

为了解决这个问题，您需要打开VS Code并执行以下步骤：

1. 打开命令面板。在Windows或Linux上，可以使用Ctrl + Shift + P快捷键；在Mac上，则可以使用Command + Shift + P快捷键。

2. 在命令面板中，输入“Python: Select Interpreter”并选择它。这将打开Python解释器选择菜单。

3. 从列表中选择您的虚拟环境。如果您的虚拟环境不在列表中，请选择“Enter interpreter path”选项，并手动输入您虚拟环境的路径。

4. 等待VS Code重新加载Python解释器，并确保您的虚拟环境已正确配置。

5. 在VS Code中打开您的Python文件，并尝试导入您在虚拟环境中安装的包。现在，您应该能够顺利地导入该包了。