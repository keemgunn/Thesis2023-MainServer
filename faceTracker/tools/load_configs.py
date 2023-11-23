import os
import yaml

def load():
    
    #### Determine the path to the configuration file ####
    if os.name == 'nt':
        # Windows
        file_path = os.path.join(os.path.dirname(__file__), '../../configs/Windows/configs.yml')
    elif os.name == 'posix':
        # MacOS
        file_path = os.path.join(os.path.dirname(__file__), '../../configs/MacOS/configs.yml')
    else:
        raise OSError('OS not supported')
    
    with open(file_path, 'r') as f:
        configs = yaml.safe_load(f)

    return configs
