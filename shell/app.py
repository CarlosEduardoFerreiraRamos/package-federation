
from importlib import import_module
import os
from pyclbr import Function
from types import ModuleType
from typing import Dict

EXTERNAL_APP = 'EXTERNAL_APP'

EXTERNAL_CONFIGURATION = 'config'

EXTERNAL_CONFIG_APP = 'apps'

EXTERNAL_APP_MODULE = 'app_module'

EXTERNAL_APP_CALLEBLE = 'run_app'

def load_module(module_name: str, default_value: str = None) -> ModuleType:
    module_path = os.environ.get(module_name, default_value)
    return import_module(module_path)

def load_config(app_module: ModuleType) -> Dict:
    return getattr(app_module, EXTERNAL_CONFIGURATION, None)

def load_app(aplication: Dict) -> Function:
    app_module = import_module(aplication.get(EXTERNAL_APP_MODULE))
    return getattr(app_module, aplication.get(EXTERNAL_APP_CALLEBLE), None)

def exec():
    # load a module installed in the python environment
    loaded_module = load_module(EXTERNAL_APP)
    # extract the config variable from the loaded module
    loaded_conf = load_config(loaded_module)
    # interate over the the application list
    for application in loaded_conf.get(EXTERNAL_CONFIG_APP):    
        # extract the function from the external module
        app_function = load_app(application)
        app_function()

# execute
exec()