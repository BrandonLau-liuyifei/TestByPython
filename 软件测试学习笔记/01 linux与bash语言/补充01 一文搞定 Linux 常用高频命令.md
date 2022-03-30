# 干货 | 一文搞定 Linux 常用高频命令

原创 HJP 霍格沃兹测试学院  _2020-09-02 08:54_

收录于话题

# 测试开发2个内容

# 软件测试2个内容

# Linux / Shell 命令1个内容

# 测试面试真题汇总|霍格沃兹53个内容

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ervTCibwaujFMmyEicHU8owqZFtMe32on0icribXvpoXhXlGVJpgGGOVibRSTkxBKR9YP0B5vRy3XOBmw2CyTRSSDGw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> 本文为霍格沃兹测试学院优秀学员 HJP 的学习笔记，进阶学习文末加群。

#### 命令 cd

```
进入上级目录    cd ..进入当前用户主目录    cd ~进入上两级目录    cd ../..进入当前目录    cd .进入目录/etc/docker    cd /etc/docker
```

#### 命令 mv

```
移动一个文件夹（docker文件夹，移动到/root/file目录）    mv ~/docker/ /root/file移动一个文件（docker.txt移动到/root/file目录）    mv docker.txt /root/file当前目录docker.txt移动到/root/file目录，并重命名为docker0304.txt    mv docker.txt /root/file/docker0304.txt移动文件到上级目录    mv docker.txt ../一条命令，移动两个文件docker.txt jenkins.txt到目录/root/file    mv docker.txt jenkins.txt -t /root/file
```

#### 命令 cp

```
复制当前目录包docker.tar.gz到备份目录/root/bak    cp docker.tar.gz /root/bak复制文件夹docker到目录/root/file    cp -r docker/ /root/file
```

#### 命令 mkdir

```
新建一个文件夹mysql    mkdir mysql新建三个文件夹mysql1 mysql2 mysql3    mkdir mysql1 mysql2 mysql3新建一个多层级文件夹mysql/2019/0304    mkdir -p mysql/2019/0304
```

#### 命令 history

```
查看历史命令执行记录    history查看命令mkdir的历史执行记录    history | grep mkdir执行历史记录中序号为54的命令    !54
```

#### 命令 tail

```
实时刷新log    tail -f mysql.log实时刷新最新200条log    tail -200f mysql.log
```

#### 命令 tar

```
压缩一个文件docker.txt    tar -cvf docker.tar docker.txt压缩多个文件docker.txt jenkins.txt    tar -cvf all.tar docker.txt jenkins.txt压缩文件夹docker/    tar -cvf docker.tar docker/将当前目录所有jpg文件打包成jpg.tar    tar -cvf jpg.tar *.jpg将当期目录所有png文件打包成png.tar.gz    tar -zcvf png.tar.gz *.png解压jpg.tar    tar -xvf jpg.tar解压png.tar.gz    tar -zxvf png.tar.gz
```

#### 命令 ls

```
列出当期目录中所有子目录和文件    ls列出目录下的所有文件（包含隐藏文件）    ls -a列出文件的详细信息（包括权限、所有者、文件大小等）    ls -l列出当前目录中所有以"docker"开头的详细内容    ls -l docker*
```

#### 命令 ps

```
查看所有进程    ps -A查看java进程    ps -ef | grep java显示所有进程信息，包括命令行    ps -ef
```

#### 命令 top

```
显示进程信息    top监控每个逻辑cpu的状况    top，按1高亮显示当前运行进程    top，按b显示完整命令    top，按c退出top程序    按q
```

#### 命令 wget

wget 是一个下载文件的工具，对于 Linux 用户是必不可少的工具：

```
文件地址    假设为http://xxxx/xxx.png下载此文件    wget http://xxxx/xxx.png下载此文件，并存储为aaa.png    wget -o aaa.png http://xxxx/xxx.png后台下载此文件    wget -b http://xxxx/xxx.png
```

#### 命令 find

```
在/root/file目录及其子目录下面查找名字为docker.txt的文件    find /root/file/ -name docker.txt在当前目录及其子目录中查找任何扩展名为"ini"的文件    find . -name "*.ini"在/root/file目录下查找更改时间在5日以前的文件    find /root/file/ -mtime +5在/root/file目录下查找更改时间在3日以内的文件    find /root/file/ -mtime -3在/root/file目录下查找所有的目录    find . -type d在/root/file目录下查找所有的文件    find /root/file/ -type f在当前目录所有的普通文件中搜索docker这个词    find ./ -type f | xargs grep "docker"在当前目录，删除1天以内的所有东西    find ./ -mtime -1 -print | xargs rm -rf在当前目录，删除5天以前的所有东西（慎用！慎用！慎用！）    find ./ -mtime +5 -print | xargs rm -rf删除文件大小为0的文件    find ./ -size 0 | xargs rm -rf
```

#### 命令 rm（rm -rf慎用）

```
删除/root/file/目录下的docker.txt文件（系统会询问是否删除）    rm /root/file/docker.txt强行删除/root/file/目录下的docker.txt文件（系统不会询问是否删除）    rm -f /root/file/docker.txt删除/root/file/目录下的所有.log文件    rm -f /root/file/*.log删除/root/file/目录下的jenkins文件夹    rm -r /root/file/jenkins/强行删除/root/file/目录下的jenkins文件夹    rm -rf /root/file/jenkins/删除/root/file/目录下的所有内容    rm -rf /root/file/*
```

#### 文件操作命令

```
创建文件    touch docker.txt    vim docker.md    echo 'create file' > docker.ini    cp docker.txt dockercp.txt    ls > filelist.txt同时创建几个文件    touch docker.txt jenkins.txt同时创建1000个文件    touch mysql{0001..1000}.ini更改文件docker.txt时间为当前时间    touch docker.txt
```

#### 查看文件命令

```
命令提示    cat 从第一行开始显示    tac 从最后一行开始显示    more 一页一页显示    less 与more相同，但是可以往前翻页，推荐用less    head 只看头几行    tail 只看尾几行    nl 显示的时候，输出行号查看文件docker.txt的内容    cat docker.txt查看文件docker.txt前20行的内容    head -n 20 docker.txt查看文件docker.txt后30行的内容    tail -n 30 docker.txt显示文件docker.txt的第10行到第20行内容    head -n 20 docker.txt | tail -n 10倒序显示文件docker.txt前10行的内容    tac docker.txt | head -n 10显示文件docker.txt前10行的内容，并显示行号    nl docker.txt | head -n 10
```

#### 命令 yum & scp

假设当前服务器 ip 为 `192.168.1.2`：

```
从linux服务器192.168.1.1复制文件docker.txt到服务器192.168.1.2    scp root@192.168.1.1:/root/file/docker.txt /root/file从linux服务器192.168.1.1复制目录docker/到服务器192.168.1.2    scp -r root@192.168.1.1:/root/file/docker/ /root/file安装scp命令，假设是centos    yum install openssh-clients
```

#### 命令 clear & ifconfig & df & du

```
清屏    clear查看当前服务器ip    ifconfig查看当前服务器硬盘空间    df -h查看目录docker/所占用的空间    du -sh docker
```

#### 命令 vi/vim & chmod

```
vi/vim，推荐用vim    创建文件、编辑文件chmod    改变文件或目录的访问权限创建文件docker.md    vim docker.md更新文件内容为"this is a markdown file"    vim docker.md    按i，进入编辑模式    输入内容    按esc进入命令模式:wq保存退出将文件docker.md设为所有人可读    chmod +r docker.md将docker.md设为只有该文件的拥有者才可以执行    chmod u+x docker.md给文件docker.md设置所有权限    chmod 777 docker.md（或者chmod a=rwx docker.md）
```

#### 查看 Java 应用

```
jps -ml
```

#### 查看应用路径

```
pwdx pid
```

#### 查看所有 Java 应用路径

```
pid=$(jps -ml|awk '{print $1}');for i in $pid;do pwdx $i;done
```

#### 小结

本文列举了测试工程师最常用的 Linux／Shell 高频命令。对于任何一个命令的详细解释都可以使用 `–help` 查看使用帮助，如 `top –help`。对于英语水平较好的同学，可以使用 `man`
命令将其解释文档输出保存为一个文件，以便查阅，同样使用 top 举例，可以使用 `man top > top.txt` 保存其解释文档。

以上，期待大家一起交流探讨。

---



**推荐学习  
**

推荐霍格沃兹出品 **《测试开发实战进阶》课程，资深测试架构师、开源项目作者亲授 **BAT 大厂前沿最佳实践****。4 个月 20+ 项目实战强化训练，带你一站式掌握 BAT 测试开发工程师必备核心技能（**
对标阿里P6+，年薪50W+**）！学员**直推 BAT 名企测试经理**，普遍涨薪 50%+！

![图片](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)

🔥15 期热招中🔥

霍格沃兹测试学院凭过硬课程课程、超强服务实力和超高好评率成为「**腾讯课堂官方认证机构**」并荣获**「最受欢迎奖」（测试类目仅此一家）**！

![图片](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)

戳“阅读

原文”，提升自己的核心竞争力吧！

[阅读原文](https://mp.weixin.qq.com/s?__biz=MzU3NDM4ODEzMg==&mid=2247489970&idx=1&sn=3b0925d3fd56b2f155ba10f14c54a5dc&chksm=fd327b79ca45f26f56afce8e3687ff9b157286ae61a9909be4ffa6b6ba90a23901cdae17fb6b&scene=178&cur_album_id=1329497002148970497&rd2werd=1&key=58032826474225cbc6701d6164781e2a59c94917d0dec22c996f546feda27008df7de7ffa6d0ec252929459476e3b23f595a01aae99b19d9fb3fc8e64355a4120684b141437f5a7fa624652202088639dd430eede8cd347454cce12250a239ec6a788c4e398cd4529b3f93a15d11c0ad799c13a64661e03bca1c5a98c8276c9f&ascene=14&uin=MTg4NTg1MDQwMQ%3D%3D&devicetype=iMac+MacBookPro17%2C1+OSX+OSX+11.6+build(20G165)&version=13020110&nettype=WIFI&lang=zh_CN&fontScale=100&exportkey=AS2lLXf5QWAY11QEfc%2FcIDA%3D&pass_ticket=F5RK%2FaiyA%2F0eXF3cAdyVRBwjAXJTc1zqpsHsVDf%2BkhanaCiBWOiR3iUq%2FvLQIAoo&wx_header=0&fontgear=2.000000##)

阅读 3984

赞18在看8

写下你的留言

**精选留言**

- ![](http://wx.qlogo.cn/mmopen/rIv87mYKYE2t54Ujiam4RcsExQM7PWPvXLS4AibsLJ6A3b8WI55HaEeobwhPmYNOpfkI3LHWyjkicOQRnPnpII0sJBCeZIvPPhA/96)

  Joker'L

  置顶

  刚想自己总结一下，推送就来了，真省心

  ![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4ibUZwCibJfAV9yFx1jL6ZrMasHOUqTu7nN3ZgibPVLibTiaA/0)

  霍格沃兹测试学院

  (作者)

  1

  哈哈哈，老铁心心相印，双击 666！

- ![](http://wx.qlogo.cn/mmopen/rIv87mYKYE0EpicQonTdszVl6iboZZIkAov8o4LX4J9FsoDNocHfRJpia6C0FWtD6rRvvBbdao2BibT1Nib5CosjTFTAfh3btBVUu/96)

  思

  2

  少个Linux三剑客

  ![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4ibUZwCibJfAV9yFx1jL6ZrMasHOUqTu7nN3ZgibPVLibTiaA/0)

  霍格沃兹测试学院

  (作者)

  三剑客文章之前有推送过

- ![](http://wx.qlogo.cn/mmopen/Q3auHgzwzM4iaibeqW2Zms6aGbwzVkDkGRGK40ql0ygctJBq2WEdyZT8A3LJia7RszRE2du7ico4xu2UibMnvTV9icftl38EFZpEYafJtDLQEVF5o/96)

  张珊

  sql面试总结有吗

  ![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4ibUZwCibJfAV9yFx1jL6ZrMasHOUqTu7nN3ZgibPVLibTiaA/0)

  霍格沃兹测试学院

  (作者)

  1

  往期好像有发过 SQL 的面试文章，你搜搜看！

  ![](http://wx.qlogo.cn/mmopen/Q3auHgzwzM4iaibeqW2Zms6aGbwzVkDkGRGK40ql0ygctJBq2WEdyZT8A3LJia7RszRE2du7ico4xu2UibMnvTV9icftl38EFZpEYafJtDLQEVF5o/96)

  张珊

  1

  搜到啦，谢谢😜

- ![](http://wx.qlogo.cn/mmopen/w8gMgicHp6ec2jKaDCY5emHcibTz0Xn79ootVTFSpanWZFn8NWia2nTfWP3byBspLgjgiaEJz1TgbSjnVf5eU228YP5noITZic6bt/96)

  wuyong

  不错👍

  ![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4ibUZwCibJfAV9yFx1jL6ZrMasHOUqTu7nN3ZgibPVLibTiaA/0)

  霍格沃兹测试学院

  (作者)

  1

  转发推荐给更多小伙伴！

- ![](http://wx.qlogo.cn/mmopen/w8gMgicHp6eeI8Zf06Em0rdLxpic4DKDh59h5RWiaLhudx43wiblZP08fr0cQaiafMe1MYa0h6UeAt336mL9JkM6qGXqoFSjdicR30/96)

  (￢_￢)🌱

  没有找到三剑客的文章链接呢？

  ![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4ibUZwCibJfAV9yFx1jL6ZrMasHOUqTu7nN3ZgibPVLibTiaA/0)

  霍格沃兹测试学院

  (作者)

  有的，搜一下 三剑客

已无更多数据

：，。视频小程序赞，轻点两下取消赞在看，轻点两下取消在看