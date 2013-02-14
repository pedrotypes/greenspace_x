var express = require('express');
var app = express();

app.get('/', function(req, res) {
    var body = 'STAR GAME HOLLAAAA';
    res.send(body);
});

port = 80;
app.listen(port);
console.log('Listening on port ' + port);
