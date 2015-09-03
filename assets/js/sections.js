require('new-pjax');
/* Album.Section, single display.
*  Fetches the
*
* */

var section = function() {
    // TODO: move it out.
    // TODO: This is not a proper "class". Should need modifications to be actually useful.

    return {
        init: function (event) {
            event.preventDefault();
            event.stopPropagation();
            var selected = this, // TODO: make sure this is a proper jquery.
                anchor = window.location.hash,
                selector = '#slide-wrapper',
                target = $(this).attr('href'),
                container = getSlidesContainer();

            section.fetch(target, container, selector);
            $('.control').one('click', section.close);
        },
        fetch: function (target, container, fragment) {
            $.pjax({
                url: this.target,
                container: this.container,
                fragment: this.fragment,
                success: function () {
                    slide = section.render(); // TODO: move to local scope.
                }
            });

        },
        render: function () {
            /*
             * Pjax callback funcion
             * */
                if (selected) {
                $('body').css({'overflow': 'hidden'});
                $('nav').toggle('fade', 1000);

                $('.work a').not(selected).each(function (index) {
                    $(this).parent('article').toggle('fade', 1500 * index);
                });
                return $('#slides').slick(slickOptions);
            }
        },

        close: function (event) {
            event.stopPropagation();
            $('nav').toggle('fade');
            slide.slickRemove(); // TODO: move `slide` to local scope.
            history.pushState({}, "Potaje ", "/" + hash);

        },
        getSlidesContainer: function () {
            var container = $(this.selector);
            if (!container) {
                container = $(caller).after('<div>').attr('id', 'slide-wrapper');

            }
            return container;
        }
    };
};

module.exports = {
    section,
}