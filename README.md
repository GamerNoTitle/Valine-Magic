<div align='center'><img src='https://socialify.git.ci/GamerNoTitle/Valine-Magic/image?description=1&descriptionEditable=%E2%9C%A8Valine%2FMiniValine%2FWaline%E8%87%AA%E5%AE%9A%E4%B9%89%E8%A1%A8%E6%83%85%E5%88%97%E8%A1%A8%EF%BC%8C%E4%B8%BA%E4%BD%A0%E7%9A%84%E8%A1%A8%E6%83%85%E5%BA%93%E2%80%9C%E5%96%9C%E5%8A%A0%E4%BA%BF%E2%80%9D&font=Inter&forks=1&language=1&owner=1&pattern=Circuit%20Board&stargazers=1&theme=Light'></div>

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FGamerNoTitle%2FValine-Magic.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FGamerNoTitle%2FValine-Magic?ref=badge_shield) ![](https://data.jsdelivr.com/v1/package/gh/GamerNoTitle/ValineCDN/badge) ![](https://img.shields.io/github/last-commit/GamerNoTitle/Valine-Magic?style=for-the-badge) ![](https://img.shields.io/github/repo-size/GamerNoTitle/ValineCDN?style=for-the-badge) 

**访问量**（自2020.10.25 11:00:00）

![](https://count.getloli.com/get/@GamerNoTitle@Valine-Magic?theme=gelbooru)

点击对应的表情名可以直接到达表情列表，请注意：你在使用本仓库内的表情时请将Valine的CDN设置为下面表格中的任意一个

**本仓库不适配Twikoo，如需Twikoo表情请访问[https://github.com/2X-ercha/Twikoo-Magic](https://github.com/2X-ercha/Twikoo-Magic)**

**已经适配MiniValine**[#8](https://github.com/GamerNoTitle/Valine-Magic/issues/8)，有问题请使用issue反馈

**已经适配[Waline最新版写法](https://waline.js.org/guide/client/emoji.html#%E5%88%9B%E5%BB%BA%E8%87%AA%E5%B7%B1%E7%9A%84%E9%A2%84%E8%AE%BE)，直接与MiniValine使用同样的链接即可，使用中有问题请通过issue反馈**

在线详细情况可以点击[issue#6](https://github.com/GamerNoTitle/Valine-Magic/issues/6)进行查看

[更新日志](https://github.com/GamerNoTitle/Valine-Magic/discussions?discussions_q=category%3A%E6%9B%B4%E6%96%B0%E6%97%A5%E5%BF%97)

你可以提交表情包，请阅读[提交的正确方式](https://github.com/GamerNoTitle/Valine-Magic/tree/master/docs/Submit.md)

| [服务器](https://valinecdn-status.bili33.top/)（点击可看在线状态） | CDN链接                                                      |
| :----------------------------------------------------------: | :----------------------------------------------------------- |
| Github [![Better Uptime Badge](https://betteruptime.com/status-badges/v1/monitor/59za.svg)](https://betteruptime.com/?utm_source=status_badge) | https://valinecdn.bili33.top/                                |
| Github [![Better Uptime Badge](https://betteruptime.com/status-badges/v1/monitor/5szl.svg)](https://betteruptime.com/?utm_source=status_badge) | https://cdn.jsdelivr.net/gh/GamerNoTitle/ValineCDN@master/   |
| Coding [![Better Uptime Badge](https://betteruptime.com/status-badges/v1/monitor/59zb.svg)](https://betteruptime.com/?utm_source=status_badge) | https://mirrorcdn.bili33.top/                                |
| Coding [![Better Uptime Badge](https://betteruptime.com/status-badges/v1/monitor/5szm.svg)](https://betteruptime.com/?utm_source=status_badge) | https://gamernotitle.coding.net/p/ValineCDN/d/ValineCDN/git/raw/master/ |

### Valine

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

### MiniValine

直接复制每个分类中的MiniValine所提供的链接（其中`https://valinecdn.bili33.top/`可以替换为任意CDN链接（见上表）），然后放在`emotionUrl`里面即可，请注意遵循列表写法，如：

```html
<body>
    <div class="mvcomment"></div>
    <script>
      new MiniValine({
          el: '.mvcomment',
          appId: 'appId',
          appKey: 'appKey',
          placeholder: 'Write a Comment O(∩_∩)O~~',
          emotionUrl: ['https://valinecdn.bili33.top/alu','https://valinecdn.bili33.top/bilibiliHotKey']
      })
    </script>
</body>

```

### Waline

直接复制与`MiniValine`相同的链接使用即可（懒得在每一个分类下的MiniValine后面加上Waline了），放在emoji列表中使用，例如

```javascript
Waline({
  el: '#waline',
  serverURL: '<YOUR SERVER URL>',

  // 设置 emoji 为微博与哔哩哔哩
  emoji: [
    'https://valinecdn.bili33.top/bilibiliHotKey',
    'https://valinecdn.bili33.top/bilibilitv',
  ],
});
```

或者你也可以使用旧版方式（不推荐，Waline将来可能砍掉这种格式），将Valine的配置复制到emoji表即可！（这里就不做例子了，毕竟我没有用Waline）

### 表情分类


|    ![](https://valinecdn.bili33.top/bilibiliHotKey/7.jpg)    |  ![](https://valinecdn.bili33.top/bilibilitv/[tv_doge].png)  | ![](https://valinecdn.bili33.top/bilibili2233/[2233娘_第一].png) |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| [哔哩哔哩热词系列](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/bilibili/hotkey热词系列) | [哔哩哔哩小电视系列](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/bilibili/tv小电视系列) | [哔哩哔哩2233娘系列](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/bilibili/2233娘系列) |
|        ![](https://valinecdn.bili33.top/alu/中枪.png)        | <img src='https://valinecdn.bili33.top/Menhera-chan/5.jpg' width=120 height=102></img> |    ![](https://valinecdn.bili33.top/HONKAI3-Daily/14.gif)    |
| [阿鲁alu系列](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/alu) | [メンヘラちゃん(Menhera-chan)系列表情包](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Menhera-chan) | [HONKAI崩坏3 日常篇](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/HONKAI3/HONKAI3-Daily) |
|     ![](https://valinecdn.bili33.top/HONKAI3-Star/3.gif)     |   ![](https://valinecdn.bili33.top/HONKAI3-Crayon/16.gif)    |    ![](https://valinecdn.bili33.top/HONKAI3-Pure/13.gif)     |
| [HONKAI崩坏3 观星篇](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/HONKAI3/HONKAI3-Star) | [HONKAI崩坏3 蜡笔日常篇](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/HONKAI3/HONKAI3-Crayon) | [HONKAI崩坏3 纯色日常篇](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/HONKAI3/HONKAI3-Pure) |
| <img src='https://valinecdn.bili33.top/HONKAI3-Stan/4f921b8ad8c16f3d2c73e3c04c5735ca9b41187b.gif' width=104 height=74.4> | <img src='https://valinecdn.bili33.top/HONKAI3-AIChan/d65b36ccae610bc4479209cd6e62bb91b0f76188.jpg' width=125 height=111></img> | <img src='https://valinecdn.bili33.top/HONKAI3-Durandal-Search/f1b9a456587638e488d93ccaa95dde59aef3af01.gif' height=100 width=100></img> |
| [HONKAI崩坏3 史丹](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/HONKAI3/HONKAI3-Stan) | [HONKAI崩坏3 爱酱](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/HONKAI3/HONKAI3-AIChan) | [HONKAI崩坏3 目标！幽兰黛尔](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/HONKAI3/HONKAI3-Durandal-Search) |
| <img src='https://valinecdn.bili33.top/HONKAI3-MEI/bf68423446465d396d3cbd8856882b5e9fb1c0c7.gif' width=120 height=120> | <img src='https://valinecdn.bili33.top/HONKAI3-NEWYEAR-2019/dc1a2b2032fad29373fe8460d4ad89ca848355a9.jpg' width=120 height=120> | ![](https://valinecdn.bili33.top/Tsuri-me-ju_mimi/10753793_key@2x.png) |
| [HONKAI崩坏3 芽衣的剑道修行](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/HONKAI3/HONKAI3-MEI) | [HONKAI崩坏3 2019新年](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/HONKAI3/HONKAI3-NEWYEAR-2019) | [つり目獣耳スタンプ(Sticker of the slant eyes & cat girl)](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Tsuri-me-ju-mimi) |
| <img src="https://valinecdn.bili33.top/Arcaea/184064198.png" style="zoom:50%;" /> | <img src="https://valinecdn.bili33.top/Mafumafu/199749477.png" style="zoom:50%;" /> |     ![](https://valinecdn.bili33.top/weibo/d_jiyan.png)      |
| [Arcaea](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Arcaea) | [動く！まふまふスタンプ（ねこ）Mafumafu Animation sticker (cat)](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/MafuMafu) | [微博原生表情包](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/weibo) |
| ![](https://valinecdn.bili33.top/Tieba-New/image_emoticon25.png) | <img src="https://valinecdn.bili33.top/Snow-Miku/3583066@2x.png" style="zoom:50%;" /> | <img src="https://valinecdn.bili33.top/Sweetie-Bunny/12311679.png" style="zoom:50%;" /> |
| [百度贴吧原生表情包](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Tieba) | [Snow Miku雪初音表情包（LINE）](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Snow-Miku) | [うさみみ少女（SWEETIE BUNNY）](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Sweetie-Bunny) |
| <img src="https://valinecdn.bili33.top/Little-Bad/我们一起做坏坏的事.jpg" style="zoom:50%;" /> | <img src="https://valinecdn.bili33.top/Yurui-Neko/029.png" style="zoom:50%;" /> | <img src="https://valinecdn.bili33.top/Cute-Emoji/010.png" style="zoom:50%;" /> |
| [小坏坏表情包](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Little-Bad) | [Yurui-Neko](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Yurui-Neko) | [Cute-Emoji](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Cute-Emoji) |
| <img src="https://valinecdn.bili33.top/Set667/032.png" style="zoom:50%;" /> | <img src="https://valinecdn.bili33.top/Marup/038.png" style="zoom:50%;" /> | <img src="https://valinecdn.bili33.top/Convenience-Store-Notes2/010.png" style="zoom:50%;" /> |
| [Set667](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Set667) | [Marup](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Marup) | [Convenience Store Notes2](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Convenience-Store-Notes2) |
| ![](https://valinecdn.bili33.top/Coolapk/coolapk_emotion_71.png) |      ![](https://valinecdn.bili33.top/aodamiao/01.gif)       |       ![](https://valinecdn.bili33.top/lengtu/04.gif)        |
| [Coolapk酷安](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Coolapk) | [aodamiao嗷大喵](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/aodamiao) | [lengtu冷兔](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/lengtu) |
|       ![](https://valinecdn.bili33.top/QQ/tuosai.gif)        |  ![](https://valinecdn.bili33.top/dingtalk/emotion_107.png)  | ![](https://valinecdn.bili33.top/Heybox/expression_heziji_22.png)![](https://valinecdn.bili33.top/Heybox/expression_cube_wa.png) |
| [QQ官方表情](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/QQ) | [钉钉官方表情](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/dingtalk) | [小黑盒表情包（包括盒娘和方块）](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Heybox) |
|   ![](https://valinecdn.bili33.top/Majotabi/367516718.png)   | ![](https://valinecdn.bili33.top/Arknights/coffeehouse_01.jpg) |    ![](https://valinecdn.bili33.top/KeQing/8uRU02Qn.png)     |
| [魔女之旅Majotabi（官方）](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Majotabi) | [明日方舟表情包](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/Arknights) | [刻晴表情包](https://github.com/GamerNoTitle/Valine-Magic/tree/master/Classification/KeQing) |

### 免责声明

本仓库内所有图片均来源于网络，仅供学习交流使用。若用户违反相关法律法规造成损失，将由用户自行承担，本仓库所有者和PR提交者不承担一切责任！

### 历史STAR

![](http://starchart.cc/GamerNoTitle/Valine-Magic.svg)

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FGamerNoTitle%2FValine-Magic.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FGamerNoTitle%2FValine-Magic?ref=badge_large)
