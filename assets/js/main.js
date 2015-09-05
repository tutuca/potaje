/* Globals */

var $ = require('jquery');
window.jQuery = $;

var helpers = require('./helpers.js'),
    selected,
    styles = [ // TODO: generate this using http://devmag.org.za/2012/07/29/how-to-choose-colours-procedurally-algorithms/
        '#67e2ad',
        '#003e5f',
        '#fa8e53',
        '#f84c53'
    ],
    slickOptions = {
        dots: true,
        accessibility: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        centerMode: true,
        variableWidth: true
    };


require('bootstrap-sass');
require('slick-carousel');
require('new-pjax');

function collapseNavbar (){
    'use strict';
    $('#main-nav').hide();
}
function fitImages(){
    helpers.fit($(this), '#slide-wrapper');
}
function colorizeNav (i){
    var color = styles[(i%styles.length)];
    $(this).css({'background-color': helpers.toRGBAString(color, 0.5)});
}

/* main */
$(function(){
    var vp = helpers.viewport();

    $('section').css({'min-height': vp.height});
    $('.slider').css({'height': vp.height});
    $('.slide').css({
        'height': vp.height - 120,
        'width': vp.width - 120
    });

    $('body').scrollspy({ target: '#main-nav' });
    $('nav a').each(function(i){
        var color = styles[(i%styles.length)];
        $(this).css({'background-color': color});
    });
    $('section').each(colorizeNav);
    
    $('#slides').on('init', collapseNavbar);
    helpers.fit('#video-reel', '#reel');
    $("header").affix();

    $('#slides').slick(slickOptions);
    $('.slide img').each(helpers.fitImages);
    setTimeout(function(){
        var new_color = styles[Math.floor(Math.random()*styles.length)];
        $('#logo').css('background-color', new_color);
    }, 5000);
    //$('.cover').on("click", section.init);
});
