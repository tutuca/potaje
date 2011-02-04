var express = require('express');
var mustache_view = require('./mustache_view');
var config = require('./config');
var app = express.createServer();

app.configure(function() {
    app.use(express.methodOverride());
    app.use(express.bodyDecoder());
    app.use(app.router);
    app.register(".html", mustache_view);
    app.set("view options", {layout: false});
    app.use(express.staticProvider(__dirname + '/media'));
    app.use(express.errorHandler({
        dumpExceptions:true, 
        showStack:true
    }));
});

app.get('/', function(req, res){
    res.render(
        'index.html',
        {
            locals: {
                trabajo: [
                    {nombre: 'Prueba'},
                    {nombre: 'Prueba2'},
                    {nombre: 'Prueba2'},
                ]
        }
    });
});

app.listen(3000)
