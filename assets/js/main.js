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

function colorize (i){
    var color = styles[(i%styles.length)];
    $(this).css({'background-color': color});
}

/* main */
$(function(){
    var vp = helpers.viewport(),
        home_img = $('#home').css('background-image');

    $('nav a').each(colorize);
    $('section:not(#home)').each(colorize);
    $('section:not(#home)').css({'min-height': vp.height});
    $('.slider').css({'height': vp.height});
    $('.slide').css({
        'height': vp.height - 120,
        'width': vp.width - 120
    });
    $('#home').css({
        'background-image': home_img,
        'min-height': vp.height
    });
    $('body').scrollspy({ target: '#main-nav' });
    $('#slides').on('init', collapseNavbar);
    helpers.fit('#video-reel', '#reel');
    $("header").affix();

    $('#slides').slick(slickOptions);
    $('.slide img').each(helpers.fitImages);
    setTimeout(function(){
        var new_color = styles[Math.floor(Math.random()*styles.length)];
        $('#logo').css('background-color', new_color);
    }, 5000);
    //$('.cover').each(section.init);
});
