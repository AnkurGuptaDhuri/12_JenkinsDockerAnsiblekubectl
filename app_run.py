from flask import Flask
from mypackage import application

if __name__=='__main__':
    application.run(host='0.0.0.0',port=5000)