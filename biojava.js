
function bigImg(x) {
  x.style.height= "150px";
  x.style.width= "1000px";
}

function normalImg(x) {
  x.style.height= "70px";
  x.style.width= "1200px";
}



function bigImg5(x) {
  x.style.height= "100px";
  x.style.width= "1000px";
}

function normalImg5(x) {
  x.style.height= "60px";
  x.style.width= "1200px";
}

function bigImg2(x) {
  x.style.height= "50px";
  x.style.width= "1000px";
}

function normalImg2(x) {
  x.style.height= "30px";
  x.style.width= "1200px";
}


function bigImg3(x) {
  x.style.height= "50px";
  x.style.width= "1000px";
}

function normalImg3(x) {
  x.style.height= "30px";
  x.style.width= "1200px";
}


function bigImg4(x) {
  x.style.height= "50px";
  x.style.width= "1000px";
}

function normalImg4(x) {
  x.style.height= "30px";
  x.style.width= "1200px";
}










var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
