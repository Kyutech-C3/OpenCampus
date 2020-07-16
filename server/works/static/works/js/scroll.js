$(function(){
  $(".genre_button").click(function(e){
    const target_id = $(e.target).data("scroll-to");
    $("body, html").animate({scrollTop: $(target_id).offset().top});
    document.body.classList.remove('nav-open');
  });
});
