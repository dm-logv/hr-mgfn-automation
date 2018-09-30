"use strict";

var matrix = function(root){
    // Получаем ноды полей
    var nNode = root.querySelector('.matrix__n');
    var mNode = root.querySelector('.matrix__m');
    var dNode = root.querySelector('.matrix__d');
    var resultNode = root.querySelector('.matrix__result');

    /* Заполнение матрицы

       Args:
           n (Integer): количество строк
           m (Integer): количество ячеек
           d: заполнитель

       Returns:
           [[]]
     */
    var recalc = function(n, m, d){
        var matrix = [];

        for(var i = 0; i < n; i++){
            matrix.push([]);

            for(var j = 0; j < m; j++){
                matrix[i].push(d);
            }
        }

        return matrix;
    };

    var update = function(){
        resultNode.value = "[" + recalc(
            parseInt(nNode.value),
            parseInt(mNode.value),
            dNode.value
            ).join("\n ") + "]";
    };

    root.addEventListener("change", update);

    update();
}

document.addEventListener("DOMContentLoaded", function(){
    matrix(document.querySelector(".matrix"))
});
