var express = require('express');
var app = express();

app.configure(function() {
    app.use(express.static('/static', __dirname + '/public'));
    app.engine('.html', require('jade').__express);
    app.set('view engine', 'jade');
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
    res.render('index', {title: 'cenas'});
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
