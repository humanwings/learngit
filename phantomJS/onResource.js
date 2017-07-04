"use strict";
var page = require('webpage').create(),
    system = require('system'),
    t, address;

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

// page.onResourceRequested = function(request) {
//   console.log('Request ' + JSON.stringify(request, undefined, 4));
// };
page.onResourceRequested = function(requestData, networkRequest) {
  console.log('Request (#' + requestData.id + '): ' + JSON.stringify(requestData));
};
// page.onResourceReceived = function(response) {
//   console.log('Receive ' + JSON.stringify(response, undefined, 4));
// };

page.open(address, function (status) {
    console.log("Status: " + status);
    if (status === "success") {
        console.log('loading done : ' + address);        
    } else {
        console.log('FAIL to load the address : ' + address);
    }
    phantom.exit();
});

