let inputText = document.querySelector("#text");
let selectOne = document.querySelector("#ml-models");
let selectTwo = document.querySelector("#dl-models");
let buttonSelect = document.querySelector("#submitBtn");

function selectedOne() {
  
  if (selectOne.value!="") {
    selectTwo.disabled = true;
    }  
else {
    selectTwo.disabled = false;
  }
  return false;
}

function selectedTwo() {
  if (selectTwo.value!="") {
    selectOne.disabled = true;
           
} else {
    selectOne.disabled = false;
    
}
    return false;
}