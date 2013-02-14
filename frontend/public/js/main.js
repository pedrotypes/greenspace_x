$(function() {
    setMapHeight();
    $(window).resize(setMapHeight);
});

function setMapHeight()
{
    var h = $(window).height() - 50 - 4;
    $("#map").height(h);
}