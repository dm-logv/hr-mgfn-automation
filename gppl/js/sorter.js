"use strict";

var sorter = function(root){
    // Получаем ноды полей
    var resultNode = root.querySelector('.sorter__result');

    /* Человек

       Args:
           name (str): имя
           age (int): возраст
     */
    var Person = function(name, age){
        this.name = name;
        this.age = age;

        this.parse = function(raw){
            var arr = raw.split(",").map(function(str){
                return str.trim()
            });
            this.name = arr[0];
            this.age = parseInt(arr[1]);
        }

        this.toString = function(){
            return this.name + ", " + this.age;
        }
    };

    /* Функция сравнения по имени */
    Person.compareName = function(a, b){
        return a.name < b.name ? -1 : 1;
    }

    /* Функция сравнения по возрасту (в убыв.) */
    Person.compareAge = function(a, b){
        return a.age > b.age ? -1 : 1;
    }

    var rnd = function() {
        var min = 0;
        var max = 100;

        var rand = min - 0.5 + Math.random() * (max - min + 1)
        return Math.round(rand);
    }

    var storage = [];
    storage.push(new Person('Jonelle Lytch', rnd()));
    storage.push(new Person('Glenda Cabana', rnd()));
    storage.push(new Person('Alene Coomer', rnd()));
    storage.push(new Person('Isidro Trexler', rnd()));
    storage.push(new Person('Palmer Saffold', rnd()));
    storage.push(new Person('Lynne Mayse', rnd()));
    storage.push(new Person('Sandee Callihan', rnd()));
    storage.push(new Person('Theron Stroup', rnd()));
    storage.push(new Person('Tracy Criger', rnd()));
    storage.push(new Person('Ardath Chacko', rnd()));

    /* Перевод значений radio в функции сравнения */
    var modeToFunc = {
        'byname': Person.compareName,
        'byage': Person.compareAge
    };

    var update = function(){
        var modeNode = root.querySelector('input[name="mode"]:checked');
        console.log(modeNode.value)
        resultNode.value = (storage
            .sort(modeToFunc[modeNode.value])
            .map(function(item){ return item.toString(); })
            .join("\n"));
    };

    root.addEventListener("click", update);

    update();
}

document.addEventListener("DOMContentLoaded", function(){
    sorter(document.querySelector(".sorter"))
});
