#!/usr/bin/node
const ai = $('#add_item');
const myList = $('.my_list');

ai.on('click', function () {
  myList.append('<li>Item</li>');
});
