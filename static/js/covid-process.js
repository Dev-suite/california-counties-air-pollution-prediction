function uploadXray(){
    $(".rotor").css("visibility" , "visible");
    let file =document.getElementById('file');
    let option = document.getElementById('type');
    let formData = new FormData();
    formData.append("file", file.files[0]);
    if (option.options[option.selectedIndex].text === 'X-Ray PA'){
        axios.post('/covid/xray', formData, {
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

    if (option.options[option.selectedIndex].text === 'CT'){
        axios.post('/covid/ct', formData, {
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