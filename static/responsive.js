/*code for responsive navbar*/
burger = document.querySelector('.burger')
navbar = document.querySelector('.navbar')
navlist = document.querySelector('.navlist')
rightnav = document.querySelector('.rightnav')

burger.addEventListener('click', ()=>{
    rightnav.classList.toggle('v-class-resp');
    navlist.classList.toggle('v-class-resp');
    navbar.classList.toggle('nav-height-resp');
})

/*code for responsive login and reg form*/
function register(){
    document.location.href="candireg";
}

function comp_register(){
    document.location.href="compreg";
}

function login(){
    document.location.href="candilogin";
}

function comp_login(){
    document.location.href="complogin";
}

// redirect to resume page

// function regtores(){
//     document.location.href="resumeform";
// }

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
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