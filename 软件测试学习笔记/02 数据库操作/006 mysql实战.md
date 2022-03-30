# 1. mysql查询

## 1-1 基本查询

- 字段查询
- 条件查询 排序 分页 去重

## 1-2 条件查询 where

比较 通配 范围限定 子集限定 逻辑关系

## 1-3 聚合查询

Group by having

1. Sql 查询关键点 sql基础扎实，表结构熟悉。 分析查询需求的查询结果和限制条件。  
   结合表结构分析查询结果和限制条件。 如果查询结果和限制条件载同一个表，则为单表查询，否则多表查询。 结合sql基础和表结构，使用数据逻辑关系编写sql。

## 1-5 多表join查询和子查询

# 2. 索引

## 2-1 关键名字

1. 主键：表中记录的唯一标识符，不重复、且唯一。 单主键、组合主键
1. 外键：字段中的值来自于其他表的主键

## 2-1 索引 加速表查询

1.索引原理
索引是一个排序的列表，存储着索引的值和包含这个值的数据所在行的物理地址，在数据十分庞大的时候，索引可以加快查询的速度，这是因为使用索引后可以不用扫描全表来定位某行的数据，而是先通过索引表找到该行数据对应的物理地址然后访问相应的数据。
优势：可以快速检索，减少I/O次数，加快检索速度；根据索引分组和排序，可以加快分组和排序；
劣势：索引本身也是表，因此会占用存储空间，一般来说，索引表占用的空间的数据表的1.5倍；索引表的维护和创建需要时间成本，这个成本随着数据量增大而增大；构建索引会降低数据表的修改操作（删除，添加，修改）的效率，因为在修改数据表的同时还需要修改索引表；

## 2-2 索引的分类：

- 主键索引：不允许重复，不允许空值；
- 唯一索引：用来建立索引的列的值必须是唯一的，允许空值；
- 普通索引：用表中的普通列构建的索引，没有任何限制；
- 全文索引：用大文本对象的列构建的索引；
- 组合索引：用多个列组合构建的索引，这多个列中的值不允许有空值。

## 2-3 索引使用策略：

- 主键自动建立唯一索引；
- 经常作为查询条件在WHERE或者ORDER BY 语句中出现的列要建立索引；
- 作为排序的列要建立索引；
- 查询中与其他表关联的字段，外键关系建立索引；
- 用于聚合函数的列可以建立索引，例如使用了max(column_1)或者count(column_1)时的column_1就需要建立索引。

## 2-4 索引失效场景：

- 在组合索引中不能有列的值为NULL，如果有，那么这一列对组合索引就是无效的。
- LIKE操作中，'%aaa%'不会使用索引，也就是索引会失效，但是‘aaa%’可以使用索引(分情况),其它通配符同样，也就是说，在查询条件中使用正则表达式时，只有在搜索模板的第一个字符不是通配符的情况下才能使用索引。
- 在索引的列上使用表达式或者函数会使索引失效，例如：select * from users where YEAR(adddate)<2007，将在每个行上进行运算，这将导致索引失效而进行全表扫描，因此我们可以改成：select *
  from users where adddate<'2007-01-01′。
- 在查询条件中使用不等于，包括<符号、>符号和！=会导致索引失效。特别的是如果对主键索引使用!=则不会使索引失效，如果对主键索引或者整数类型的索引使用<符号或者>符号不会使索引失效 。
- 在查询条件中使用IS NULL或者IS NOT NULL会导致索引失效。
- 字符串不加单引号会导致索引失效。更准确的说是类型不一致会导致失效，比如字段email是字符串类型的，使用WHERE email=99999 则会导致失败，应该改为WHERE email='99999'。
- 在查询条件中使用OR连接多个条件会导致索引失效，除非OR链接的每个条件都加上索引，这时应该改为两次查询，然后用UNION ALL连接起来。
- 尽量不要包括多列排序，如果一定要，最好为这队列构建组合索引；

# 3. explain介绍

使用EXPLAIN关键字可以模拟优化器执行SQL查询语句，从而知道MySQL是如何处理你的SQL语句的。分析你的查询语句或是表结构的性能瓶颈 。

- id：相同，执行顺序由上至下 ；不同，如果是子查询，id的序号会递增，id值越大优先级越高，越先被执行。
- select_type： 表示select的类型；
    - SIMPLE 代表简单表，不用表连接或子查询，
    - PRIMRY 主查询（外层查询），
    - UNION中的第二个或者后面的查询语句，SUBQUERY 子查询中的第一个SELECT；
- table：输出结果集的表；
- ref：显示索引的哪一列被使用了，如果有可能是一个常数，哪些列或常量被用于查询索引列上的值；
- possible_keys：查询中可能用到的索引；
- key：查询中实际用到的索引；
- key_len：索引的长度；
- rows： 扫描的行数；
- type：访问类型 下面几种： 下面的值，从左到右，性能由最差到最好 ALL,index,range,ref,eq_ref,const,system,NULL ALL:全表扫描 index:索引全扫描 range: 索引的范围扫描
  用于<,<=,>,>=,between等操作 ref:使用非唯一索引扫描或者唯一索引的前缀扫描； eq_ref:使用唯一索引扫描，多表链接中使用primary key或 unique key作为关联条件； const/system:
  单表中只有一个匹配行，查询速度快，根据主键或唯一索引进行的查询； NULL:mysql不用访问表或者索引，直接能够得到结果；
- Extra
    - Using filesort：说明mysql会对数据使用一个外部的索引排序，而不是按照表内的索引顺序进行读取。MySQL中无法利用索引完成的排序操作称为“文件排序”。
    - Using temporary：使用了用临时表保存中间结果，MySQL在对查询结果排序时使用临时表。常见于排序order by和分组查询group by。
    - Using index：表示相应的select操作中使用了覆盖索引（Covering Index），避免访问了表的数据行，效率不错。如果同时出现using where，表明索引被用来执行索引键值的查找；如果没有同时出现using
      where，表明索引用来读取数据而非执行查找动作。
    - Using join buffer：表明使用了连接缓存,比如说在查询的时候，多表join的次数非常多，那么将配置文件中的缓冲区的join buffer调大一些。

**总结**：

1. EXPLAIN不会告诉你关于触发器、存储过程的信息或用户自定义函数对查询的影响情况
2. 部分统计信息是估算的，并非精确值
3. 在5.6以及以后的版本中，除过select，其他比如insert，update和delete均可以使用explain查看执行计划
   ![[00004.png]]
   ![[00005.png]]
   ![[00006.png]]
   ![[00007.png]]
   ![[00008.png]]
   ![[00009.png]]
   ![[00010.png]]
   ![[00011.png]]

# 事物

1. ACID (原子性 Atomicity、一致性 Consistency、隔离性 Isolation、持久性 Durability)
2. 隔离性：包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）。
3. 执行事物
    - begin：开始一个事务
    - rollback：事务回滚
    - commit：事务提交
      ![[00012.png]]

# 4. 存储过程

存储过程是一种在数据库中存储复杂程序，以便外部程序调用的一种数据库对象，目的是为了完成特定功能的SQL语句集，经编译创建并保存在数据库中，用户可通过指定存储过程的名字并给定参数(需要时)来调用执行。 数据库 SQL
语言层面的代码封装与重用。
`drop procedure if exists test;`
`delimiter ;;  #将语句的结束符号定义为;;(可以是自定义，比如临时改为两个$$)`
`create procedure test()`
`begin`
`declare i int;`
`declare s2 varchar(100);`
`set i=2041;`
`set s2='你好';`
`while(i<=2060)do`
`insert into hogwarts_user4 values(i,s2, i);`
`set i=i+1;`
`end while;`
`end;;`
`delimiter ; #将语句的结束符号恢复为分号`
`call test();  #调用存储过程`

1. 存储过程与函数的区别 存储过程：依赖于数据库，是SQL操作集的封装 call procedue name(@in, @out)
   函数：对基本数据做处理，可用于增强sql语句 select max(age) from table;
2. 测试存储过程
    1. 可以把存储过程当成普通的函数对待，使用单元测试理念
    2. 输入
    3. 为入参设置等价类测试数据
    4. 为引用的表构造测试数据
    5. 输出
    6. 断言出参
    7. 断言被写到的表内容

# 5.日志

## 5-1 统计日志

1. generic log：所有的sql查询log
2. slow log：超过预设的long_query_time阈值的sql记录

## 5-2 使用log-日志输出

❖show variables like 'log_output'; ❖show variables like '%query%' ; ❖show variables like '%_log%';

❖SHOW CREATE TABLE mysql.general_log; ❖SET GLOBAL general_log = 'ON';

❖SHOW CREATE TABLE mysql.slow_log; ❖SET GLOBAL slow_query_log = 'ON';

❖SET long_query_time = 0.01; show variables like '%long_query%';
![[00013.png]]
![[00014.png]]
❖SET GLOBAL slow_query_log = 'ON'; ❖set GLOBAL log_output = 'table'; ❖SET long_query_time = 0.01;

❖SELECT * FROM employees.employees LIMIT 2000; ❖SELECT * FROM mysql.general_log; ❖SELECT * FROM mysql.slow_log;
![[00015.png]]

# 6. 备份

❖dump：mysqldump ❖load：source ❖主从备份：bin log

# 7. 数据库面试知识点结构

- 数据定义：DDL
- 数据类型：常见数字类型、字符串类型（varchar）等
- 关系定义：主键、外键、索引
- 表结构修改：alter
- sql基本查询知识：DML
    - 条件查询
    - 分页查询
    - 聚合查询
    - 更新符合条件数据
    - 删除符合条件数据
- sql的知识进阶：DML
- 连接（Join）查询：inner、left、right
- 事务：基本知识和作用
- 索引：价值与用途
- 存储过程：如何对存储过程进行测试
- 数据库使用经验
- 常见数据库：mysql、oracle、mongodb、redis
- 数据库备份与恢复：mysqldump、mysql
- 性能统计：执行计划、slow sql

# 8. mysql练习

# 8-1 单表练习:

❖1. 查询所有的部门信息 ❖2. 查询开发部门的部门信息(编号)
❖3. 查询所有在1998年入职的信息,按入职时间从早到晚排序 ❖4. 查询所有在1998年入职的信息,按入职时间从早到晚排序,只要当年前十个新入职的员工(只要第10到15个呢)
❖5. 练习题 查询1998年所有的工资信息,按工资从高到低排序,只要当年工资最高的前十个员工(只要第10到20个呢)
❖6. 公司抽奖，只有员工名称中含有Mary,就中奖了 ❖7. 公司抽奖，只有10025，10223，10252三位员工中奖了，需要查出这三位员工的姓名 ❖8. 公司抽奖，从工资表中所以的员工编号,并且只要编号以23结尾(含有25)
或含有25的员工工号 ❖9. not用法 ❖10. 统计下员工入职以来，调薪次数有17次以上的员工编号 ❖11. 练习题 统计下员工入职以来，调薪次数有17次以上的员工编号,且编号里含有25的所有员工编号信息 ❖12.
查询公司的最高/平均/总和/最低薪资

# 8-2 多表练习：

1. 查询Development部的所有员工信息(所有信息)
   `SELECT   *
   FROM   dept_emp de LEFT JOIN departments deps ON de.dept_no = deps.dept_no WHERE deps.dept_name = 'Development’;`
   `SELECT   *
   FROM   dept_emp WHERE   dept_no IN (
     SELECT   dept_no   FROM   departments   WHERE   dept_name = 'Development'   );`
2. 查询Development部的工资最高的前十位员工信息
   `SELECT
   *
   FROM dept_emp de LEFT JOIN departments deps ON de.dept_no = deps.dept_no LEFT JOIN salaries saa ON de.emp_no = saa.emp_no WHERE deps.dept_name = 'Development' ORDER BY saa.salary DESC LIMIT 10;`
3. 取出部门的历任管理者
   `SELECT * FROM     departments d,     dept_manager m WHERE d.dept_no = m.dept_no;`
4. 计算各个部门的平均工资并排序，给出平均工资、部门名称
   `SELECT      AVG(salary) a, dept_emp.dept_no, departments.dept_name FROM     salaries         LEFT JOIN     (dept_emp, departments) ON dept_emp.emp_no = salaries.emp_no         AND departments.dept_no = dept_emp.dept_no GROUP BY dept_no ORDER BY a DESC;`