function viewport(){
    e = window;
    a = 'inner';
    if ( !( 'innerWidth' in window ) ){
        a = 'client';
        e = document.documentElement || document.body;
    };
    return { width : e[ a+'Width' ] , height : e[ a+'Height' ] };
};
function nube(ctx, x, y, size, steps) {
    ctx.beginPath();  
    for(i=0;i<steps;i++) {
        ctx.arc(x+(size*2)*i, y, size, 0, Math.PI, true);
    }
    ctx.fill();
}
function waves(ctx, x, y, width, height){
    styles = ['#67e2ad','#003e5f','#fa8e53','#FBF383','#B04C64'];
    vertical_limit = 30;
    for (j=0;j<30; j++) {
        d_y = Math.floor(Math.random()*height) + y;
        // transformacion de size
        size = (d_y - y)*0.1+5
        d_x = Math.floor(Math.random()*(width-size)) + x;
        steps = Math.floor(width/Math.floor(size))-40;
        // transformacion de color
        ctx.globalAlpha=Math.random()+0.3;
        ctx.fillStyle = styles[Math.floor(Math.random()*styles.length)];

        nube(ctx,d_x, d_y, size, steps);
    }
};
$(function(){
    vp = viewport();
    
    $("#waves").attr('width',vp.width);
    $("#waves").attr('height',vp.height);
    $('section').height(vp.height);
    $('nav a').each(function(i, e){
        styles = ['#67e2ad','#003e5f','#fa8e53','#f84c53'];
        style = styles[i];
        $(this).css({'background-color':style})
    })
    image = new Image();
    image.src = '/static/img/logo_periscopio.png';
    
    canvas = $('canvas')[0];
    ctx = canvas.getContext("2d");
    image.onload = function(){
        console.log(image.height);
        img_y = (vp.height/2)-(image.height/1.3);
        img_x = (vp.width/2)-image.width;
        ctx.drawImage(image, img_x, img_y)
        waves(ctx, 0, vp.height/2, vp.width, vp.height/2);
    }



})
