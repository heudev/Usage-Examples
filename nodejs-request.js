const request = require('request');
var HTMLParser = require('node-html-parser');

request('https://www.osym.gov.tr/', function (error, response, body) {
    var root = HTMLParser.parse(body);
    var i = 0;
    while (true) {
        var tag = root.querySelector(`#pane ul > li:nth-child(${i + 1})`);
        if (tag == null) break;
        i++;
        console.log(tag.text.trim());
    }
    console.log("Number of outputs:", i);
});
