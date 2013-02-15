var fleetRefreshTimeout = 500;
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
    setInterval(refreshFleet, fleetRefreshTimeout);

    $("#map").on('click', '.base-area', function() {
        $.get('/fleet/move/' + $(this).attr('rel')).done(refreshFleet);
    });
});

function refreshFleet()
{
    $.getJSON('/fleet', function(data) {
        $("#fleet-info").html(tpl.fleet_info(data));
        $("#fleet").remove();

        var location;
        if (data.eta) location = calculateFleetOffset(data);
        else location = {
            left: data.position.x * 10 - 9,
            top: data.position.y * 10 - 9,
            moving: false
        };
        $("#map").append(tpl.fleet(location));
    });
}

function calculateFleetOffset(fleet)
{
    var delta = {
        x: fleet.destination.x - fleet.position.x,
        y: fleet.destination.y - fleet.position.y
    };
    var progress = 1 - parseInt(fleet.eta, 10) / fleet.eta_total;

    return {
        top: (fleet.position.y + (delta.y * progress)) * 10 - 5,
        left: (fleet.position.x + (delta.x * progress)) * 10 - 5,
        moving: true
    };
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