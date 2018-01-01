$(document).ready(function() {

    $(".x").hide();
    $(".menu").hide();

    $(".hamburger").click(function() {
        $(".menu").slideToggle("medium", function() {
            $(".hamburger").hide();
            $(".x").show();
        });
    });

    $(".x").click(function() {
        $(".menu").slideToggle("medium", function() {
            $(".x").hide();
            $(".hamburger").show();
        });
    });

});