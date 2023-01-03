let inputText = document.querySelector("#text");
let selectOne = document.querySelector("#ml-models");
let selectTwo = document.querySelector("#dl-models");
let buttonSelect = document.querySelector("#submitBtn");

function selectOne() {
  alert('selectOne')
  if (selectOne.value!="") {
    selectTwo.disabled = true;
    }  
else {
    selectTwo.disabled = false;
  }
  return false;
}

function selectTwo() {
  alert('selectTwo')
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

const btn = document.getElementById('submitBtn');

btn.addEventListener('click', () => {
  const form = document.getElementById('form');

  if (form.style.visibility === 'hidden') {
    form.style.visibility = 'visible';
  } else {
    form.style.visibility = 'hidden';
  }
});