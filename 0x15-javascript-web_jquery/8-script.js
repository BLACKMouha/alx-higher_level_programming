#!/usr/bin/node
const u = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
const lm= $('#list_movies');
$.getJSON(u, function (d) {
	$.each(d.films, function (k, v) {
		$.getJSON(v, function (x) {
			lm.append('<li>' + x.title + '</li>');
		});
	});
});
