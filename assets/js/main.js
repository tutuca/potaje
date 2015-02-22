/* Globals */
var selected,
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



function collapseNavbar (){
    'use strict';
    $('#main-nav').hide();
}
function fitImages(){
    'use strict';
    fit(this, '#slide-wrapper');
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

    $('body').scrollspy({ target: '#main-nav' });
    $('nav a').each(function(i){
        var color = styles[(i%styles.length)];
        $(this).css({'background-color': color});
    });
    $('section').each(function(i){
        var color = styles[(i%styles.length)];
        $(this).css({'background-color':toRGBAString(color, 0.5)});
    });
    $('.slide img').on('load', fitImages);
    $('#slides').on('init', collapseNavbar);

    $("header").affix();

    $('#slides').slick(slickOptions);

    setTimeout(function(){
        var new_color = styles[Math.floor(Math.random()*styles.length)];
        $('#logo').css('background-color', new_color);
    }, 5000);
    //$('.cover').on("click", section.init);
});
