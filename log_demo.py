import log_demo
import logging
logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

#create logger
mylog = logging.getLogger("MyMLProject")
mylog.setLevel(logging.DEBUG)

if not mylog.handlers:
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s-%(message)s"
    )
    #save logs to file
    file_handler = logging.FileHandler("my_project.log",mode="a")
    file_handler.setFormatter(formatter)

    #show log in terminals
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    mylog.addHandler(file_handler)
    mylog.addHandler(console_handler)

    mylog.debug("Logger is set up and ready")
    mylog.info("Starting Ml pipeine")
    mylog.warning("Dataset has some missing values")
    mylog.error("Failed to load model")
    mylog.critical("GPU not found")

    # create logger
    mylog = logging.getLogger("MyMLProject")
    mylog.setLevel(logging.DEBUG)

    if not mylog.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s-%(message)s"
        )
        # save logs to file
        file_handler = logging.FileHandler("my_project.log", mode="a")
        file_handler.setFormatter(formatter)

        # show log in terminals
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        mylog.addHandler(file_handler)
        mylog.addHandler(console_handler)
    #function
def divide(a,b):
    try:
     return a/b#Handle division by zero
    except ZeroDivisionError:
     return None
print(divide(20,2))
divide(10,0)



