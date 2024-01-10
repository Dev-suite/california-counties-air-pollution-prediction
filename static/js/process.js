function uploadFile(){
    $(".rotor").css("visibility" , "visible");
    let checkbox = document.getElementById("compress");
    let file = document.querySelector('#wild');
    var formData = new FormData();
    formData.append("file", file.files[0]);
    console.log(checkbox.checked)
    if(checkbox.checked == true){
        axios.post('/upload/compress', formData, {
            headers: {
            'Content-Type': 'multipart/form-data'
            }
        }).then((response) => {
            console.log(response.data.destination);
            
            let downloadFile = `static/outputs/${response.data.destination}`
            console.log(downloadFile)
            Download(downloadFile);
            $(".rotor").css("visibility" , "hidden")
    
        }).catch((error)=>{
            console.log(error);
        })

    }
    else{
        axios.post('/upload/uncompress', formData, {
            headers: {
            'Content-Type': 'multipart/form-data'
            }
        }).then((response) => {
            console.log(response.data.destination);
            
            let downloadFile = `static/outputs/${response.data.destination}`
            console.log(downloadFile)
            Download(downloadFile);
            $(".rotor").css("visibility" , "hidden")
    
        }).catch((error)=>{
            console.log(error);
        })

    }
    

}

function uploadFire(){
    $(".rotor").css("visibility" , "visible");
    let file = document.querySelector("#fire");
    let formData = new FormData();
    formData.append("file", file.files[0]);
    axios.post('/fire', formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    }).then((response) => {
        console.log(response.data.destination);
            
            let downloadFile = `static/outputs/${response.data.destination}`
            console.log(downloadFile)
            Download(downloadFile);
            $(".rotor").css("visibility" , "hidden")

    }).catch((error)=>{
        console.log(error);
    })

}

function uploadImage(){
    $(".rotor").css("visibility" , "visible");
    let file = document.querySelector('#animal');
    let formData = new FormData();
    formData.append("file", file.files[0]);
    axios.post('/animal', formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    }).then((response) => {
        console.log(response)
        let prediction = response.data;
        document.getElementById("class").innerHTML = printObj(prediction)
        $(".rotor").css("visibility" , "hidden")
    })
}

function Download(url) {
    document.getElementById('my_iframe').src = url;
};

// function showLoading(time) {
//     var $src = $(".popup img").attr("src");
//         $(".show").fadeIn();
//         $(".img-show img").attr("src", $src);
//     // document.getElementById("loadDiv").style.display="block";
//     setTimeout("hide()", (time * 1000));  //5000 = 5 seconds
// }

// function hide() {
//     $(".show").fadeOut();
//     // document.getElementById("loadDiv").style.display="none";
// }

var printObj = function(obj) { 
    var string = ''; 

    for(var prop in obj) { 
        if(typeof obj[prop] == 'string') { 
            string += `${prop}: ${obj[prop]}% </br>`;
            // string+= prop + ': ' + obj[prop]+'; </br>'; 
        } 
        else { 
            string+= `${prop} : { </br> ${obj[prop]}%}`;
            // string+= prop + ': { </br>' + print(obj[prop]) + '}'; 
        } 
    } 

    return string; 
} 