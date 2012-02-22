function viewport(){
    e = window;
    a = 'inner';
    if ( !( 'innerWidth' in window ) ){
        a = 'client';
        e = document.documentElement || document.body;
    };
    return { width : e[ a+'Width' ] , height : e[ a+'Height' ] };
};

$(function(){
    $('#slide-wrapper').flexslider({
        animation:'slide',
        
    })

    vp = viewport();
    $("nav ul").onePageNav({
        'currentClass':'current',
        'changeHash':true,
        
    })
    $('section').height(vp.height);
    $('nav a').each(function(i, e){
        styles = ['#67e2ad','#003e5f','#fa8e53','#f84c53'];
        style = styles[i];
        $(this).css({'background-color':style})
    })
    
    $('.work').each(function(i,e){
        pos = $(this).position();
        $(this).css({'left':pos['left'], 'top':pos['top']})
     }).css({'position':'absolute',});
    $('.work a').on("click", function(event){
        selected = this;
        hash = window.location.hash;
        event.preventDefault();
        event.stopPropagation();
        $('#slide-wrapper').remove();
        container = $(this).parents('section').append($('<div>').attr('id','slide-wrapper'));
        target = $(this).attr('href');
        rest = $('.work a').not(selected);
        length = rest.lentgh;
        $.pjax({
            url:target,
            container: '#slide-wrapper',
            fragment: '#slide-wrapper',
            success: function(){
                $('body').css({'overflow':'hidden'});
                $('nav').toggle('fade', 1000);
                rest.each(function(index){
                    $(this).parent('article').toggle('fade', 1500*index);
                });
                $('#slide-wrapper').flexslider({
                    animation:'slide',
                    
                })
            }
        });
        $('#slide-wrapper').one('click',function() {
            event.stopPropagation();
            $('nav').toggle('fade');
            rest.each(function(){
                $(this).parent('article').toggle('fade');
            });
            $(this).remove();
            $('body').css({'overflow':'auto'});
            history.pushState({}, "Potaje ", "/"+hash);

        })
    })
})
