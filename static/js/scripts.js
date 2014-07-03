function viewport_size(){
    e = window;
    a = 'inner';
    if ( !( 'innerWidth' in window ) ){
        a = 'client';
        e = document.documentElement || document.body;
    };
    return { width : e[ a+'Width' ] , height : e[ a+'Height' ] };
};

function create_slider(){
/* refactor this into a proper plugin or closure. */
    if ($('#slide-wrapper').length){
        $('#slide-wrapper').flexslider({
            animation:'slide',
            controlNav: false,
        });
        $('#slide-wrapper .close').on('click',function(e) {
            e.preventDefault();
            $('nav').toggle('fade');
            $('#slide-wrapper').remove();
            $('body').css({'overflow':'auto'});
            history.pushState({}, "", "/"+hash);
        })
        $('.slide').each(function(){
            $(this).find('img').load(function(){
                w = $(this).width();
                $(this).siblings('.caption').css({
                    'margin-left': -w/2,
                    'width':w,
                })
            })
        })
    }
    
};

$(function(){

    create_slider();
    vp = viewport_size();
    $("nav ul").onePageNav({
        'currentClass':'current',
        'changeHash':true,
        
    });
    
    $('nav a').each(function(i, e){
        colors = ['#67e2ad','#003e5f','#fa8e53','#f84c53'];
        index = i % colors.length
        $(this).css({'background-color':colors[index]})
    });

    $('section').height(vp.height);

    $(window).on('resize', function(event){
        $('section').height(vp.height);
    });

    $('.work a').on("click", function(event){
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
            success: function(){
                $('body').css({'overflow':'hidden'});
                $('nav').toggle('fade', 1000);
                create_slider()
            }
        });
    });

})
