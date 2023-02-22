let countEl = document.getElementById("count-el")
let savedEl = document.getElementById("saved-el")

let count = 0;

function increment(){
    count = count + 1;
    countEl.innerText = count;
}

function save (){
    let countStr = count + "-"
    savedEl.innerText+=countStr;
    countEl.innerText=0;
    count=0;
}

