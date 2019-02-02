

var express = require('express');
var bodyparser = require('body-parser');
var connection = require('./connection');
var routes = require('./routes');
var path = require('path');



var app = express();
app.use(express.static(path.join(__dirname, '/public')));
app.use(bodyparser.urlencoded({extended: true}));
app.use(bodyparser.json());
connection.init();
routes.configure(app);


var myLogger = function (req, res, next) {
  console.log('LOGGED')
  next()
}

app.use(myLogger)

var server = app.listen(8006, function() {
  console.log('Server listening on port ' + server.address().port);
});
