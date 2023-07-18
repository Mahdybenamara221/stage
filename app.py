from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Article")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', Article=data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        Title = request.form['Title']
        Author = request.form['Author']
        Source = request.form['Source']
        IOC = request.form['IOC']
        AG = request.form['AG']
        Vulnerabilities = request.form['Vulnerabilities']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Article (Title, Author, Source,IOC,AG,Vulnerabilities) VALUES (%s, %s, %s, %s, %s, %s)", (Title, Author, Source,IOC,AG,Vulnerabilities))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Article WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))



@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        Title = request.form['Title']
        Author = request.form['Author']
        Source = request.form['Source']
        IOC = request.form['IOC']
        AG = request.form['AG']
        Vulnerabilities = request.form['Vulnerabilities']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE Article SET Title =%s , Author=%s, Source=%s, IOC=%s, AG=%s, Vulnerabilities=%s WHERE id=%s", (Title, Author, Source,IOC,AG,Vulnerabilities,id_data))
        flash("Data Updated Successfully")
        return redirect(url_for('Index'))




if __name__ == "__main__":
    app.run(debug=True)
