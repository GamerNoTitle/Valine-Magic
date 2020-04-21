# Valine-Magic

**因为Valine在2020/4/21下午更新了1.4.5，支持了自定义表情和自动拉取QQ头像，本仓库从此刻开始提供表情列表，而不是替换Valine原版js用的js链接**

点击对应的表情名可以直接到达表情列表，请注意：你在使用本仓库内的表情时请保持Valine的表情CDN为空，否则会造成表情无法正常获取的BUG

如果你有新的表情包想要加入，你可以提出issue，或者直接提交PR让我把表情包并入此库

PR要求：文件夹和文件名字为英文，文件夹内除了图片无任何文件

仓库内的那个PY脚本是我提前编写好用来写表情列表的脚本，如果你有需要可以随意取用

### 表情分类


| ![](https://cdn.jsdelivr.net/gh/GamerNoTitle/Picture-repo-v1@master/img/BQB/7.jpg) | ![](https://cdn.jsdelivr.net/gh/GamerNoTitle/Picture-repo-v1@master/img/BQB/[tv_doge].png) | ![](https://cdn.jsdelivr.net/gh/GamerNoTitle/Picture-repo-v1@master/img/BQB/[2233娘_第一].png) |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| [哔哩哔哩热词系列](https://github.com/GamerNoTitle/Valine-Magic/tree/master/bilibili/hotkey热词系列) | [哔哩哔哩小电视系列](https://github.com/GamerNoTitle/Valine-Magic/tree/master/bilibili/tv小电视系列) | [哔哩哔哩2233娘系列](https://github.com/GamerNoTitle/Valine-Magic/tree/master/bilibili/2233娘系列) |
|          ![](https://bqb1.bili33.top/alu/中枪.png)           |                                                              |                                                              |
| [阿鲁alu系列](https://github.com/GamerNoTitle/Valine-Magic/tree/master/alu) |                                                              |                                                              |

---

~~这是Valine-Magic（魔改版本）的表情包库，使用jsdelivr进行CDN加速~~

~~具体效果可以访问[https://bili33.top/About](https://bili33.top/About)的评论区进行查看（往下滑就看得到了）~~

~~会考虑做分类表情，但是肯定没那么快~~

预览图：![](https://cdn.jsdelivr.net/gh/GamerNoTitle/Picture-repo-v1@master/img/Valine-Magic/Result.png)

![](https://cdn.jsdelivr.net/gh/GamerNoTitle/Picture-repo-v1@master/img/Valine-Magic/Result-Stickers.png)

## 更新日志

### 2020/4/21 V2.0.0

修改本仓库发布方式，因为Valine在今日下午进行了更新，支持了自定义表情，那么本项目最初的目标就不需要使用修改JS的方式来实现了，所以我改变了发布方式，将来在这个仓库会发布各表情包的List，是按照Valine所需要的格式写好的List，加入到Valine的表情列表就可以立即使用的那种

表情更新：哔哩哔哩热词系列、哔哩哔哩小电视系列、哔哩哔哩2233娘系列、阿鲁alu系列

### 2020/4/21 V1.0.1

**基于Valine 1.4.4**

版本js地址：https://cdn.jsdelivr.net/gh/GamerNoTitle/Valine-Magic@master/js/1.0.1/valine.min.js

更新了alu系列表情包（[#1](https://github.com/GamerNoTitle/Valine-Magic/issues/1)），删除了使用频率较低的系列表情，被删除的表情显示不受影响，仍可继续使用

表情包会丢在coding的[仓库](https://gamernotitle.coding.net/p/Valine-BQB1/)里面，本仓库只用于发布新版本

修改了python脚本，使得更易使用，加入下载用的python脚本

### 2020/4/19 V1.0.0

**基于Valine 1.4.4**

版本js地址：https://cdn.jsdelivr.net/gh/GamerNoTitle/Picture-repo-v1@Valine-Magic-V1.0/js/valine.min.js

启动Valine-Magic项目，将原本Valine的表情替换为B站现有的表情包，加入判断为QQ邮箱则显示QQ头像的功能（参考[https://blog.csdn.net/cungudafa/article/details/104638730](https://blog.csdn.net/cungudafa/article/details/104638730)）

第一批表情包[在此仓库](https://github.com/GamerNoTitle/Picture-repo-v1/tree/master/img/BQB)