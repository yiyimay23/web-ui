
# web\APP-ui-auto 自动化框架


### 设计思路:

web\APP-ui-auto (python+selenium+pytest+allure) 

# 开始使用
查看浏览器与驱动版本，driver文件夹下更新

### 1开始准备

```python
# 安装所需的依赖环境(阿里源安装 * 操作系统中必须有python3, 推荐python3.8或者更高版本)
本用例使用的是3.9.6

# 先自行安装Node.js\selenium\appium\allure

# 安装配置Allure(官网下载解压包)
https://github.com/allure-framework/allure2/releases

解压allure - commandline - 2.30.0.zip包到对应目录

把allure - commandline - 2.30.0 / bin加入到环境变量

打开控制台输入: allure - -version出来版本代表安装成功

# ===================================

pip
install - r
requirements.txt
https://mirrors.aliyun.com/pypi/simple



# 运行(run.py 文件即可)

python3
run.py

```

### 2使用说明
0.run.py运行的用例规则pytest.ini

1 本架构元素定位 数据依赖为yaml文件

2 使用前需要对 yaml模板的熟悉 参考（databse/file/test_demo_yaml）注释说明

3 web-base.py 为 web函数封装 已经封装了功能代码 可以仔细阅读注释来完成页面功能！

4 app_base.py 为 app函数封装 可以仔细阅读注释来完成页面功能

5 目前浏览器支持 ctenos7(谷歌/火狐)， windos(谷歌/火狐/IE)，mac(谷歌/火狐/safair) 


### 3用例维护--以web为例
1）database--locatorYAML

2)database--caseYAML

3)pageobj

4)case