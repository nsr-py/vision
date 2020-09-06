from flask import Flask
from flask_restful import Resource, Api
#import grovepi 


#for pins
from gpiozero import DistanceSensor
from time import sleep
from gpiozero import LED

sensor_r = DistanceSensor(16, 20)
sensor_l = DistanceSensor(10, 9)
sensor_f = DistanceSensor(23, 24)
right = LED(25)
left = LED(8)
front = LED(7)
right.off()
left.off()
front.off()
app = Flask(__name__)
api = Api(app)
sensor = 7

class TempHum(Resource):
    def get(self):
         dis_r = sensor_r.distance
         dis_l = sensor_l.distance
         dis_f = sensor_f.distance
         #[temp,hum] = grovepi.dht(sensor,0)
         left,right,front = dis_l,dis_r,dis_f
         print(left,right,front)
         return {'front' : dis_f,
                 'left' : dis_l,
                 'right' : dis_r}

api.add_resource(TempHum, '/')

#if __name__ = "__main__":
app.run(host='0.0.0.0', port=80, debug=True)
