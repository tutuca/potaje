var $ = require('jquery');

$(function() {
    'use strict';

    var Backbone = require('backbone'),
        app, Router;

    Router = Backbone.Router.extend({
        rutes: {
            'home': 'home',
            'album/:album_id': 'album'
        },
        home: function ( ) {
        },
        album: function (album_id) {

        }

    })

    app = {
        router : Router,
        init : function () {
            new this.router();
            Backbone.history.start({
                pushState: true,
                hashChange: false
            });
        }
    };

    return app.init();
});
