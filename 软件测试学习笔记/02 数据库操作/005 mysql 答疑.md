# 1. mysql 搭建

		`Docker run \
		-name mysql \
		-v $PWD/mysql:/var/b/lib/mysql \
		-p 3306:3306 \
		-e MYSQL_ROOT_PASSWORD=hogwarts \
		-d mysql5.7`

# 2. 练习地址

练习环境：
[http://sql.testing-studio.com:3080](http://sql.testing-studio.com:3080) python_12 python_12 练习数据：
[https://github.com/datacharmer/test_db](https://github.com/datacharmer/test_db)
本地测试数据导入：进入sql文件所在目录，执行
`Mysql -h 127.0.0.1 -u root -p < employees.sql`

# 3. sql分类

![[00002.png]]

# 4. join类型

![[00003.png]]

# 5. navicat对比表数据

1. 不同数据库表对比，表同步
2. 不同数据库表数据对比，数据同步
