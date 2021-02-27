// ==UserScript==
// @name         Aimgods Bot
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Script to scroll through the cases automatically
// @author       LLinoor
// @match        https://aimgods.finalmouse.com/goldenKey
// @grant        none
// ==/UserScript==

setTimeout(() => {
    var use = document.getElementsByClassName("ZxONt")
    var play = document.getElementsByClassName("dDhfSV")
    var keys = 0

   function automate(){
        setInterval(() => {
            use[0].click()
        }, 250);
        setInterval(() => {
            play[0].click()
        }, 18000);
   }

    automate()
}, 2000);