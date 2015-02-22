/* Globals */
var selected,
    slide,
    styles = [
        '#67e2ad',
        '#003e5f',
        '#fa8e53',
        '#f84c53'
    ];  // TODO: generate this using http://devmag.org.za/2012/07/29/how-to-choose-colours-procedurally-algorithms/
    slickOptions = {
        dots: true,
        accessibility: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        centerMode: true,
        variableWidth: true
    };


/* Views */

function collapseNavbar (){
    "use strict";
    debugger
    $('#main-nav').hide('fold');
}

/* main */
$(function(){
    'use strict';
    var vp = viewport();

    $('section').css({'min-height': vp.height});
    $('.slider').css({'height': vp.height});
    $('.slide').css({
        'height': vp.height - 120,
        'width': vp.width - 120
    });

    $("header").affix();

    $('body').scrollspy({ target: '#main-nav' });
    $('nav a').each(function(i){
        var target = $(this).attr('href').replace('/', ''),
            style = styles[(i%styles.length)];
        $(target).css({'background-color':toRGBAString(hexToRgb(style), 0.5)});
        $(this).css({'background-color':style});
    });
    $('.slide img').on('load', function(){
        fit(this, '#slide-wrapper');
    });

    slide = $('#slides')
                .slick(slickOptions)
                .on('init', function(){console.log('caca')});

    setTimeout(function(){
        var new_color = styles[Math.floor(Math.random()*styles.length)];
        $('#logo').css('background-color', new_color);
    }, 5000);
    //$('.cover').on("click", section.init);
});
