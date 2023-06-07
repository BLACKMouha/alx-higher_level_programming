#!/usr/bin/node
const u = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
const c = $('#character');

$.getJSON(u, function (d) {
	c.text(d.name);
});
