module.exports = function (){
    'use strict';
    var Backbone = require('backbone');
    return Backbone.Collection.extend({
        url: '/api/sections/',
        model: Backbone.Model.extend({
            url: '/api/sections/'
        })
    });
};
