
from flask import Flask
app = Flask(__name__)
c=0
@app.route('/') 
def getcount():
    global c
    c+=1
    return str(c)
    

