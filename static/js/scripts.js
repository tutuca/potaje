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
    
    $('.work').each(function(){
        pos = $(this).position();
        $(this).css({'left':pos['left'], 'top':pos['top']})
     }).css({'position':'absolute',});
    $('.work a').on("click", function(event){
        selected = this;
        event.preventDefault();
        event.stopPropagation();
        $('#slide-wrapper').remove();
        container = $(this).parents('section').append($('<div>').attr('id','slide-wrapper'));
        target = $(this).attr('href');
        $.pjax({
            'url':target,
            'container': '#slide-wrapper',
        })

        rest = $('.work a').not(selected);
        rest.each(function(index){
            $(this).parent('article').toggle('fade', 1000*index);
        });
        $('body').one('click',function() {
            rest.each(function(){
                $(this).parent('article').toggle('fade');
            });
        });

    })
})
