from flask_restful import Api
from gold_rate import goldapp 
from .Task import Task
import requests

restserver = Api(goldapp)

restserver.add_resource(Task,"/goldrate")






