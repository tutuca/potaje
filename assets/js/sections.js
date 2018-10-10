import $ from 'jquery';
import 'new-pjax';
window.jQuery = $;

class Section {
  // TODO: move it out.
  // TODO: This is not a proper "class". Should need modifications to be actually useful.


  init(event) {
    event.preventDefault();
    event.stopPropagation();
    const anchor = window.location.hash;
    const selector = '#slide-wrapper';
    const target = $(this).attr('href');
    const container = getSlidesContainer();

    section.fetch(target, container, selector);
    $('.control').one('click', section.close);
  }
  fetch(target, container, fragment) {
    $.pjax({
      url: this.target,
      container: this.container,
      fragment: this.fragment,
      success: function () {
        slide = section.render(); // TODO: move to local scope.
      }
    });
  }
  render() {
    /*
     * Pjax callback funcion
     * */
    if (selected) {
      $('body').css({ 'overflow': 'hidden' });
      $('nav').toggle('fade', 1000);

      $('.work a').not(selected).each(function (index) {
        $(this).parent('article').toggle('fade', 1500 * index);
      });
      return $('#slides').slick(slickOptions);
    }
  }
  close(event) {
    event.stopPropagation();
    $('nav').toggle('fade');
    slide.slickRemove(); // TODO: move `slide` to local scope.
    history.pushState({}, "Potaje ", "/" + hash);
  }
  getSlidesContainer() {
    var container = $(this.selector);
    if (!container) {
      container = $(caller).after('<div>').attr('id', 'slide-wrapper');

    }
    return container;
  }
};

export default Section;