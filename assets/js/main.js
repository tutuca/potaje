var selected,
    slickOptions = {
    dots: false,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    centerMode: true,
    variableWidth: true
};
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
function renderSection(){
    /*
    * Pjax callback funcion
    * */
    'use strict';
    if (selected){
        $('body').css({'overflow':'hidden'});
        $('nav').toggle('fade', 1000);

        $('.work a').not(selected).each(function(index){
            $(this).parent('article').toggle('fade', 1500*index);
        });
        return $('#slides').slick(slickOptions);
    }
}
function getSlidesContainer(caller){
    "use strict";
    var container = $('#slide-wrapper');
        if (!container){
            container = $(caller).after('<div>').attr('id', 'slide-wrapper');

        }
    return container;
}

$(function(){
    'use strict';
    var vp = viewport(),
        styles = ['#67e2ad','#003e5f','#fa8e53','#f84c53'],  // generate this
        slide = $('#slides').slick(slickOptions );

    $('section').css({'min-height': vp.height});
    $("header").affix();

    $('body').scrollspy({ target: '#main-nav' });
    $('nav a').each(function(i){
        var target = $(this).attr('href'),
            style = styles[(i%styles.length)];
        $(target).css({'background-color':toRGBAString(hexToRgb(style), 0.5)});
        $(this).css({'background-color':style});
    });
    setTimeout(function(){
        var new_color = styles[Math.floor(Math.random()*styles.length)];
        $('#logo').css('background-color', new_color);
    }, 5000);

    $('.cover').on("click", function(event){
        event.preventDefault();
        event.stopPropagation();

        var selected = this,
            hash = window.location.hash,
            target = $(this).attr('href'),
            container = getSlidesContainer();
        $.pjax({
            url:target,
            container: container,
            fragment: '#slide-wrapper',
            success: function() {

                slide = renderSection(selected);
            }
        });
        $('.control').one('click',function(e) {
            e.stopPropagation();
            $('nav').toggle('fade');
            slide.slickRemove();
            history.pushState({}, "Potaje ", "/"+hash);

        });
    });
});
