class ConfigDB:
    
    USER = 'root'
    PASSWORD = '290307'
    HOST = 'localhost'
    DATABASE = 'interfichas'
    
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False