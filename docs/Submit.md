### 如何提交新表情

#### 方法1：到对应的仓库提交PR

首先先fork一份[ValineCDN仓库](https://github.com/GamerNoTitle/ValineCDN)，然后clone到本地

接着新建一个文件夹，里面存放图片，一个类别存放在一个文件夹（仅英文）内，生成索引（类似每个类别下的类别，例如[这里](https://github.com/GamerNoTitle/Valine-Magic/tree/master/bilibili/tv小电视系列)），你可以将配套的`BQB-Link-List-Generate.py`文件放在你的文件夹下并运行，生成列表后复制备用，**请先删除路径指向文件为BQB-Link-List-Generate.py的那一行**，把更改push到你的仓库中，到[这里](https://github.com/GamerNoTitle/ValineCDN/pulls)提交一个新的PR

然后到[本仓库](https://github.com/GamerNoTitle/Valine-Magic)，同样先clone一份，在clone下来的目录的`Classification`文件夹中创建于上面存放分类的文件夹同名的文件夹（仅英文），在里面新建一个`README.md`，格式要求如下

```markdown
# 表情包名字

在这里填写你的描述

​```json
//在这里填入你的索引
​```

在这里将生成的预览图列表（格式为![]()的那一堆）贴入这里
```

保存文件，打开本仓库顶级目录下的README.md文件，将添加的表情类别写入索引（填入表格），参考如下链接

```markdown
[表情名字](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/表情文件夹)
```

Tips：Markdown的表格写法

```markdown
|   首行1   |   首行2   |   首行3   |
| ---- | ---- | ---- |
|   格子1   |   格子2   |   格子3   |
|   格子4   |   格子5   |   格子6   |
|   格子7   |   格子8   |   格子9   |
```

一般来说直接接着表格填就好了

再打开docs文件夹内的`Update.md`文件，写入更新日志，其中版本号直接`+0.01`即可，如：

```markdown
### 2020/x/x V2.x.x
加入xxx表情包（由[@xxx](提供)）
```

请自己修改其中的内容，不要直接复制粘贴，将所有的更改push到你的仓库

最后，打开[PR页面](https://github.com/GamerNoTitle/Valine-Magic/pulls)，新建一个PR，等待合并即可！

#### 方法2：邮件发送

直接发送邮件到[admin@bili33.top](mailto:admin@bili33.top)即可，需要包含以下内容

1、表情（请用压缩包保存发送）

2、表情包名字（英文必须，因为要用来命名路径，中文可选）

3、共享者（GithubID）