# rent-telegram-bot
> 使用`Github Actions` 定时推送租房信息到指定的电报机器人，数据来自[租房搜索助手](http://uz.yurixu.com/)


## 效果图：
![example.jpeg](images/example.jpeg)

## 如何使用

-  `fork` 本项目
- 在项目设置中写入两个 `Github Action Secrets` , 分别是 `BOT_TOKEN` 电报机器人 `token` , 以及 `CHAT_ID` 需要推送的频道 `ID`
- 按照自己的需求填充 `config.json`
  - 其中 `filter` 为关键词数组，做包含匹配
  - `params`为向 [租房搜索助手](http://uz.yurixu.com/) 发送查询请求的参数, 可以直接抓包拿到
- 按照自己的需求修改 `.github/workflow/main.yaml` 中的 `cron` 字段
