var plus = document.getElementById("plus")
var munis = document.getElementById("minus")
var div = document.getElementById("div")
var multiple = document.getElementById("multiple")
var equal = document.getElementById("equal")
var end;
plus.addEventListener("click",function(){
    var txt1 = document.getElementById("txt1")
    var txt2 = document.getElementById("txt2")
    var number1 = parseInt(txt1.value)
    var number2 = parseInt(txt2.value)
    end = number1+number2
});
minus.addEventListener("click",function(){
    var txt1 = document.getElementById("txt1")
    var txt2 = document.getElementById("txt2")
    var number1 = parseInt(txt1.value)
    var number2 = parseInt(txt2.value)
    end = number1-number2
});
equal.addEventListener("click",function(){
    var txt3 = document.getElementById("txt3")
    var number3 = parseInt(txt3.value)
    if (number3==end){
    alert(true)
    }
    else{
    alert(false)
    }
})

