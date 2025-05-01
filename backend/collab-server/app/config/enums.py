from enum import Enum

class LogLevelEnum(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
    
class AppEnvironmentEnum(str, Enum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"
    TESTING = "testing"