function getPlotData(county, parameter) {
  var plotData;
  // Make prediction by calling api /predict

  axios
    .get("/predict", {
      params: {
        county: county,
        parameter: parameter,
      },
    })
    .then(function (response) {
      plotData = response.data.predicted;
      plotData = plotData.toFixed(2);
      var history = [];
      history = response.data.history;
      parameter = response.data.parameter;
      history = history[29];
      history = history.toFixed(2);
      display(plotData, history, parameter);
    })
    .catch(function (error) {
      console.log(error);
    });
}

function plot(prediction, parameter) {
  var color = "";
  var status = "";
  if (parameter == "pm25") {
    if (prediction >= 0) {
      if (prediction >= 0 && prediction <= 10) {
        color = "#56ac39";
        status = "Good";
      }

      if (prediction > 10 && prediction <= 20) {
        color = "#80cc66";
        status = "Fair";
      }

      if (prediction > 20 && prediction <= 25) {
        color = "#80cc66";
        status = "Moderate";
      }

      if (prediction > 25 && prediction <= 50) {
        color = "#ff8c1a";
        status = "Poor";
      }

      if (prediction > 50 && prediction <= 75) {
        color = "#ff1a1a";
        status = "Very Poor";
      }

      if (prediction > 75) {
        color = "#800000";
        status = "Extremely Poor";
      }
    } else {
      color = "#ffffff";
      status = "Error fetching prediction";
    }
  }

  if (parameter == "aqi") {
    if (prediction >= 0) {
      if (prediction >= 0 && prediction <= 50) {
        color = "#56ac39";
        status = "Good";
      }

      if (prediction > 50 && prediction <= 100) {
        color = "#80cc66";
        status = "Moderate";
      }

      if (prediction > 100 && prediction <= 150) {
        color = "#80cc66";
        status = "Unhealthy for Sensitive Groups";
      }

      if (prediction > 150 && prediction <= 200) {
        color = "#ff8c1a";
        status = "Unhealthy";
      }

      if (prediction > 200 && prediction <= 300) {
        color = "#ff1a1a";
        status = "Very Unhealthy";
      }

      if (prediction > 300) {
        color = "#800000";
        status = "Hazardous";
      }
    } else {
      color = "#ffffff";
      status = "Error fetching prediction";
    }
  }

  if (parameter == "co") {
    color = "#80cc66";
    status = "";
  }

  data = [];
  data[0] = color;
  data[1] = status;
  return data;
}

function display(data, history, parameter) {
  // update();
  pm25unit = "<span>μg/m<sup>3</sup></span>";
  coUnit = "<span>PPM</span>";
  var prediction = [];
  var historyValue = [];
  prediction = plot(data, parameter);
  historyValue = plot(history, parameter);

  predColor = prediction[0];
  predStatus = prediction[1];

  histColor = historyValue[0];
  histStatus = historyValue[1];
  tag = document.getElementById("nowdiv");
  predTag = document.getElementById("prediction");
  statusTag = document.getElementById("status");

  // cardTag = document.getElementById('card')
  // cardTag.style.backgroundColor = color;
  tag.style.backgroundColor = histColor;
  if (parameter == "co") {
    predTag.innerHTML = data + coUnit;
  }

  if (parameter == "pm25" || parameter == "aqi") {
    predTag.innerHTML = data + pm25unit + " - " + predStatus;
  }

  if (parameter == "aqi") {
    predTag.innerHTML = data + " - " + predStatus;
  }

  // statusTag.innerHTML = predStatus;

  var today = new Date();
  var date =
    today.getFullYear() + "-" + (today.getMonth() + 1) + "-" + today.getDate();
  var time = today.getHours() + ":" + today.getMinutes();
  var currentTime = date + " " + time;

  hour = document.getElementById("current-time");
  hour.innerHTML = currentTime;
  hourTag = document.getElementById("nextdiv");
  currentTag = document.getElementById("current-hour");
  statusHour = document.getElementById("status-hour");
  hourTag.style.backgroundColor = predColor;
  if (parameter == "co") {
    currentTag.innerHTML = history + coUnit + " - " + histStatus;
  }

  if (parameter == "pm25") {
    currentTag.innerHTML = history + pm25unit + " - " + histStatus;
  }

  if (parameter == "aqi") {
    currentTag.innerHTML = history + " - " + histStatus;
  }

  $(".rotor").css("visibility", "hidden");
  // statusHour.innerHTML = histStatus
  // cityTag = document.getElementById('navbarDropdownMenuLink');
  // cityTag.innerHTML = city
  // cityTag.style.backgroundColor = predColor;
}

// function update(){
//     var element = document.getElementById("myprogressBar");
//     var width = 1;
//     var identity = setInterval(scene, 10);

//     function scene() {
//         if (width >= 100) {
//           clearInterval(identity);
//         } else {
//           width++;
//           element.style.width = width + '%';
//           element.innerHTML = width * 1  + '%';
//         }
//       }
// }
