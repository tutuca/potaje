import $ from "jquery";

const MIN_SIZE = 576;

export const initLogo = (element) => {
  const width = $(window).width;
  if (width >= MIN_SIZE) {
    $(element).on("click", (element) => {
      const target = element.target;
      const menu = $("#main-nav");
    });
  }
  return element;
};
