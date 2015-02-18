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

function getSlidesContainer(caller){
    "use strict";
    var container = $('#slide-wrapper');
        if (!container){
            container = $(caller).after('<div>').attr('id', 'slide-wrapper');

        }
    return container;
}


/* Views */
var section = {
    // TODO: move it out.
    // TODO: This is not a proper "class". Should need modifications to be actually useful.
    init: function(event){
        event.preventDefault();
        event.stopPropagation();
        selected = this; // TODO: move to local scope.

        var hash = window.location.hash,
            target = $(this).attr('href'),
            container = getSlidesContainer();
        section.fetch(target, container, '#slide-wrapper')
        $('.control').one('click', section.close);
    },
    fetch: function(target, container, fragment) {
        "use strict";
        $.pjax({
            url:this.target,
            container: this.container,
            fragment: this.fragment,
            success: function() {
                slide = section.render(); // TODO: move to local scope.
            }
        });

    },
    render: function(){
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
    },

    close: function(event) {
        event.stopPropagation();
        $('nav').toggle('fade');
        slide.slickRemove(); // TODO: move `slide` to local scope.
        history.pushState({}, "Potaje ", "/"+hash);

    }
}
function collapseNavbar (){
    "use strict";
    debugger
    $('#main-nav').hide('fold');
}

/* main */
$(function(){
    'use strict';
    var vp = viewport();

    $('.albums').css({'min-height': vp.height});
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
