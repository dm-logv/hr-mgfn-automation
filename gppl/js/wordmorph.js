"use strict";

var wordmorph = function(root){
    // Получаем ноды полей
    var numNode = root.querySelector('.wordmorph__num');
    var wordNode = root.querySelector('.wordmorph__word');
    var resultNode = root.querySelector('.wordmorph__result');

    /* Расчет кратных значений

       Args:
           min (Integer): минмальное значение
           max (Integer): максмальное значение
           wordmorph (Integer): кратность

       Returns:
           []
     */
    var recalc = function(num, word){
        // Последняя цифра
        var lastDigit = num % 10;
        // Окончание
        var end = "";

        if (
                // Односоставные числительные
                (5 <= num && num <= 20)
                // Составные числительные
                || (lastDigit == 0 || 5 <= lastDigit && lastDigit <= 9)
        ){
            end = 'ов';
        } else if (lastDigit == 1) {
            end = '';
        } else if (2 <= lastDigit && lastDigit <= 4) {
            end = 'а';
        }

        return num + " " + word + end;
    };

    var update = function(){
        resultNode.value = recalc(parseInt(numNode.value), wordNode.value)
    };

    root.addEventListener("change", update);

    update();
}

document.addEventListener("DOMContentLoaded", function(){
    wordmorph(document.querySelector(".wordmorph"))
});
