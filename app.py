from flask import Flask,render_template,jsonify
from database import Load_db
# JOBS=[
#     {
#         'id':1,
#         'title':"data analyst",
#         'location':"bengaluru"
#     },
#     {
#         'id':2,
#         'title':"web developer",
#         'location':"bengaluru"
#     },
#     {
#         'id':3,
#         'title':"ui/ux",
#         'location':"bengaluru"
#     }
    
# ]
app=Flask(__name__)

@app.route("/")
def hello():
    JOBS=Load_db()
    return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(fun())



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
