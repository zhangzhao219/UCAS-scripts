// ==UserScript==
// @name         自动提交代码评测
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Zhang Zhao
// @match        https://course.educg.net/assignment/programOJPList.jsp*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=educg.net
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    var button_summit = document.createElement("input");
    button_summit.value = "自动评测";
    button_summit.type = "button";
    button_summit.className = "btn btn-danger"
    document.getElementsByClassName('form-inline my-2')[1].appendChild(button_summit);
    button_summit.onclick = function () {
        var myVar = setInterval(
            fn()
            ,1000*60*60
        );
    }
    function fn() {
        var time = new Date();
        var score = document.querySelector("iframe").contentWindow.document.getElementById("result").childNodes[0].innerHTML.split(".")[0].split("分")[1];
        var latency = document.querySelector("iframe").contentWindow.document.getElementsByTagName("p")[3].innerHTML.split("<br>").slice(-115)[0].split(" ")[1]
        console.log("评测时间：",time);
        console.log("上次得分：",score);
        console.log("上次推理时间：",latency);
        if (score == "90"){
            clearInterval(myVar);
            console.log("满分！")
            return;
        } else{
            document.getElementById("ojpSubmitBtn").click();
        }
        return fn
    }

})();