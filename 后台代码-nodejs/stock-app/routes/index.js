var express = require('express');
var router = express.Router();
const connection = require('../db/dbtest');
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});
/*得到账户密码*/
router.post('/login',function(req,res){
  console.log('sucessful') //处理请求和响应
  const {username,password}=req.body;
  connection.query(`select password from user_info where username=${username}`,function(error,results){
    if(error){
      console.log('查询失败');
      res.send({code:0,msg:'账号或密码错误'})
      return
    }
    if(results){
    if(results[0].password==password){
      res.send({code:1,msg:'登陆成功'})
    }
    else{
      res.send({code:0,msg:'账号或密码错误'})
    }
  }
  else{
    res.send({code:0,msg:'账号或密码错误'})
  }
  })
})
/*新增关注列表*/
router.post('/guanzhu',function(req,res){
  console.log('sucessful') //处理请求和响应
  const {username,daima}=req.body;
  connection.query(`update user_info set id=concat(id,',${daima}') where username = ${username}`,function(error,results){
    if(error){
      throw(error);
    }
  else{
    res.send({code:1,msg:'插入成功'})
  }
  })
})
/*删除（通过全体更新的方式）关注列表*/
router.post('/del',function(req,res){
  console.log('sucessful') //处理请求和响应
  const {username,id}=req.body;
  connection.query(`update user_info set id=replace(id,',${id}','') where username = ${username}`,function(error,results){
    if(error){
      throw(error);
    }
  else{
    res.send(results)
  }
  })
})
/*取消关注*/
router.post('/delguanzhu',function(req,res){
  console.log('sucessful') //处理请求和响应
  const {username,daima}=req.body;
  const pattern = new RegExp('(,'+daima+')|'+'('+daima+',)'+'|'+daima)
 var ids ={};
  connection.query(`select id from user_info where username=${username}  `,function(error,ids){
    if(error){
      throw error;
    }
    else{
      console.log('succesful!');
      console.log(ids[0].id);
      var str = ids[0].id.replace(pattern,'')
      console.log(str);
      res.send(ids);
    }
  }
)
console.log(ids)
  // connection.query(`update user_info set id=replace(id,'${pattern},','') where username = ${username}`,function(error,results){
  //   if(error){
  //     throw(error);
  //   }
  // else{
  //   res.send({code:1,msg:'删除成功'})
  // }
  // })
})
/*获取登录用户信息*/
router.get('/myid',function(req, res){
  const username = req.query.username;
  connection.query(`select id from user_info where username=${username}  `,function(error,results){
    if(error){
      throw error;
    }
    else{
      console.log('succesful!');
      res.send(results);
    }
  }
)})
/*获取关注列表*/
router.post('/mylist',function(req, res){
  const {idList}=req.body;
  connection.query(`select * from  stocktest2 where daima in (${idList})  `,function(error,results){
    if(error){
     throw error;
    }
    else{
    
      res.send(results);
    }
  }
)

})
/*得到股票信息*/
router.get('/stock',function(req, res){
  connection.query(`select * from stocktest2  `,function(error,results){
    if(error){
      throw error;
    }
    else{
      console.log(typeof(results));
      res.send(results);
    }
  }
)})
/*得到港股信息*/
router.get('/hk',function(req, res){
  connection.query(`select * from stocktestforhk  `,function(error,results){
    if(error){
      throw error;
    }
    else{
      console.log(typeof(results));
      res.send(results);
    }
  }
)})
/*得到美股信息*/
router.get('/us',function(req, res){
  connection.query(`select * from stocktestforus  `,function(error,results){
    if(error){
      throw error;
    }
    else{
      console.log(typeof(results));
      res.send(results);
    }
  }
)})
/*得到股指信息*/
router.get('/index',function(req, res){
  connection.query(`select * from indexst `,function(error,results){
    if(error){
      throw error;
    }
    else{
      console.log(typeof(results));
      res.send(results);
    }
  }
)})
/*用户注册路由*/
router.post('/register',function(req,res){
  console.log('sucessful') //处理请求和响应
  const {username,password}=req.body;
  if(username == '20161022'){
    res.send({code:0,msg:'duplicate'})
  }
  if(username == ''){
    res.send({code:0,msg:'null'})
  }
  const id ='0,0';
  connection.query(`insert into user_info (username,password,id)values('${username}','${password}','${id}')`,function(error,results){
    if(error){
      console.log('duplicate!');
    }
  else{
    res.send({code:1,msg:'yes'});
  }
  })
})
module.exports = router;
