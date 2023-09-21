var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index');
});

/* GET home page. */
router.get('/contacts', function(req, res, next) {
  res.render('contacts');
});

/* GET home page. */
router.get('/team', function(req, res, next) {
  res.render('team');
});

/* GET home page. */
router.get('/recipes', function(req, res, next) {
  res.render('recipes');
});

module.exports = router;
