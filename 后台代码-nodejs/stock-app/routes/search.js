var express = require('express');
var router = express.Router();
const connection = require('../db/dbtest');
router.get('/search',function(req,res){
    connection('select * from user_info',function(error,results){
        console.log(results)
    })
})

module.exports = router;
