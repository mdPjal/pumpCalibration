from flask import Flask, request

app = Flask(__name__)

MAINTENANCE = False

@app.route("/")
def home():
  return "Server Is Alive"

@app.route("/health", methods = ["GET","HEAD"])
def health():
  return "OK"

#Pump Calibration to Jaini
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

#Complete Pump Calibration
@app.get("/pumpCalibration")
def pumpCalibration():
  if MAINTENANCE:
    return str("Service Unavailable!")
    
  key = str(request.args.get("key"))
  if key != "VIP120":
    return "Access Denied!"
    
  vol = float(request.args.get("vol"))
    
  time1 = float(request.args.get("time1"))
  time2 = float(request.args.get("time2"))
  time3 = float(request.args.get("time3"))
  avg1 = (time1 + time2 + time3) / 3
  result1 = ((vol / 1000) * 3600) / avg1

  time4 = float(request.args.get("time4"))
  time5 = float(request.args.get("time5"))
  time6 = float(request.args.get("time6"))
  avg2 = (time4 + time5 + time6) / 3
  result2 =((vol / 1000) * 3600) / avg2

  time7 = float(request.args.get("time7"))
  time8 = float(request.args.get("time8"))
  time9 = float(request.args.get("time9"))
  avg3 = (time7 + time8 + time9) / 3
  result3 =((vol / 1000) * 3600) / avg3

  time10 = float(request.args.get("time10"))
  time11 = float(request.args.get("time11"))
  time12 = float(request.args.get("time12"))
  avg4 = (time10 + time11 + time12) / 3
  result4 =((vol / 1000) * 3600) / avg4

  time13 = float(request.args.get("time13"))
  time14 = float(request.args.get("time14"))
  time15 = float(request.args.get("time15"))
  avg5 = (time13 + time14 + time15) / 3
  result5 =((vol / 1000) * 3600) / avg5
     
  return f"{str(round(result1,1))}, {str(round(result2,1))}, {str(round(result3,1))}, {str(round(result4,1))}, {str(round(result5,1))}"

@app.get("/pumpVerification")
def pumpVerification():
  if MAINTENANCE:
    return str("Service Unavailable!")
    
  key = str(request.args.get("key"))
  if key != "VIP121":
    return "Access Denied!"
    
  time = float(request.args.get("time"))
  vol = float(request.args.get("vol"))
  result = ((vol / 1000) * 3600) / time
  return str(round(result,1))
