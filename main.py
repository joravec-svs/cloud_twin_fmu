from app import app, db
from app.models import SensorData,InputData,VirtualData

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'SensorData': SensorData, 'InputData': InputData, 'VirtualData': VirtualData}