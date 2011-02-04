var mustache = require('mustache');
var fs = require('fs');

var mustache_view = {
    compile: function (template, options) {
        layout = fs.readFileSync('./views/layout.html', 'utf-8');
        if (typeof template == 'string') {
            return function(options) {
                options.locals = options.locals || {};
                options.partials = {content: template};
                if (options.body) // for express.js > v1.0
                    locals.body = options.body;
                return mustache.to_html(
                    layout, 
                    options.locals, 
                    options.partials
                );
            };
        } else {
            return template;
        }
    },
    render: function (template, options) {
        template = this.compile(template, options);
        return template(options);
    }
};

module.exports = mustache_view;
