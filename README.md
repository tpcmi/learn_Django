## 创建表
```mysql
CREATE table myapp_users(
`id` int(10) UNSIGNED not null AUTO_INCREMENT,
`name` varchar(32) not null,
`age` tinyint(3) UNSIGNED not null DEFAULT'20',
`phone` varchar(16) DEFAULT NULL,
`addtime` datetime(6) not null,
PRIMARY KEY(`id`)
)ENGINE=INNODB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8
```