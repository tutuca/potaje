var $ = require('jquery');
$(function() {
    'use strict';
    var _ = require('underscore'),
        Backbone = require('backbone'),
 
    var Router = Backbone.Router.extend({
        rutes: {
            'home': 'home',
            'album/:album_id': 'album'
        },
        home: function ( ) {
        },
        album: function (album_id) {

        }

    });
    var app_router = new Router();
    app_router.on('initialize:after', function() {
        return Backbone.history.start({
            pushState: true,
            hashChange: false
        });    
    });

});
