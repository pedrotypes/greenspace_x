var express = require('express');
var app = express();
var fs = require('fs');

// RabbitMQ
var amqp = require('amqp');
var connection = amqp.createConnection({host:'127.0.0.1'});
var rpc = new (require('./amqprpc'))(connection);
// --

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

var fleetSchema = mongoose.Schema({
    position: {
        type: mongoose.Schema.ObjectId,
        ref: 'Base'
    },
    destination: {
        type: mongoose.Schema.ObjectId,
        ref: 'Base'
    },
    eta: Number,
    eta_total: Number
}, { collection: 'fleet'});
var Fleet = mongoose.model('Fleet', fleetSchema);


app.get('/', function(req, res) {
    fs.readFile(__dirname + '/public/index.html', 'utf8', function(err, indexHtml) {
        res.send(indexHtml);
    });
});
app.get('/map', function(req, res) {
    fs.readFile(__dirname + '/public/map.html', 'utf8', function(err, mapHtml) {
        res.send(mapHtml);
    });
});
app.get('/fleet', function(req, res) {
    // There should be a single fleet ATM
    Fleet
        .findOne()
        .populate('position')
        .populate('destination')
        .exec(function(err, doc) {
            res.send(doc);
        });
});
app.get('/fleet/move/:id', function(req, res) {
    Fleet.findOne(function(err, doc_fleet) {
        Base.findById(doc_fleet.position, function(err, doc_position) {
            Base.findById(req.param('id'), function(err, doc_base) {
                // This logic should be offloaded to the backend
                var delta = {
                    x: doc_position.x - doc_base.x,
                    y: doc_position.y - doc_base.y
                };

                distance = Math.sqrt(Math.pow(delta.x, 2) + Math.pow(delta.y, 2));
                eta = Math.round(distance);

                doc_fleet.destination = new Base(doc_base);
                doc_fleet.eta = eta;
                doc_fleet.eta_total = eta;
                doc_fleet.save();
            });
            res.send('ok');
        });
    });
});

app.get('/rabbit', function(req, res) {
    rpc.makeRequest('greenspace_fleet', {first_name: 'Leroy', last_name: 'Jenkins'}, function(err, response){
      if(err)
        res.send(err);
      else
        res.send(response.data.toString());
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
