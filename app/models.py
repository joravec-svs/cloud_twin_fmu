from app import db
from datetime import datetime, timedelta

class InputData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valve_value = db.Column(db.Float)

    def __init__(self,data):
        for k,v in data.items():
            if k in vars(InputData):
                setattr(self,k,v)

    def to_dict(self):
        data = {k:v for k,v in self.__dict__.items() if not k.startswith('__') and not k in ['id', 'to_dict','_sa_instance_state']}
        return data

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    pressure1 = db.Column(db.Float)
    pressure2 = db.Column(db.Float)
    flow1 = db.Column(db.Float)
    flow2 = db.Column(db.Float)
    temperature = db.Column(db.Float)
    valve_position = db.Column(db.Float)

    def __init__(self,data):
        for k,v in data.items():
            if k == "datetime":
                v = datetime.fromisoformat(v)
            if k in vars(SensorData):
                setattr(self,k,v)

    def to_dict(self):
        data = {k:v for k, v in self.__dict__.items() if not k.startswith('__') and not k in ['id', 'to_dict','_sa_instance_state']}
        return data

class VirtualData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    Ball_Valve_Pressure_drop = db.Column(db.Float)
    Bend_Pressure_drop = db.Column(db.Float)
    Control_Valve_Static_pressure_diff = db.Column(db.Float)
    Pump_pressure_rise = db.Column(db.Float)
    ManometrMonitor = db.Column(db.Float)
    FlowMonitor1 = db.Column(db.Float)
    FlowMonitor2 = db.Column(db.Float)
    PressureMonitor1 = db.Column(db.Float)
    PressureMonitor2 = db.Column(db.Float)

    def __init__(self,data):
        for k,v in data.items():
            if k == "datetime":
                v = datetime.fromisoformat(v)
            if k in vars(VirtualData):
                setattr(self,k,v)

    def to_dict(self):
        data = {k:v for k, v in VirtualData.__dict__.items() if not k.startswith('__') and not k in ['id', 'to_dict','_sa_instance_state']}
        return data
