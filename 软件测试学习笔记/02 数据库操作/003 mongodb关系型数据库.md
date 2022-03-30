# 1. 关系型数据库与非关系型数据库

## 1-1 关系型数据库：

mysql、oracle、sqlserver、access等

- 使用sql机构化语言
- 存储在磁盘中，读写慢
- 保持ACID，难扩展

## 1-2 非关系型数据库：

Nosql - NOT ONLY SQL

- key：value型
- CAP ->BASE 一致性Consistency，所有节点在统一时间具有相同的数据 可用性Availability，保证每个请求无论成功或者失败都具有相应 分割容忍 Partition
  tolerance，系统中任意信息的丢失或者失败不会影响系统的继续运作 三者不可同时结合使用，可以两两结合使用
- 没有标准化
- 有限的查询功能

# 2. mongodb介绍

- 非关系型数据库nosql
- 文档存储：类json格式
- 有机会对字段创建索引，实现关系数据库

# 3. 下载与安装

# 4. 使用与操作

1. 配置数据库目录 运行mongodb服务器：
   `mongod -dbpath XXX`
   连接mongodb：
   `mongo`
2. 删除数据库 查看数据库
   `show dbs`
   切换数据库
   `use demo1`
   插入一条数据
   `db.demo1.insert({"name":"小红"})`
   删除数据库
   `db.dropDatabase()`
3. 集合 创建集合
   `db.creatCollection('collection1')`
   查看集合
   `show collections`
   删除结合
   `db.coll.drop()`
4. 插入文档,mongo会自动创建集合
   `db.collectionDemo.insert({"name":"hello"})`
   查看插入的集合
   `db.collectionDemo.find().pretty()`
   插入复杂文档
   `document=({`
   `title: 'MongoDB',`
   `Tags: ['mongodb','datasource','NoSql']`
   `})`
   `db.collectionDemo.insert(document)`
   ![[00001.png]]
   修改文档
   `格式：db.collection.update(`
   `<query>,`
   `<update>,`
   `{`
   `upsert:<boolean>,`
   `multi:<bealean>,`
   `writeConcern:<document>`
   `}`
   `)`
   可选选项：
    - upsert：如果不存在update的记录，是否插入，默认false
    - Multi：把按条件条件差出来的数据全部更新，默认false
    - writeConcern：抛出异常的级别
    - update数据是整条修改，未修改的字段会消失 修改文档
      `db.coll.update({'name':"xiaohong"},`
      `{'name':"abc"})`
      修改多个文档
      `db.coll.update({'name':"xiaohong"},`
      `{$set:{'name':"abc"}},`
      `{multi:true})`
      删除文档 删除单个文档
      `db.col.remove({'name':"xiaohong"},1)`
      删除多个文档
      `db.col.remove({'name':"xiaohong"})`
      修改操作符
    - $inc

      `{$inc:{field:value}}` 对某个字段field加上value
      `示例 db.student.update(name:'xiaohua'),{$inc:{score:50}}`
    - $set

      `{$set:{field:value}}` 对某个字段field设为value
      `示例 db.student.update(name:'xiaohua'),{$set:{score:50}}`
    - $unset

      `{$unset:{field:value}}` 对某个字段field删除
      `示例 db.student.update(name:'xiaohua'),{$unset:{score:10}}`
    - $push

      `{$push:{field:value}}` 对某个字段field追加value值,field只能是数组类型，如果field类型不存在，则会自动插入一个数组类型
      `示例 db.student.update(name:'xiaohua'),{$push:{"ailas":"xiaozhang"}}`
    - $rename

      `{$rename:{old_field:new_field}}` 对某个字段field追加进行重新命令
      `示例 db.student.update(name:'xiaohua'),{$rename:{"name":"xiaozhan"}}`
	