import mysql.connector
from flask import Flask, render_template, request


app = Flask(__name__)
mydb = mysql.connector.connect(host="localhost",user="root",password= "bekkam11anil22..",database="anil")
cursor = mydb.cursor()

@app.route('/', methods=['GET', 'POST'])
def example():
    cursor.execute("SELECT * from student")
    data = cursor.fetchall()
    return render_template("results.html", value=data)



if "name" == "__main__":
    app.run(debug=True)
app.run(debug=True)

