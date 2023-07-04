// ==UserScript==
// @name         国科大雁栖湖校区西区羽毛球馆预约
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://ehall.ucas.ac.cn/v2/reserve/reserveDetail?id=6
// @icon         https://www.google.com/s2/favicons?sz=64&domain=ucas.ac.cn
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    var k = 2 // 默认抢后两天的时间，也可以更改
    function sleep (time) {
        return new Promise((resolve) => setTimeout(resolve, time));
    }

    // 用法
    sleep(1000).then(() => {
        document.querySelector("body > div.el-message-box__wrapper > div > div.el-message-box__btns > button").click()
        for(var i=0;i<k;i++){
            document.querySelector("#reserveDetail > div.reserveDetail_content.content_w > div > div.reserveDetail_content_left > div.content_top.startReserve > div.select_week > button:nth-child(5)").click()
        }
    })
    sleep(2000).then(() => {
        document.querySelector("#dayReserve > div.right_calendar > div > div:nth-child(22) > div:nth-child(2) > div").click()
    })

    // Your code here...
})();