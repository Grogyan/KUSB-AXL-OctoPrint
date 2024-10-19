import octoprint.plugin
import serial
import threading

class USBAccelerometerPlugin(octoprint.plugin.StartupPlugin,
                             octoprint.plugin.TemplatePlugin,
                             octoprint.plugin.SettingsPlugin):

    def __init__(self):
        self.serial_port = None
        self._data_thread = None
        self._data_callback = None

    def on_after_startup(self):
        self._logger.info("USB Accelerometer Plugin started")
        try:
            self.serial_port = serial.Serial('/dev/ttyUSB0', 9600)
            self._start_data_thread()
        except serial.SerialException as e:
            self._logger.error(f"Failed to connect to serial port: {e}")

    def _start_data_thread(self):
        if self._data_thread is None:
            self._data_thread = threading.Thread(target=self._data_loop)
            self._data_thread.daemon = True
            self._data_thread.start()

    def _data_loop(self):
        while self.serial_port and self.serial_port.is_open:
            data = self.read_accelerometer_data()
            if data and self._data_callback:
                self._data_callback(data)

    def read_accelerometer_data(self):
        if self.serial_port is not None:
            try:
                data = self.serial_port.readline().decode('utf-8').strip()
                self._logger.info(f"Accelerometer data: {data}")
                return data
            except serial.SerialException as e:
                self._logger.error(f"Error reading from serial port: {e}")
        return None

    def get_settings_defaults(self):
        return {
            "serial_port": "/dev/ttyUSB0"
        }

    def get_template_configs(self):
        return [
            {"type": "settings", "custom_bindings": False}
        ]

__plugin_name__ = "USB Accelerometer Plugin"
__plugin_implementation__ = USBAccelerometerPlugin()
