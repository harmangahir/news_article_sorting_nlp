let inputText = document.querySelector("#text");
let selectOne = document.querySelector("#ml-models");
let selectTwo = document.querySelector("#dl-models");
let buttonSelect = document.querySelector("#submitBtn");
selectOne.addEventListener("change", () => {  
  if (selectOne.value!="") {
    selectTwo.disabled = true;
} else {
    selectTwo.disabled = false;
}
})
selectTwo.addEventListener("change", () => {  
    if (selectTwo.value!="") {
        selectOne.disabled = true;       
    } else {
        selectOne.disabled = false;
    }
  })
  buttonSelect.addEventListener("click",()=>{    
    if(inputText.value!="") {
        document.querySelector(".table").id="showTable"
        
    } 
  })

  function sendModelInfo(){
    let modelinfo = document.getElementById('ml-models').value
    console.log(modelinfo)
  }