Valine-Magic

**因为Valine在2020/4/21下午更新了1.4.5，支持了自定义表情和自动拉取QQ头像，本仓库从此刻开始提供表情列表，而不是替换Valine原版js用的js链接**

点击对应的表情名可以直接到达表情列表，请注意：你在使用本仓库内的表情时请将Valine的CDN设置为`https://valinecdn.bili33.top/`	[#2](https://github.com/GamerNoTitle/Valine-Magic/issues/2)

复制的列表可以直接复制到例如[butterfly](https://github.com/jerryc127/hexo-theme-butterfly)主题的`valine.json`内，或者是各种用于放Valine表情配置的地方

请注意：如果你想添加多个分类，请记得在每个分类的最后一个表情后面加个`,`否则Valine无法识别。假设下面这个表情为该系列最后一个表情：

```json
"hotkey1": "bilibiliHotKey/1.jpg"
```

你想在这个表情下面添加其他表情的时候，那么请在这个表情的后面加个`,`就像下面这样

```json
"hotkey1": "bilibiliHotKey/1.jpg",
```

如果你有新的表情包想要加入，你可以提出issue，或者直接发到[admin@bili33.top](mailto:admin@bili33.top)，并注上你的ID和表情包名字（中文英文都需要）

仓库内的那个PY脚本是我提前编写好用来写表情列表的脚本，如果你有需要可以随意取用

这里有跟本项目同类型的表情仓库，如果在本仓库未找到你想要的表情包可以到这里找 [表情速查](https://www.antmoe.ml/)

### 表情分类


|    ![](https://valinecdn.bili33.top/bilibiliHotKey/7.jpg)    |  ![](https://valinecdn.bili33.top/bilibilitv/[tv_doge].png)  | ![](https://valinecdn.bili33.top/bilibili2233/[2233娘_第一].png) |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| [哔哩哔哩热词系列](https://github.com/GamerNoTitle/Valine-Magic/tree/master/bilibili/hotkey热词系列) | [哔哩哔哩小电视系列](https://github.com/GamerNoTitle/Valine-Magic/tree/master/bilibili/tv小电视系列) | [哔哩哔哩2233娘系列](https://github.com/GamerNoTitle/Valine-Magic/tree/master/bilibili/2233娘系列) |
|        ![](https://valinecdn.bili33.top/alu/中枪.png)        | <img src='https://valinecdn.bili33.top/Menhera-chan/5.jpg' width=120 height=102></img> |    ![](https://valinecdn.bili33.top/HONKAI3-Daily/14.gif)    |
| [阿鲁alu系列](https://github.com/GamerNoTitle/Valine-Magic/tree/master/alu) | [メンヘラちゃん(Menhera-chan)系列表情包](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Menhera-chan) | [HONKAI崩坏3 日常篇](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3/HONKAI3-Daily) |
|     ![](https://valinecdn.bili33.top/HONKAI3-Star/3.gif)     |   ![](https://valinecdn.bili33.top/HONKAI3-Crayon/16.gif)    |    ![](https://valinecdn.bili33.top/HONKAI3-Pure/13.gif)     |
| [HONKAI崩坏3 观星篇](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3/HONKAI3-Star) | [HONKAI崩坏3 蜡笔日常篇](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3/HONKAI3-Crayon) | [HONKAI崩坏3 纯色日常篇](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3/HONKAI3-Pure) |
| <img src='https://valinecdn.bili33.top/HONKAI3-Stan/4f921b8ad8c16f3d2c73e3c04c5735ca9b41187b.gif' width=104 height=74.4> | <img src='https://valinecdn.bili33.top/HONKAI3-AIChan/d65b36ccae610bc4479209cd6e62bb91b0f76188.jpg' width=125 height=111></img> | <img src='https://valinecdn.bili33.top/HONKAI3-Durandal-Search/f1b9a456587638e488d93ccaa95dde59aef3af01.gif' height=100 width=100></img> |
| [HONKAI崩坏3 史丹](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3/HONKAI3-Stan) | [HONKAI崩坏3 爱酱](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3/HONKAI3-AIChan) | [HONKAI崩坏3 目标！幽兰黛尔](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3/HONKAI3-Durandal-Search) |
| <img src='https://valinecdn.bili33.top/HONKAI3-MEI/bf68423446465d396d3cbd8856882b5e9fb1c0c7.gif' width=120 height=120> | <img src='https://valinecdn.bili33.top/HONKAI3-NEWYEAR-2019/dc1a2b2032fad29373fe8460d4ad89ca848355a9.jpg' width=120 height=120> |                                                              |
| [HONKAI崩坏3 芽衣的剑道修行](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3/HONKAI3-MEI) | [HONKAI崩坏3 2019新年](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3/HONKAI3-NEWYEAR-2019) |                                                              |

---

## 更新日志

### 2020/4/24 V2.0.3

加入崩坏3系列5组表情包（官方表情）

[HONKAI崩坏3 史丹](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3/HONKAI3-Stan) | [HONKAI崩坏3 爱酱](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3/HONKAI3-AIChan) | [HONKAI崩坏3 目标！幽兰黛尔](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3/HONKAI3-Durandal-Search) | [HONKAI崩坏3 芽衣的剑道修行](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3/HONKAI3-MEI) | [HONKAI崩坏3 2019新年](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3/HONKAI3-NEWYEAR-2019)

### 2020/4/24 V2.0.2

加入崩坏3系列4组表情包（QQ内提取）

[HONKAI崩坏3 日常篇](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3-Daily) | [HONKAI崩坏3 观星篇](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3-Star) | [HONKAI崩坏3 蜡笔日常篇](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3-Crayon) | [HONKAI崩坏3 纯色日常篇](https://github.com/GamerNoTitle/Valine-Magic/tree/master/HONKAI3-Pure)

### 2020/4/23 V2.0.1

加入[メンヘラちゃん(Menhera-chan)](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Menhera-chan)系列表情包（中文版）

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