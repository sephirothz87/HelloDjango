var page = require('webpage').create();
var fs = require('fs');
var system = require('system');

phantom.outputEncoding="gbk";
// page.open("http://localhost:8000/static/testdiff2.html", function(status) {
// page.open("https://www.baidu.com", function(status) {
page.open("http://10.19.95.76:8000/static/form.html", function(status) {
    
    // setTimeout(function () {
    if ( status === "success" ) {
        console.log(page.title); 
        console.log(page); 
        // page.render("t2.png");
        page.render("t2.png");




        // page.evaluate(function () {
        //     var scriptList = document.querySelectorAll('script');
        //     [].forEach.call(scriptList, function (script) {
        //         script.parentElement.removeChild(script);
        //     });
        // });

        var html = page.evaluate(function () {
            return document.documentElement.outerHTML;
            // return window.clipboardData.setData("Text",document.documentElement.value);
        });

        console.log(html);

        fs.write('t1.html', html, 'w');

    } else {
       console.log("Page failed to load."); 
    }
    phantom.exit(0);

    // }, 5000);

});