"use strict";

var multiplicity = function(root){
    // Получаем ноды полей
    var minNode = root.querySelector('.multiplicity__min');
    var maxNode = root.querySelector('.multiplicity__max');
    var multiplicityNode = root.querySelector('.multiplicity__multiplicity');
    var resultNode = root.querySelector('.multiplicity__result');

    /* Расчет кратных значений

       Args:
           min (Integer): минмальное значение
           max (Integer): максмальное значение
           multiplicity (Integer): кратность

       Returns:
           []
     */
    var recalc = function(min, max, multiplicity){
        var result = [];
        var min_value = min - 1; // Включаем в результат минимальное значение

        while (min_value <= max) {
            // Рассчитываем следующее кратное
            var next = (min_value + multiplicity - (min_value % multiplicity))

            if (next <= max) {
                // Добавляем в результат, если не вышли за максимум
                result.push(next);
            }

            min_value = next;
        }

        return result
    };

    var update = function(){
        resultNode.value = recalc(
            parseInt(minNode.value),
            parseInt(maxNode.value),
            parseInt(multiplicityNode.value)
            ).join(', ')
    };

    root.addEventListener("change", update);

    update();
}

document.addEventListener("DOMContentLoaded", function(){
    multiplicity(document.querySelector(".multiplicity"))
});
