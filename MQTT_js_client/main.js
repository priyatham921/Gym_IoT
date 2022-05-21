window.onload = function () {
  navigator.permissions
    .query({ name: "accelerometer" })
    .then(function (result) {
      if (result.state == "granted") {
        console.log("access granted!!!");
        let sensor = new Accelerometer();
        console.log("test1");
        sensor.start();
        console.log("test2");
        sensor.onreading = () => {
          document.getElementById("acc_data_x").innerHTML = sensor.x;
          document.getElementById("acc_data_y").innerHTML = sensor.y;
          document.getElementById("acc_data_z").innerHTML = sensor.z;
          //console.log("Acceleration along X-axis: " + sensor.x);
          //console.log("Acceleration along Y-axis: " + sensor.y);
          //console.log("Acceleration along Z-axis: " + sensor.z);
        };

        sensor.onerror = (event) =>
          console.log(event.error.name, event.error.message);
      } else console.log("permission denied");
    });
};
