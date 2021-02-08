const img = document.querySelector(".background");

if( (window.screen.width)/(window.screen.height) > 0.65)
{
    img.setAttribute("src", "./assets/media/img/Galery/_MG_5405.jpg");
}
if( (window.screen.width)/(window.screen.height) > 1.1)
{
    img.setAttribute("src", "./assets/media/img/Galery/_MG_5381.jpg");
    img.style.height= "auto";
    img.setAttribute("width", "100%");
}