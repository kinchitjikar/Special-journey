function changeLanguage(language) {
	var element = document.getElementById("url");
	element.value = language;
	element.innerHTML = language;
}

function showDropdownTodo(no) {
	var menu = "myDropdown" + no;
	console.log(menu);
	var drops = document.getElementsByClassName('dropdown-content show');
	for (i = 0; i < drops.length; i++) {
		drops[i].classList.toggle('show');
	}
	document.getElementById(menu).classList.toggle("show");
}

 //Close the dropdown if the user clicks outside of it
 window.onclick = function (event) {
 	if (!event.target.matches('.dropbtn')) {
 		var dropdowns = document.getElementsByClassName("dropdown-content");
 		var i;
 		for (i = 0; i < dropdowns.length; i++) {
 			var openDropdown = dropdowns[i];
 			if (openDropdown.classList.contains('show')) {
 				openDropdown.classList.remove('show');
 			}
 		}
 	}
 }

 function todosave() {
 	var x = document.getElementById('titletext').value;
 	var y = document.getElementById('datepicker').value;
 	if (x == "") {
 		alert("Please enter Title");
 		return false;
 	}
 	else if (y == "") {
 		document.getElementById('dateError').innerHTML = "Please Enter Date";
 		return false;
 	}
 	else {
 		document.getElementById('textidtodo').innerHTML = x;
 		document.getElementById('datepicker').innerHTML = y;
 	}
 	document.getElementById('lg').style.display = "block";

 	document.getElementById('titletext').value = "";
 	document.getElementById('datepicker').value = "";
 	document.getElementById('time').value = "";
 	document.getElementById('description').value = "";
 }


 function movetodoing() {
 	var m_t_doing = document.getElementById('marktodoing');
 	if (m_t_doing) {
 		document.getElementById('uldoing').append(document.getElementById('firstli'));
 	}
 }

 function movetodone() {
 	var m_t_done = document.getElementById('marktodone');
 	if (m_t_done) {
 		document.getElementById('uldone').append(document.getElementById('firstli'));
 	}
 }

 function movetotodo() {
 	var m_t_todo = document.getElementById('marktoto')
 }