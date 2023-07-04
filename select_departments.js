// ==UserScript==
// @name         国科大抢课-自动选择院系并新增课程
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Zhang Zhao
// @match        https://jwxk.ucas.ac.cn/courseManage/main*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=ucas.ac.cn
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    // document.getElementById('id_910').click(); // 数学学院
    // document.getElementById('id_914').click(); // 地球学院
    // document.getElementById('id_915').click(); // 外语系
    document.getElementById('id_917').click(); // 经管
    // document.getElementById('id_927').click(); // 人文
    // document.getElementById('id_945').click(); // 公管学院
    // document.getElementById('id_951').click(); // 计算机
    // document.getElementById('id_963').click(); // 网安
    // document.getElementById('id_964').click(); // 马克思
    // document.getElementById('id_969').click(); // 人工智能
    document.getElementsByName('sb')[1].click();//选课按钮
})();