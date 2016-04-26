from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time
import os

value = False
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, value)
print ("see of course it prints")
res = os.popen('vcgencmd measure_temp').readline()
print(res)

def writeToFile():
        global value
        global res
        text_file = open("output.txt","w")
        text_file.write(str(res))
        text_file.close()

writeToFile()

app = Flask(__name__)

@app.route('/')
def index():
        global value
        if(value):
                onoff = "on"
        else:
                onoff = "off"
        global res
        return render_template('index.html', var = res, on = onoff)
        
def changeStat():
        global value
        print("test")
        if (value):
                value = False
        else:
                value = True
       #GPIO.setup(11, GPIO.OUT)
        GPIO.output(11, value)
        index()
        #time.sleep(10)

@app.route('/Worth', methods=['GET', 'POST'])
def worthy():
        if request.method == 'GET':
                print("ITS GETTING This")
                changeStat()
        return render_template('Worth.html')
        #else:
                #changeStat() 
                
if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
