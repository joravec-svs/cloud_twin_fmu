import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """Base config."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'svs-fem-secret-key1234'
    FMU_NAME = "HydraulicSystem.fmu"
    INPUTS = ["Ansi_Control_Valve_Fraction_opening__0_1_"]
    OUTPUTS = ["Control_Valve_Static_pressure_diff","Ball_Valve_Pressure_drop","Bend_Pressure_drop","FlowMonitor1",
            "FlowMonitor2","Pump_pressure_rise","ManometrMonitor","PressureMonitor1","PressureMonitor2"]
    START_TIME = 0
    STOP_TIME = 0.1
    STEP_SIZE = 0.1
    OUTPUT_INTERVAL = 0.1

class ProdConfig(Config):
    FLASK_DEBUG = False
    TESTING = False
    INSTANCE_NAME = os.environ.get('INSTANCE_NAME')
    PROJECT_ID = os.environ.get('PROJECT_ID')
    DB_PASS = os.environ.get('DB_PASS')
    DB_USER = os.environ.get('DB_USER')
    DBNAME = os.environ.get('DBNAME')
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevConfig(Config):
    FLASK_DEBUG = True
    TESTING = True

    PUBLIC_IP_ADDRESS = "127.0.0.1:3306"
    DB_PASS = os.environ.get('DB_PASS')
    DB_USER = os.environ.get('DB_USER')
    DBNAME = os.environ.get('DBNAME')
    PROJECT_ID = os.environ.get('PROJECT_ID')
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{PUBLIC_IP_ADDRESS}/{DBNAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    