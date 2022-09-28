# affspeedchanger
>arcaea谱面变速器，啊这还没想好，有一说一，等我有空了再做吧我寻思。

##总体来说
估计使用python写个变速脚本，用于arcaea游戏的自制谱面，然后使用一个整合可以输出一整个文件夹

to-do列表：
- songlist.json的生成器或者变速器, (主要就是bpm_base这个东西可以改下)
- sox开源音频处理，顺便整合一下.ogg文件，（这还需要ffmpeg吗？）
- 文件整合，包括文件夹和新文件的输出
- UI界面（？？）

Misc.东西:
```
        └── songs/
            └── song_id/
                ├── 谱面0.aff
                ├── 谱面1.aff
                ├── 谱面2.aff
                ├── base.ogg
                ├── base.jpg
                ├── base_256.jpg
                ├── 3.jpg (optional)
                └── 3_256.jpg (optional)
```
songlist可能不包括：
- idx字段，除非在私服会在linkplay用到
- remote_dl同理，离线私服不会用到
- byd_local_unlock好像就不用填，可以在离线解锁byd的arc壳子里直接启用byd谱面
- audioOverride & jacketOverride，hmm我寻思没啥用
