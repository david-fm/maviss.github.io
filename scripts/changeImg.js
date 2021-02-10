const img = document.querySelector(".background");
addEventListener("resize", responsive)
responsive();
function responsive()
{
    let width = window.screen.availWidth;
    let height = window.screen.availHeight;
    if( (width)/(height) < 0.65)
    {
        img.setAttribute("src", "./assets/media/img/_MG_4679.jpg");
    }
        else if( ((width)/(height) > 0.65) && ((width)/(height) < 1.1))
        {
            img.setAttribute("src", "./assets/media/img/Galery/_MG_5405.jpg");
        }
            else if( (width)/(height) > 1.1 )
            {
                img.setAttribute("src", "./assets/media/img/Galery/_MG_5381.jpg");
            }
}