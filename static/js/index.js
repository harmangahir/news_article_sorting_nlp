let inputText = document.querySelector("#text");
let selectOne = document.querySelector("#ml-models");
let selectTwo = document.querySelector("#dl-models");
let buttonSelect = document.querySelector("#submitBtn");

function selectOne() {
  if (selectOne.value!="") {
    selectTwo.disabled = true;
    }  
else {
    selectTwo.disabled = false;
  }
  return false;
}

function selectTwo() {
  if (selectTwo.value!="") {
    selectOne.disabled = true;
    alert('select Two')
           
} else {
    selectOne.disabled = false;
    
}
    return false;
}

function dataSent() {
  if(inputText.value!="") {
    document.querySelector(".table").id="showTable";
  } 
return false;
}
