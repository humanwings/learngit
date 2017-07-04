var page = require('webpage').create();
var system = require('system');
var t, address;

phantom.outputEncoding="Shift_JIS"

if (system.args.length === 1) {
  console.log('Usage: loadspeed.js <some URL>');
  phantom.exit();
} else {
    system.args.forEach(function (arg, i) {
        console.log(i + ': ' + arg);
    });
    console.log("\n");

}

address = system.args[1]
console.log('Loading  ... ' + address);

page.onConsoleMessage = function (msg) {
    console.log(msg);
};

console.log('Loading  ... ');
page.open(address, function (status) {
    console.log("Status: " + status);
    if (status === "success") {
        var title = page.evaluate(function() {
            return document.title;
        });
        console.log('Page title is ' + title);
        

        page.evaluate(function() {
            console.log('Page title is ' + document.title)
        });
        
    } else {
        console.log('FAIL to load the address : ' + address);
    }
    phantom.exit();
});
