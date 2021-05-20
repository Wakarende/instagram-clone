$(document).on("scroll", function () {
  if ($(document).scrollTop() > 50) {
    $(".navigation").addClass("shrink");
  } else {
    $(".navigation").removeClass("shrink");
  }
});
