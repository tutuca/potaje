/* Globals */
import '../sass/style.scss';
import $ from  'jquery';
window.jQuery = $;

import {
    viewport,
    fit
} from './helpers';
const styles = [ // TODO: generate this using http://devmag.org.za/2012/07/29/how-to-choose-colours-procedurally-algorithms/
    '#67e2ad',
    '#003e5f',
    '#fa8e53',
    '#f84c53'
];
const slickOptions = {
    dots: true,
    accessibility: true,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    centerMode: true,
    variableWidth: true
};


require('bootstrap-sass');
require('new-pjax');

function collapseNavbar (){
    $('#main-nav').hide();
}
function fitImages(){
    fit($(this), '#slide-wrapper');
}

function colorize (i){
    const color = styles[(i%styles.length)];
    $(this).css({'background-color': color});
}

/* main */
$(() => {
    const vp = viewport();
    const home_img = $('#home').css('background-image');

    $('nav a').each(colorize);
    $('section:not(#home)').css({'min-height': vp.height});
    $('#home').css({
        'background-image': home_img,
        'min-height': vp.height
    });
    $('body').scrollspy({ target: '#main-nav' });
    $("header").affix();

    setTimeout(function(){
        const new_color = styles[Math.floor(Math.random()*styles.length)];
        $('#logo').css('background-color', new_color);
    }, 5000);
    //$('.cover').each(section.init);
});
