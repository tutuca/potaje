module.exports = function (){
    'use strict';
    var Backbone = require('backbone');
    return Backbone.View.extend({
        el: $("nav ul"),
        model: Sections,
        //template: new AlbumTemplate(),
        initialize: function () {
            require('slick-carousel');
            this.listenTo(this.model, "change", this.render);
        },
        render: function () {
            var content = '' ;//this.template(this.model.attributes);
            //this.$el.html(content).slick();

            return this;
        },
        show: function (event) {
        }
    });
};
