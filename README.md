# hoshinobot-user_block
hoshinobot插件，手动拉黑用户插件

使用说明：

  将.py放到HoshinoBot\hoshino\modules\botmanage目录下

指令：

  .block+小时数@用户1@用户2
  
    将@用户拉入机器人黑名单（指定时间内不响应被拉黑用户的指令）
    
    可以修改py文件增加拉黑时间上限（默认最高999小时，设置时间超过999也只拉黑999小时）
    
  .block0@用户1@用户2
  
    将@用户取消拉黑


  .blockuid+小时数@QQ号1@QQ号2
  
    将QQ号用户拉入机器人黑名单（指定时间内不响应被拉黑用户的指令）
    
  .blockuid0@QQ号1@QQ号2
  
    将QQ号用户取消拉黑


  .blockgid+小时数@群号1@群号2
  
    将群拉入机器人黑名单（指定时间内不响应被拉黑群内所有用户的指令）
    
  .blockgid0@群号1@群号2
  
    将群取消拉黑
注意：

  groupmaster下的anti_abuse.py的拉黑会覆盖该插件的用户拉黑。如不想受影响可以手动注释anti_abuse.py代码。
  
  *取消拉黑可以取消被anti_abuse.py拉黑的用户。
