#!/usr/bin/node
const hu = "https://fourtonfish.com/hellosalut/?lang=fr";
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (d) {
    $('#hello').text(d.hello);
});
