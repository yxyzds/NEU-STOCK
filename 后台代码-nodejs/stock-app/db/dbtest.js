const mysql = require('mysql');
var connection = mysql.createConnection({
    host: '127.0.0.1', //主机
    user: 'root',     //数据库用户名
    password: '19980729',     //数据库密码
    port: '3306',       
    database: 'users', 
    multipleStatements: true//数据库名称
});
module.exports = connection;
  