# hoshinobot-user_block
hoshinobot插件，手动拉黑用户插件

使用说明：将.py放到HoshinoBot\hoshino\modules\botmanage目录下

指令：
.block+小时数@用户1@用户2
将@用户拉入机器人黑名单（指定时间内不响应被拉黑用户的指令）
.block0@用户1@用户2
将@用户取消拉黑

注意：
groupmaster下的anti_abuse.py的拉黑会刷新你设置的拉黑时间。
取消拉黑可以取消被anti_abuse.py拉黑的用户。
