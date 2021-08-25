const id_month = [
  "JAN",
  "FEB",
  "MAR",
  "APR",
  "MAY",
  "JUN",
  "JUL",
  "AUG",
  "SEP",
  "OCT",
  "NOV",
  "DEC",
];
const id_day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"];

var dt = new Date();
document.getElementById("year").innerHTML = dt.getFullYear();
document.getElementById("month").innerHTML = id_month[dt.getMonth()];
document.getElementById("day").innerHTML = id_day[dt.getDay()];
document.getElementById("date").innerHTML = dt.getDate();
document.getElementById("time").innerHTML = dt.toLocaleTimeString();

setInterval(function() {
  var dt = new Date();
  document.getElementById("year").innerHTML = dt.getFullYear();
  document.getElementById("month").innerHTML = id_month[dt.getMonth()];
  document.getElementById("day").innerHTML = id_day[dt.getDay()];
  document.getElementById("date").innerHTML = dt.getDate();
  document.getElementById("time").innerHTML = dt.toLocaleTimeString();
}, 1000);
