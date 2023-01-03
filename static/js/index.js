let inputText = document.querySelector("#text");
let selectOne = document.querySelector("#ml-models");
let selectTwo = document.querySelector("#dl-models");
let buttonSelect = document.querySelector("#submitBtn");
selectOne.addEventListener("change", () => {  
  if (selectOne.value!="") {
    selectTwo.disabled = true;
    return false; }  
else {
    selectTwo.disabled = false;
    return false;
}
})
selectTwo.addEventListener("change", () => {  
    if (selectTwo.value!="") {
        selectOne.disabled = true;
        return false;       
    } else {
        selectOne.disabled = false;
        return false;
    }
  })
  buttonSelect.addEventListener("click",()=>{    
    if(inputText.value!="") {
        document.querySelector(".table").id="showTable";
        return false;
        
    } 
  })