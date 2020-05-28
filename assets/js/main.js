/* Globals */
import "../sass/style.scss";
import $ from "jquery";
import "bootstrap";
import { fit } from "./helpers";
import { initLogo } from "./logo";

window.jQuery = $;
const styles = [
  // TODO: generate this using http://devmag.org.za/2012/07/29/how-to-choose-colours-procedurally-algorithms/
  "#67e2ad",
  "#003e5f",
  "#fa8e53",
  "#f84c53",
];
const logo = $("#logo");
function colorize(i) {
  const color = styles[i % styles.length];
  $(this).css({ "background-color": color });
}

/* main */
$(() => {
  initLogo(logo);
  $("#main-nav li.nav-item a").each(colorize);
  $("#home .album-reel iframe").each(fit);
  setTimeout(function () {
    const selectedColor = Math.floor(Math.random() * styles.length);
    const newColor = styles[selectedColor];
    $("#logo").css("background-color", newColor);
  }, 5000);
});
