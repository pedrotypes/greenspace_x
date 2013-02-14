var express = require('express');
var app = express();
var fs = require('fs');

app.configure(function() {
    app.use('/static', express.static(__dirname + '/public'));
});

var mongoose = require('mongoose');
mongoose.connect('localhost', 'stargame');
var db = mongoose.connection;

var baseSchema = mongoose.Schema({
    name: String,
    size: Number,
    money: Number,
    x: Number,
    y: Number
}, { collection: 'base'});
var Base = mongoose.model('Base', baseSchema);


app.get('/', function(req, res) {
    fs.readFile(__dirname + '/public/index.html', 'utf8', function(err, indexHtml) {
        res.send(indexHtml);
    });
});

app.get('/bases', function(req, res) {
    Base.find(function(err, bases) {
        var out = [];

        bases.forEach(function(doc) {
            out.push(new Base(doc));
        });

        res.send(out);
    });
});

port = 80;
app.listen(port);
console.log('Listening on port ' + port);
