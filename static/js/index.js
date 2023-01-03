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

  element.addEventListener("change", (e) => {
    const value = e.target.value;
    const text = element.options[element.selectedIndex].text;
   
    if (value) {
      document.getElementById("pick").textContent = `Value Selected: ${value}`;
    } else {
      document.getElementById("pick").textContent = "";
    }
  });