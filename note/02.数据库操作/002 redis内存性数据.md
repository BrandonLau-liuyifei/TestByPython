# 1. redis简介
1. 高性能的key-value数据库
2. 数据持久化，将内存中的数据存在在次盘中，重启可以加载
3. 同时提供list、set、zset、hash等数据结构的存储
4. 数据可以备份，master-slave模式数据备份
5. 高性能，读取速度110000次/s，写入81000次/s
6. 原子性操作，单个操作支持原子性，多个也支持事物，通过mulit和exec指令包裹的
7. 支持publish、subscribe，通知、key过期等特性。
# 2. redis安装部署
1. 下载redis安装包，解压
2. 命令行切换到解压后的目录中，执行
		`redis-server.exe redis.window.conf`
3. 报错creating server tcp listening socket 127.0.0.1:6379:bind:no error
		解决：停止服务中的redis服务
4. redis基本数据结构
	- String 二进制安全的，可以包含任何数据，如.jpg图片或者序列化对象，最大能存储512m。
	- Hash string 类型的key和value的映射表，特别适合用于存储对象：存储232 - 1键值对（40多亿）
	- List 按照插入顺序排序，可以添加元素至表头（左边）或者表尾（右边），可存储232 -1元素，每列可存储40多亿
	- Sorted Set 有序集合，每个元素都会关联一个double类型的分数，redis是通过分数来为集合中的成员进行从小到大的排序，zset的成员是唯一的，但分数score可以重复的。
# 3. redis基本使用
1. 连接redis：切换到redis目录，执行redis_cli.exe -h 127.0.0.1 -p 6379
	- `String: SET key member/GET key`
	- `Hash: HMSET key field1 "hello" field2 "world"/HGET/HGETALL key field1`
	- `List: 1push key member/1range key 0 10`
	- `Set: sadd key member/smembers key`
	- `Sorted Set: sadd key score member/ZRANGEBYSCORE key 0 1000`
# 4. 使用java连接redis