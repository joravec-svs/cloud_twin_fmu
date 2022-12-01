from fmpy import simulate_fmu, read_model_description
from fmpy.fmi1 import FMICallException
import pkg_resources

class Fmu():
    def __init__(self,name,inputs,outputs,start_time,stop_time,step_size,output_interval):
        self.name = name
        self.filename = pkg_resources.resource_filename('app',f"static/{self.name}")
        self.inputs = inputs
        self.outputs = outputs
        self.start_time = start_time
        self.stop_time = stop_time
        self.step_size = step_size
        self.output_interval = output_interval

    def __del__(self):
        print(f"{self.name} fmu deleted!")

    def __str__(self):
        return f"{self.name} inputs:{self.inputs}, outputs:{self.outputs}"

    def __repr__(self):
        return f"Fmu({self.name!r},{self.inputs!r},{self.outputs!r})"

    def run_fmu(self,start_values):
        start_dict = dict(zip(self.inputs,start_values))
        try:
            result = simulate_fmu(
                filename=self.filename,
                validate=False,
                start_time=self.start_time,
                stop_time=self.stop_time,
                step_size=self.step_size,
                output_interval=self.output_interval,
                start_values=start_dict)
        except FMICallException:
            print("Values out of bounds!")
            return None
        else:
            res = list(result[-1])
            res_dict = dict(zip(self.outputs,res[1:]))
            print("FMU results calculated succesfully")
            return res_dict
