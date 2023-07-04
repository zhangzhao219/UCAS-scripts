// ==UserScript==
// @name         科学前沿讲座监控
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://jwxk.ucas.ac.cn/subject/student
// @icon         https://www.google.com/s2/favicons?sz=64&domain=ucas.ac.cn
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    var resultsum = 0;
    var scorelist = document.getElementsByTagName('table')[0].children[1].children;
    for(var j=0;j<scorelist.length;j+=1){
        resultsum += scorelist[j].children[1].innerHTML*1;
    }
    console.log(resultsum);
    document.getElementsByClassName('mc-body')[0].children[3].innerHTML += ' 总计学时' + resultsum.toString()+' 其中一定有效'+ (resultsum-12).toString()+'学时';
    // Your code here...
})();