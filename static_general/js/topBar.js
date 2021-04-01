const HAMBURGER = document.querySelector(".nav");
const NAV = document.querySelector(".nav_container");
const TOP = document.querySelector(".flex_header");

NAV.style.top = "-100vh";

HAMBURGER.addEventListener("click", ()=>
{
    if(NAV.style.top == "-100vh")
    {
        NAV.style.top ="10vh";
        TOP.style.background ="#000000bf"
    }
    else
    {
        NAV.style.top = "-100vh";
        TOP.style.background = "#00000000"
    }
})