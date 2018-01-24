$(document).ready(function() {

    $(".footer-twitter").hover(function() {
        $(this).attr("src", "https://patricia-penton.s3.amazonaws.com/images/twitter_orange.png");
        }, function() {
        $(this).attr("src", "https://patricia-penton.s3.amazonaws.com/images/twitter_white.png");
    });

    $(".footer-linkedin").hover(function() {
        $(this).attr("src", "https://patricia-penton.s3.amazonaws.com/images/linkedin_orange.png");
        }, function() {
        $(this).attr("src", "https://patricia-penton.s3.amazonaws.com/images/linkedin_white.png");
    });

    $(".footer-github").hover(function() {
        $(this).attr("src", "https://patricia-penton.s3.amazonaws.com/images/github_orange.png");
        }, function() {
        $(this).attr("src", "https://patricia-penton.s3.amazonaws.com/images/github_white.png");
    });

    $(".footer-envelope").hover(function() {
        $(this).attr("src", "https://patricia-penton.s3.amazonaws.com/images/envelope_orange.png");
        }, function() {
        $(this).attr("src", "https://patricia-penton.s3.amazonaws.com/images/envelope_white.png");
    });

});
