$(document).ready(function(){

    
// CAROUSEL PAGE
// ID'S FOR EACH CAROUSEL TAB

$('#wesc, #atc, #fd').tab('show');
$('.carousel').carousel();
});

$(".nowdiv, .nextdiv").css({"width" : "80%", "height" : "50px", "backgroundColor" : "#434F53"});

// REAL TIME PREDICTION OVERHEAD PREDICTION BAR
// WILL CHAGE COLOR AS THE PERCENTAGE GETS HIGHER
$(".percentage").css({
    "width" : "80%",
    "height" : "50px",
    "backgroundColor" : "#949494",
    "color" : "white",
    "text-align" : "center",
    "justify-content" : "center"
});
// REAL TIME PREDICTION PERCENTAGE VALUE
// $(".number").value("0%");

// $(".number").css({"color" : "white", "font-size" : "40px"});




//   LOADING ANIMATION

// let now = document.getElementsByClassName("now");
// let next = document.getElementsByClassName("next");



// $(".load").click(function(){

        
//         if (next.innerHTML == "" && now.innerHTML == "" ){
//             $(".rotor").css("visibility" , "visible");
//         }
//         else{
//             $(".rotor").css("visibility" , "hidden");
    
//         }
//     }
    
// );




 