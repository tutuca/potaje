var $ = require('jquery');
$(function() {
    'use strict';

    var _ = require('underscore'),
        Backbone = require('backbone'),
        AlbumTemplate = require('./templates/album.hbs');

    var NavView = Backbone.View.extend({
         el: $("nav ul"),
         
    });
    var Album = Backbone.Model.extend({
        url: '/api/albums/',
    });
    var Albums = Backbone.Collection.extend({
        url: '/api/albums/',
        model: Album,
    });
    var AlbumView = Backbone.View.extend({
        el: $("nav ul"),
        model: Album,
        template: new AlbumTemplate(),
        initialize: function () {
            require('slick-carousel');
            this.listenTo(this.model, "change", this.render);
        },
        render: function () {
            var content = this.template(this.model.attributes);
            this.$el.html(content).slick();

            return this;
        },
        show: function (event) {
        }
    });
 
    var Router = new Backbone.Router.extend({
        rutes: {
            'home': 'home',
            'album/:album_id:': 'album'
        },
        album: function (album_id) {
            return new AlbumView();
        },
        home: function(){
        },
    });
 
    // Main entry point.    
    return Backbone.history.start({
        pushState: true,
        hashChange: false
    });
});
