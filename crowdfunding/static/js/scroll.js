$(document).ready(function () {
    var xH
    $('.dhiraj').hover(
    function () {
        xH = $(this).children("img").css("height");
        xH = parseInt(xH);
        xH = xH - 150;
        xH = "-" + xH + "px";
        $(this).children("img").css("top", xH);
    }, function () {
        $(this).children("img").css("top", "0px");
    });
});