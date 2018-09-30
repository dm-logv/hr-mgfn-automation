"use strict";

var mortgage = function(root){
    var valueNode = root.querySelector('.mortgage__value');
    var rateNode = root.querySelector('.mortgage__rate');
    var termNode = root.querySelector('.mortgage__term');
    var overpaymentsNode = root.querySelector('.mortgage__overpayments');

    var recalc = function(value, rate, term){
        return value * rate * term
    };

    var update = function(){
        overpaymentsNode.value = recalc(valueNode.value, rateNode.value, termNode.value)
    };

    root.addEventListener("change", update);

    update();
}

document.addEventListener("DOMContentLoaded", function(){
    mortgage(document.querySelector(".mortgage"))
});