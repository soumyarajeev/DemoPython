var s2Clone;

// Doesn't work in older IEs
//CLone the Dependant drop down and hide
document.addEventListener('DOMContentLoaded', function(){
   s2Clone = document.getElementById("s2").cloneNode(true);
   document.getElementById("s2").innerHTML = "";
}, false);

document.getElementById("s1").onchange = function() {
  var selected = this.value;

  //Get the nodes with a parent attribute of the selected data
  var optionsToInsert = s2Clone.querySelectorAll("[data-parent='" + selected +"']");
  //clear existing
  var s2 = document.getElementById("s2");
  s2.innerHTML = "";

  //Add The new  options.
  for(i = 0; i < optionsToInsert.length; i++)
  {
    s2.appendChild(optionsToInsert[i]);
  }

}

