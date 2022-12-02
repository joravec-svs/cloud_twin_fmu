from datetime import datetime
from flask import request
import base64

from app import app,db
from app.fmu import Fmu
from app.models import VirtualData

@app.route("/", methods=["POST"])
def index():
    envelope = request.get_json()
    print(envelope)
    if not envelope:
        msg = "no Pub/Sub message received"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if not isinstance(envelope, dict) or "message" not in envelope:
        msg = "invalid Pub/Sub message format"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    pubsub_message = envelope["message"]
    if isinstance(pubsub_message, dict) and "data" in pubsub_message:
        data = base64.b64decode(pubsub_message["data"]).decode("utf-8").strip()

    inputdata = data["attributes"]
    time = data["timestamp"]

    name = app.config["FMU_NAME"]
    inputs = app.config["INPUTS"]
    outputs = app.config["OUTPUTS"]
    start_time = app.config["START_TIME"]
    stop_time = app.config["STOP_TIME"]
    step_size = app.config["STEP_SIZE"]
    output_interval = app.config["OUTPUT_INTERVAL"]
    
    fmu = Fmu(name,inputs,outputs,start_time,stop_time,step_size,output_interval)
    inputs = list(inputdata.values())
    fmu_results = fmu.run_fmu(inputs)
    fmu_results["datetime"] = time
    print(fmu_results)
    virtualdata = VirtualData(fmu_results)
    print(virtualdata.datetime)
    db.session.add(virtualdata)
    db.session.commit()

    
    if isinstance(pubsub_message, dict) and "data" in pubsub_message:
        name = base64.b64decode(pubsub_message["data"]).decode("utf-8").strip()
        print(name)

    return ("", 204)
