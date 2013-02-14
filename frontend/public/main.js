$(function() {
    $.getJSON('/bases', function(data) {
        var map = $("#map");
        $.each(data, function(i, base) {
            var tpl = Handlebars.compile($("#tpl-base").html());
            var radius = Math.round(base.size / 2);
            var base_margin = Math.round(10 - radius) / 2;
            map.append(tpl({
                area_top: base.y * 10 - 5,
                area_left: base.x * 10 - 5,
                base_margin: base_margin,
                base_width: radius,
                base_height: radius,
                base: base
            }));
        });
    });
});