$(document).ready(function(){
    $("#topBtn").hide(); 
    $(window).on("scroll", function() {
        if ($(this).scrollTop() > 100) {
            $("#topBtn").fadeIn("fast"); 
        } else { 
            $("#topBtn").fadeOut("fast"); 
        }
        scrollHeight = $(document).height();
        scrollPosition = $(window).height() + $(window).scrollTop(); 
        footHeight = $("footer").innerHeight(); 
        if ( scrollHeight - scrollPosition  <= footHeight ) { 
            $("#topBtn").css({
                "position":"absolute", 
                "bottom": footHeight + 80 
            });
        } else { 
            $("#topBtn").css({
                "position":"fixed", 
                "bottom": "20px" 
            });
        }
    });
    $('#topBtn').click(function () { 
        $('body,html').animate({ 
        scrollTop: 0 
        }, 400); 
        return false;
    });
});