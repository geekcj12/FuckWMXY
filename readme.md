瞎捣鼓的一个脚本，自用和学习性质。代码很烂，才疏学浅，欢迎大佬指点。

## Usage

可能每个学校的打卡题目都不太一样，手动打卡一次，使用`HttpCanary`抓包，把请求的json导出来，替换到`submit_json`变量。如果打卡题目变了，重新抓包替换即可。

本项目挂在服务器上运行，使用`crontab`设置定时任务。

自行更改路径。赋予sh的执行权限和创建一个每天零时零点执行的任务。

```
chomd +x start.sh
0 0 * * * /bin/sh /home/start.sh
```

