# 1. 数据库搭建与使用
## 1-1. 数据库搭建
1.  mysql安装
2.  直接解压压缩包
3.  My.ini 文件设置端口号、连结数量、服务端字符集
4.  环境变量配置
	windows：
		系统变量-配置mysql所在目录。
		环境变量-安装目录mysql的bin目录。
	Mac os 或着 linux：
		用户的目录下打开.bash_profile文件下，配置如下参数：
		`#mysql`
		`export PATH="$PATH":/usr/local/mysql/bin`
5.  初始化数据库
		进入数据库bin目录，执行
		`mysql --initialize --user=mysql --console`
		初始化命令，保存临时密码，启动mysql数据库服务器
		net start mysql
		登陆mysql
		`mysql -u -root -p，输入数据临时密码。`
6.  添加到服务
		`mysql - install`
7.  修改密码
		`alter user 'root''@''localhost' identified with by '新密码';`
## 1-2. navicat客户端使用
1.  使用nativecat客户段链接数据库，报错
		`client does`
		`Not support authentication protocol requested by server`
		执行下述语句解决：
		`use mysql;`
		`alter user 'root''@''localhost' identified with mysql_native_password by '新密码';`
		`flush privileges;`
2. nantivecat链接mysql
3. 新建数据库
		数据库名：数据库名
		字符集使用：utf8mb4 --UTF_8 Unicode
		排序规则：utf8mb4_general_ci
4. 命令行界面即cmd界面
		use 数据库名；
5. sql文件导入
		运行sql文件
6. sql文件导出
		转出sql文件 数据库或表
## 1-3. phpmyadmin操作
1.  phpMyAdmin介绍
		以php为基础，以web-bashe方式架构在网站主机上的mysql管理工具，让管理者使用web接口来管理数据库。
# 2. mysql表结构
1.  创建表
		`CREATE table `hogwarts_user` (
		`id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
		`name` VARCHAR(100) DEFAULT NULL COMMENT '名称', 
		PRIMARY KEY (`id`) USING BTREE
		) 
		ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 
		ROW_FORMAT=DYNAMIC COMMENT='霍格沃滋测试学院';`
2. 插入表数据
		`INSERT into hogwarts_user(`name`),values('');`
3. 删除表
		`DROP table hogwarts_user;`
# 3. mysql基础操作
# 4. mysql联合操作