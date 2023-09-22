from flask import Flask
from src.logger import logging 
from src.exception import CustomException
app = Flask(__name__)
import os,sys

@app.route('/',methods= ['GET','POST'])

def index():

    try:
        raise Exception("We are testing our exception file ") #error 
    except Exception as e:
        ML=CustomException(e,sys)
        logging.info(ML.error_message,)

    logging.info("Testing the logging file ")

    return "Welcome to Modular programming "

if __name__ == '__main__':
    app.run(debug =True) #5000
    