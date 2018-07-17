/* Globals */
import '../sass/style.scss';

import $ from  'jquery';
import 'bootstrap';

const styles = [ // TODO: generate this using http://devmag.org.za/2012/07/29/how-to-choose-colours-procedurally-algorithms/
    '#67e2ad',
    '#003e5f',
    '#fa8e53',
    '#f84c53'
];

window.jQuery = $;

function colorize (i){
    const color = styles[(i%styles.length)];
    $(this).css({'background-color': color});
}

/* main */
$(() => {

    $('#main-nav li a').each(colorize);
        
    setTimeout(function(){
        const new_color = styles[Math.floor(Math.random()*styles.length)];
        $('#logo').css('background-color', new_color);
    }, 5000);
});
