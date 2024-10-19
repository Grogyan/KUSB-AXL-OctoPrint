import octoprint.plugin
import serial

class USBAccelerometerPlugin(octoprint.plugin.StartupPlugin,
                             octoprint.plugin.TemplatePlugin,
                             octoprint.plugin.SettingsPlugin):

    def __init__(self):
        self.serial_port = None

    def on_after_startup(self):
        self._logger.info("USB Accelerometer Plugin started")
        self.serial_port = serial.Serial('/dev/ttyUSB0', 9600)

    def read_accelerometer_data(self):
        if self.serial_port is not None:
            data = self.serial_port.readline().decode('utf-8').strip()
            self._logger.info(f"Accelerometer data: {data}")
            return data
        return None

    def get_settings_defaults(self):
        return {}

    def get_template_configs(self):
        return [
            {"type": "settings", "custom_bindings": False}
        ]

__plugin_name__ = "USB Accelerometer Plugin"
__plugin_implementation__ = USBAccelerometerPlugin()
