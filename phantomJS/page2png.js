var page = require('webpage').create();
var system = require('system');
var t, address;

phantom.inputEncoding="GBK"
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

t = Date.now()
page.open(address, function (status) {
    console.log("Status: " + status);
    if (status === "success") {
        t = Date.now() - t;
        console.log('Loading time ' + t + ' msec');

        page.render('example.png');

    } else {
        console.log('FAIL to load the address : ' + address);
    }
    phantom.exit();
});
