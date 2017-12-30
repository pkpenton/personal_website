$(document).ready(function() {

    $(".x").hide();
    $(".menu").hide();

    $(".hamburger").click(function() {
        $(".menu").slideToggle("slow", function() {
            $(".hamburger").hide();
            $(".x").show();
        });
    });

    $(".x").click(function() {
        $(".menu").slideToggle("slow", function() {
            $(".x").hide();
            $(".hamburger").show();
        });
    });

});