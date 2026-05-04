from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def home():
  return "Server Is Alive"

@app.get("/health")
def health():
  return "OK"

@app.get("/calculation")
def calculation ():
 vol = float(request.args.get("vol"))
 time1 = float(request.args.get("time1"))
 time2 = float(request.args.get("time2"))
 time3 = float(request.args.get("time3"))
 avg = (time1 + time2 + time3) / 3
 result = ((vol / 1000) * 3600) / avg
 return str(round(result,1))
