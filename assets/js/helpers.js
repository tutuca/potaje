/* Helpers */
function hexToRgb(hex) {
    /*
    * Expand shorthand form (e.g. "03F") to full form (e.g. "0033FF")
    * from http://stackoverflow.com/a/5624139/53468
    */
    'use strict';
    var shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
    hex = hex.replace(shorthandRegex, function(m, r, g, b) {
        return r + r + g + g + b + b;
    });

    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
}

function toRGBAString (color, a) {
    'use strict';
    if (!a) {a=1;}
    color = hexToRgb(color);
    return 'rgba('+color.r+','+color.g+','+color.b+','+a+')';
}

function viewport(){
    /*
    * Calculates the available surface on the client's window.
    * */
    'use strict';
    var e = window,
        a = 'inner';
    if ( !( 'innerWidth' in window ) ){
        a = 'client';
        e = document.documentElement || document.body;
    }
    var innerWidth = Math.max(e[a+'Width'], 580),
        innerHeight = Math.max(e[a+'Height'], 580);
    return { width : innerWidth , height : innerHeight };
}

function fit(selector, to, padding){

    var visible_height, visible_width,
        old_height, old_width,
        delta, landscape;
    padding = padding || 0;
    if (to) {
        visible_height = $(to).height() - padding;
        visible_width = $(to).width() - padding;
    } else {
        var vp = viewport();
        visible_height = vp.height - padding;
        visible_width = vp.width- padding;

    }
    $(selector).each(function() {
        var $el = $(this);
        old_width = $el.width();
        old_height = $el.height();
        landscape = old_width > old_height;
        if (landscape) {
            $el.css({
                width: Math.floor(visible_height / old_height * old_width),
                height: 'auto'
            });
        } else {
            $el.css({
                height: visible_height,
                width: 'auto'
            });
        }
        /* delta = (visible_width - $el.width())/2;
        $(this).css('margin-left', delta); */
    });

}

module.exports = {
    viewport,
    hexToRgb,
    toRGBAString,
    fit
};
