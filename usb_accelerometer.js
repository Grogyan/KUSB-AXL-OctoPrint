$(function() {
    function USBAccelerometerViewModel(parameters) {
        var self = this;

        self.settings = parameters[0];

        self.onBeforeBinding = function() {
            self.serialPort = ko.observable(self.settings.settings.plugins.usb_accelerometer.serial_port());
        };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: USBAccelerometerViewModel,
        dependencies: ["settingsViewModel"],
        elements: ["#settings_plugin_usb_accelerometer"]
    });
});
