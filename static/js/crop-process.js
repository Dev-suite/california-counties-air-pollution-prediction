function uploadCrop(){
    $(".rotor").css("visibility" , "visible");
    let file =document.querySelector('#crop');
    let formData = new FormData();
    formData.append("file", file.files[0]);
    axios.post('/crop', formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    }).then((response) => {
        let prediction = response.data;
        document.getElementById("class").innerHTML = printObj(prediction)
        $(".rotor").css("visibility" , "hidden");
        $('#myModal').modal('show');
    })
    
}

let printObj = function(obj){
    var string = '';

    for(var prop in obj){
        if(typeof obj[prop] == 'string'){
            string += `${prop}: ${obj[prop]}% </br>`;
        }
        else{
            string += `${prop} : { </br> ${obj[prop]}%}`;
        }
    }
    return string;
}