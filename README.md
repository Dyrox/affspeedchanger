
# Arcaea谱面变速器


> 适用于[Arcaea](https://arcaea.lowiro.com/en)游戏谱面文件的变速脚本

## 功能
支持谱面语句类型：
- Tap 地键
- Hold 长条
- Arc & ArcTap 蛇和天键
- Timing 语句
- Timinggroup 语句
- Scenecontrol 语句（支持hidegroup和enwidenlanes，enwidencamera）
- 自动生成变速过的base.ogg
- 自动根据songid生成一件文件夹（包括谱面，歌曲封面，变速音频）

## 其他

- 目前支持到游戏 v4.1.0 版本的所有官方谱面。暂不支持愚人节谱面，不过要做也挺快的，主要我懒（
- 有简单的GUI页面可以选择谱面2.aff文件，但是调整倍速还是得自己在代码里调

### to-do列表：
- [x] songlist.json的生成器或者变速器, (主要是bpm_base参数)
- [x] sox开源音频处理，顺便整合一下.ogg文件
- [x] 文件整合，包括文件夹和新文件的输出
- [x] UI界面（？？）

