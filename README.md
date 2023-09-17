# fofa-api-edu

## 声明

> 本工具仅供用于提高搜索edu资产的效率，严禁用于非授权网站。



## 下载须知

切记，下载源码的时候，务必将`eduName.txt`文本文件放置于 `fofa-api-edu.py`同文件夹下

如果使用`fofa-api-edu.exe`，一样需要将`eduName.txt`文本文件放置于 `fofa-api-edu.exe`同文件夹下



## 工具简介

 该工具是基于fofa空间探测引擎，专门为搜索EDU资产定制的，内置中国大多数的高校名单，你只需要根据fofa的语法，就可以自动搜索出符合条件的高校的IP或域名

各位大佬们可以根据这个工具的源码进行二开。



## 使用帮助

### 直接下载exe



切记，下载源码或者exe的时候，务必将`eduName.txt`文本文件放置于 `fofa-api-edu.py`或 `fofa-api-edu.exe`同文件夹下

### 源码启动

**安装库**

```
pip install -r requirements.txt
```

**启动工具**

```
python fofa_api_edu.py
```

**输入案例**

    请输入邮箱：xxxxxx@xxxx
    请输入apikey：xxxxx
    请输入搜索条件：country="CN" && title=="Error 404--Not Found"



## 使用案例

![image-20230917142558706](https://gitee.com/yuan_boss/yuanboss-pic-bed/raw/master/img2/image-20230917142558706.png)



![image-20230917142835607](https://gitee.com/yuan_boss/yuanboss-pic-bed/raw/master/img2/image-20230917142835607.png)

这里控制台会直接输出符合条件的网址，可以通过二开，将其输出到文件中