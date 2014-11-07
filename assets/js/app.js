$(function() {
    'use strict';

    var $ = require('jquery'),
        Backbone = require('backbone');

    var NavView = Backbone.View.extend({
         el: $("nav ul"),
         model: Backbone.Model.extend({

         })
    });
});

//$().foundation();
/*
$.pjax.defaults.scrollTo = false;


function get_fit(srcWidth, srcHeight, maxWidth, maxHeight) {

    var ratio = Math.min(maxWidth / srcWidth, maxHeight / srcHeight);

    return { width: srcWidth*ratio, height: srcHeight*ratio };
 }

function layout_images(selector){
    var vp, padding, max_height, max_width;

    vp = viewport();
    padding = 15;
    max_height = vp.height - padding;
    max_width = vp.width - padding;

    $(selector).each(function(){
        var slide;
        slide = $(this);
        
        slide.find('img, iframe').load(function(){
            var content, fit, width_delta;
            content = $(this);
            fit = get_fit(content.width(), content.height(), max_width, max_height);
            width_delta = (max_width - content.width())/2;
            content.width(fit.width);
            content.height(fit.height);
            slide.find('.caption').css({
                'margin-left': - (fit.width / 2),
                'width': fit.width,
            })
        })
    })
};
function create_slider(){
    // refactor this into a proper plugin or closure.
    if ($('#slide-wrapper').length){
        $('#slide-wrapper').flexslider({
            animation:'slide',
            controlNav: false,
        });
        $('#slide-wrapper .close').on('click',function(e) {
            e.preventDefault();
            $('nav').toggle('fade', 500);
            $('#slide-wrapper').toggle('fade', 300, function(){
                $(this).remove();
            })
            $('body').css({'overflow':'auto'});
            history.pushState({}, "", "/"+hash);
        })
        layout_images('.slide');
    }
    
};
function handle_album(){
    $('body').css({'overflow':'hidden'});
    $('nav').toggle('fade', 500);
    create_slider()
}
$(document).on('pjax:success', handle_album)

$(function(){
    vp = viewport();
    hash = '';
    create_slider();
    

    $("nav ul").onePageNav({
        'currentClass':'current',
        'changeHash':true,
    });
    
    $('nav a').each(function(i, e){
        colors = ['#67e2ad','#003e5f','#fa8e53','#f84c53'];
        index = i % colors.length;
        $(this).css({'background-color':colors[index]});
    });
    $('section').height(vp.height);

    $(window).on('resize', function(event){
        $('section').height(vp.height);
    });
    $('.album a').on("click", function(event){
        hash = window.location.hash;
        event.preventDefault();
        event.stopPropagation();
        $('#slide-wrapper').remove();
        container = $(this).parents('section').append($('<div>').attr('id','slide-wrapper'));
        target = $(this).attr('href');
        
        $.pjax({
            url:target,
            container: '#slide-wrapper',
            fragment: '#slide-wrapper',
        });
    });

})
*/