const img_1 = document.getElementById("background_1");
const img_2 = document.getElementById("background_2");
const img_3 = document.getElementById("background_3");

addEventListener("resize", responsive)
responsive();
function responsive()
{
    let width = window.screen.availWidth;
    let height = window.screen.availHeight;

    if( (width)/(height) < 0.65)
    {
        img_1.setAttribute("style", "display:relative" );
        img_2.setAttribute("style", "display:none" );
        img_3.setAttribute("style", "display:none");
    }
        else if( ((width)/(height) > 0.65) && ((width)/(height) < 1.1))
        {
            img_1.setAttribute("style", "display:none" );
            img_2.setAttribute("style", "display:relative" );
            img_3.setAttribute("style", "display:none");
        }
            else if( (width)/(height) > 1.1 )
            {
                img_1.setAttribute("style", "display:none" );
                img_2.setAttribute("style", "display:none" );
                img_3.setAttribute("style", "display:relative");
            }
}