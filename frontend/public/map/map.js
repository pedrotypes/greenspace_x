var fleet = {};
var bases = [];
var tpl = {};

$(function() {
    tpl = {
        base: Handlebars.compile($("#tpl-base").html()),
        fleet: Handlebars.compile($("#tpl-fleet").html()),
        fleet_info: Handlebars.compile($("#tpl-fleet-info").html())
    };

    drawMap();
    setInterval(refreshFleet, 1000);

    $("#map").on('click', '.base-area', function() {
        $.get('/fleet/move/' + $(this).attr('rel')).done(refreshFleet);
    });
});

function refreshFleet()
{
    $.getJSON('/fleet', function(data) {
        $("#fleet-info").html(tpl.fleet_info(data));
        $("#fleet").remove();
        $("#map").append(tpl.fleet({
            left: data.position.x * 10 - 5,
            top: data.position.y * 10 - 5
        }));
    });
}

function drawMap()
{
    $.getJSON('/bases', function(data) {
        var map = $("#map");
        $.each(data, function(i, base) {
            bases.push(base);
            var radius = Math.round(base.size / 2);
            var base_margin = Math.round(10 - radius) / 2;
            map.append(tpl.base({
                area_top: base.y * 10 - 5,
                area_left: base.x * 10 - 5,
                base_margin: base_margin,
                base_width: radius,
                base_height: radius,
                base: base
            }));
        });

        refreshFleet();
    });
}