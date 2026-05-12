from flask import Flask, request

app = Flask(__name__)

MAINTENANCE = False

@app.route("/")
def home():
  return "Server Is Alive"

@app.route("/health", methods = ["GET","HEAD"])
def health():
  return "OK"

#Pump Calibration
@app.route("/calculation", methods = ["GET"])
def calculation ():
  if MAINTENANCE:
    return str("Service Unavailable!")
    
  vol = float(request.args.get("vol"))
  time1 = float(request.args.get("time1"))
  time2 = float(request.args.get("time2"))
  time3 = float(request.args.get("time3"))
  avg = (time1 + time2 + time3) / 3
  result = ((vol / 1000) * 3600) / avg
  return str(round(result,1))

#Simple math
@app.get("/add")
def add():
  if MAINTENANCE:
    return str("Service Unavailable!")
    
  a = float(request.args.get("a"))
  b = float(request.args.get("b"))
  result = a + b
  return str(round(result, 1))
    
@app.get("/subtraction")
def subtraction():
  if MAINTENANCE:
    return str("Service Unavailable!")
    
  key = str(request.args.get("key"))

  if key != "VIP120":
      return "Access Denied!"

  a = float(request.args.get("a"))
  b = float(request.args.get("b"))
  result = a - b
  return str(round(result, 1))

@app.get("/multiply")
def multiply():
  if MAINTENANCE:
    return str("Service Unavailable!")
    
  key = str(request.args.get("key"))

  if key != "VIP121":
      return "Access Denied!"
        
  a = float(request.args.get("a"))
  b = float(request.args.get("b"))
  result = a * b
  return str(round(result, 1))

@app.get("/divide")
def divide():
  if MAINTENANCE:
    return str("Service Unavailable!")
    
  key = str(request.args.get("key"))

  if key != "VIP122":
      return "Access Denied!"
        
  a = float(request.args.get("a"))
  b = float(request.args.get("b"))
  result = a / b
  return str(round(result, 1))
