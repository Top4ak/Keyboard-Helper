import json

class Settings():
    
    def __init__(self):
        with open('settings/setup.json') as file:
            #load saved data from setup
            data = json.load(file)
        
        self.update(data)

    def update(self, values):
        self._start_hk = values["start_hot_key"]
        self._stop_hk = values["stop_hot_key"]
        self._starting_delay = values["starting_delay"]
        self._inteval = values["interval"]
        self._random_factor = values["random_factor"]


        with open("settings/setup.json", "w") as file:
            json_format = json.dumps(values)
            file.write(json_format)

    def get_start_hk(self) -> str:
        return self._start_hk
    
    def get_stop_hk(self) -> str:
        return self._stop_hk
    
    def get_starting_delay(self) -> float:
        return self._starting_delay
    
    def get_inteval(self) -> float:
        return self._inteval
    
    def get_random_factor(self) -> float:
        return self._random_factor