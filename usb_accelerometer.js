$(function() {
    function USBAccelerometerViewModel(parameters) {
        var self = this;

        self.settings = parameters[0];
        self.serialPort = ko.observable();
        self.chart = null;
        self.dataPoints = [];

        self.onBeforeBinding = function() {
            self.serialPort(self.settings.settings.plugins.usb_accelerometer.serial_port());
            self.initChart();
        };

        self.initChart = function() {
            var ctx = document.getElementById('accelerometerChart').getContext('2d');
            self.chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [{
                        label: 'Accelerometer Data',
                        data: self.dataPoints,
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        x: {
                            type: 'linear',
                            position: 'bottom'
                        }
                    }
                }
            });
        };

        self.updateChart = function(data) {
            self.dataPoints.push(data);
            if (self.dataPoints.length > 100) {
                self.dataPoints.shift();
            }
            self.chart.update();
        };

        self.onDataReceived = function(data) {
            // Assuming data is a numeric value
            var parsedData = parseFloat(data);
            if (!isNaN(parsedData)) {
                self.updateChart(parsedData);
            }
        };

        // WebSocket or similar to receive data from the Python backend
        OctoPrint.socket.onMessage("plugin.usb_accelerometer.data", self.onDataReceived);
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: USBAccelerometerViewModel,
        dependencies: ["settingsViewModel"],
        elements: ["#settings_plugin_usb_accelerometer", "#accelerometerChart"]
    });
});
