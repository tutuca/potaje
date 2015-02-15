function viewport(){
    'use strict';
    var e = window,
        a = 'inner';
    if ( !( 'innerWidth' in window ) ){
        a = 'client';
        e = document.documentElement || document.body;
    }
    return { width : e[ a+'Width' ] , height : e[ a+'Height' ] };
};
function renderSection(){
    'use strict';

    $('body').css({'overflow':'hidden'});
    $('nav').toggle('fade', 1000);

    $('.work a').not(selected).each(function(index){
        $(this).parent('article').toggle('fade', 1500*index);
    });
    $('#slide-wrapper').flexslider({
        animation:'slide',
        controlNav: false
    });
};
$(function(){
    'use strict';
    var vp = viewport(),
        styles = ['#67e2ad','#003e5f','#fa8e53','#f84c53']; // generate this

    $('#slide-wrapper').slick({
        animation:'slide'

    });
    $("nav ul").onePageNav({
        'currentClass':'current',
        'changeHash':true

    });
    $('section').height(vp.height);
    $('nav a').each(function(i){
        var style = styles[i];
        $(this).css({'background-color':style});
    });
    setTimeout(function(){
        var new_color = styles[Math.floor(Math.random()*styles.length)];
        $('#logo').css('background-color', new_color);
    }, 5000);

    $('.work a').on("click", function(event){
        var selected = this,
            hash = window.location.hash,
            target = $(this).attr('href');

        event.preventDefault();
        event.stopPropagation();

        $('#slide-wrapper').remove();
        $.pjax({
            url:target,
            container: '#slide-wrapper',
            fragment: '#slide-wrapper',
            success: function() {
                renderSection(selected);
            }
        });
        $('#slide-wrapper .control').one('click',function(e) {
            e.stopPropagation();
            $('nav').toggle('fade');
            $('#slide-wrapper').remove();
            $('body').css({'overflow':'auto'});
            history.pushState({}, "Potaje ", "/"+hash);

        })
    })
})
