from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")

goldapp = Flask(__name__)

if __name__ == '__main__':
	logger.debug("Starting the application...")
	from gold_rate_registry import *
	goldapp.run(debug=True)              



