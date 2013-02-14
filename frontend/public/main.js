$(function() {
    $.getJSON('/bases', function(data) {
        var map = $("#map");
        $.each(data, function(i, base) {
            var tpl = Handlebars.compile($("#tpl-base").html());
            var radius = Math.round(base.size / 2);
            map.append(tpl({
                top: base.y * 10 - radius,
                left: base.x * 10 - radius,
                width: radius,
                height: radius
            }));
        });
    });
});