from flask import Flask, request

app = Flask(__name__)

MAINTENANCE = True

@app.route("/")
def home():
  return "Server Is Alive"

@app.route("/health", methods = ["GET","HEAD"])
def health():
  return "OK"

@app.route("/calculation", methods = ["GET"])
def calculation ():
  if MAINTENANCE:
    return str("Service Unavailable")
    
  vol = float(request.args.get("vol"))
  time1 = float(request.args.get("time1"))
  time2 = float(request.args.get("time2"))
  time3 = float(request.args.get("time3"))
  avg = (time1 + time2 + time3) / 3
  result = ((vol / 1000) * 3600) / avg
  return str(round(result,1))
