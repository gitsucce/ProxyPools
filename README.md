# ProxyPools
快速、简便获取免费、高可用性代理IP
ProxyPool 旨在快速、便捷的给用户提供免费代理IP，直接访问API接口即可获取到高可用性的代理IP地址。

# 关于 ProxyPool：

## 使用的相关技术
* Python3
* Flask
* Redis
* 爬虫
* 异步IO
* 前端
* ...
## Q & A
Q: 如何获取代理IP？
A: 直接访问/random接口即可。

Q: 获取源在哪？
A: 从11个免费的代理IP网站中提取

Q: 有没有好用的图形界面工具？
A: 没有

Q: 怎么才能看到具体实现细节？
A: 前往 Github项目源码

Q: 有多少代理池？
A: 50000个

Q: 获取的代理IP能用吗？
A: 使用redis的有序集合，对每个代理IP设置权重，实时检测，保证高可用性。

Q: 我还有其它问题怎么办？
A: 发送邮件到admin@w2n1ck.com
