$(document).ready(function() {

    $(".x").hide();
    $(".menu").hide();

    $(".hamburger").click(function() {
        $(".menu").slideToggle("fast", function() {
            $(".hamburger").hide();
            $(".x").show();
        });
    });

    $(".x").click(function() {
        $(".menu").slideToggle("fast", function() {
            $(".x").hide();
            $(".hamburger").show();
        });
    });

});