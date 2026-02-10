LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "[%(levelname)s] - %(asctime)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "formatter": "default",
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "filename": "app_log.log",
            "mode": "a",
        },
    },
    "loggers": {
        "metal_price_logger": {
            "handlers": ["file", "console"],
            "level": "DEBUG",
            "propagate": False,
        }
    },
}
