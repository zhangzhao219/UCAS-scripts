// ==UserScript==
// @name         国科大抢课-自动选择课程
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Zhang Zhao
// @match        https://jwxk.ucas.ac.cn/courseManage/selectCourse?*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=ucas.ac.cn
// @grant        none
// ==/UserScript==

(function() {
    var classlist = ["1201Z1MGX009H"];
    var tds = document.querySelectorAll('tbody tr');
    for(var i = 0; i < tds.length; ++i) {
        var classstring = tds[i].children[3].innerText;
        if (classlist.indexOf(classstring) != -1){
            var issuccess = tds[i].children[0].children[0];
            var inputbox = document.createElement("div");
            inputbox.innerHTML = "";
            document.getElementById('regfrm').appendChild(inputbox);
            if(issuccess.hasAttribute('disabled')){
                // issuccess.removeAttribute('disabled'); // 删除掉disabled元素
                // tds[i].children[0].children[0].click(); // 上面的一样
                inputbox.className = 'alert-danger';
                classstring = classstring + "\t" + tds[i].children[4].innerText + "\t" + "未成功选中！ 限选" + tds[i].children[7].innerText + " 已选" + tds[i].children[8].innerText+  "</br>";
            }
            else{
                tds[i].children[0].children[0].click();
                inputbox.className = 'alert-success';
                classstring = classstring + "\t" + tds[i].children[4].innerText + "\t" + "成功选中！</br>";
            }
            inputbox.innerHTML += classstring;
        }
    }
    window.scroll(0,1000000000);
})();