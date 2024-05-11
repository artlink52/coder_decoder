from ConfigReaderInterface import ConfigReaderInterface
from ConfigException import ConfigException
import re

class ConfigReader(ConfigReaderInterface):
    def read_config(self, config_file_name: str) -> dict:
        keys = {self.buffer_size_param_name, self.file_name_for_coder_param_name, self.coder_run_option_param_name}
        config_dict = {}

        with open(config_file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.split(" " + self._param_delimiter + " ")
                value = re.sub(r"\n", "", value)
                if key in keys:
                    keys.remove(key)
                    if key == self.coder_run_option_param_name and not (value == "code" or value == "decode"):
                        raise ConfigException("Coder_option must be 'code' or 'decode'!")
                    elif key == self.buffer_size_param_name:
                        value = int(value)
                    config_dict[key] = value

                else:
                    raise ConfigException("Unknown parameter: {}".format(key) )

            if len(keys) > 0:
                raise ConfigException("Missed parameters: " + "".join(str(i) + " " for i in keys))

        return config_dict
