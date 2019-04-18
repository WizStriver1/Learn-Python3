# 实现Flask + Nginx

> 网络上找了很多Nginx + flask的方案，但是他们之间的通讯都是基于uWSGI的，但是这个东西居然不能在windows中安装，遗憾啊。所以遨游Internet之后，最后锁定了tornado的方案

- tornado实现和Flask通讯
- Nginx转发客户端请求，发送给tornado
- python应用托管于tornado