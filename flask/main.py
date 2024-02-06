# # main.py
# import sqlite3
# from flask import Flask, redirect, render_template, request, url_for
# app = Flask(__name__)

# data = []
# def veriAl():
#     global data
#     with sqlite3.connect('kahve.db') as con:
#         cur = con.cursor()
#         cur.execute("select * from tblkahve")
#         data = cur.fetchall()
#         for i in data:
#             print(i)
            

# def veriEkle(kahvename, kahvetur, kahveyıl):
#     with sqlite3.connect('kahve.db') as con:
#         cur = con.cursor()
#         # Sütun adlarını veritabanındakilerle eşleştirin
#         cur.execute("INSERT INTO tblkahve (kahvename, kahvetur, kahveyıl) VALUES (?, ?, ?)", (kahvename, kahvetur, kahveyıl))
#         con.commit()
#         print("Veriler eklendi")


# def veriSil(id):
#     with sqlite3.connect('kahve.db') as con:
#         cur = con.cursor()
#         cur.execute("delete from tblkahve where id=?", (id))
#         print("Veriler eklendi")        

# @app.route("/kahvesil/<string:id>")
# def kahvesil(id):
#     print("Kahvesil silinecek id", id)
#     veriSil(id)
#     # Burada id'ye göre silme işlemini yapacak kodlarınız olacak
#     return redirect(url_for("kahves"))

            
# @app.route("/index")
# def index():
#     veriAl()
#     kahveler = [
#             {
#             'kahvetitle':'Turk kahvesi'
#             },
#             {
#                 'kahvetitle':'Filtre Kahve'
#             }
#             ]

#     return render_template("index.html",kahveler = kahveler)

# @app.route("/kahves")
# def kahves():
    
#     return render_template("kahves.html", veri=data)


# @app.route("/Contact")
# def Contact():
#     return render_template("Contact.html")


# @app.route("/dunya")
# def dunya():
#     return render_template("dunya.html")


# @app.route("/kultur")
# def kultur():
#     return render_template("kultur.html")

# @app.route("/kahvesec", methods=['GET', 'POST'])
# def kahvesec():
#     if request.method == 'POST':
#         kahvetitle = request.form['kahvename']
#         kahvetur = request.form['kahvetur']
#         kahveyıl = request.form['kahveyıl']
#         veriEkle(kahvetitle, kahvetur, kahveyıl)
#     return render_template("kahvesec.html")
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8080, debug=True)



# main.py
# import sqlite3
# from flask import Flask, redirect, render_template, request, url_for

# app = Flask(__name__)


# def veriAl():
#     with sqlite3.connect('kahve.db') as con:
#         cur = con.cursor()
#         cur.execute("SELECT * FROM tblkahve")
#         data = cur.fetchall()
#     return data

# def veriEkle(kahvename, kahvetur, kahveyıl):
#     with sqlite3.connect('kahve.db') as con:
#         cur = con.cursor()
#         cur.execute("INSERT INTO tblkahve (kahvename, kahvetur, kahveyıl) VALUES (?, ?, ?)", (kahvename, kahvetur, kahveyıl))
#         con.commit()


# def veriSil(id):
#     with sqlite3.connect('kahve.db') as con:
#         cur = con.cursor()
#         cur.execute("DELETE FROM tblkahve WHERE id=?", (id,))
#         con.commit()


# @app.route("/kahvesil/<int:id>")
# def kahvesil(id):
#     veriSil(id)
#     return redirect(url_for("kahves"))


# @app.route("/index")
# def index():
#     kahveler = veriAl()
#     return render_template("index.html", kahveler=kahveler)

# @app.route("/kahves")
# def kahves():
#     veriler = veriAl()
#     return render_template("kahves.html", veri=veriler)

# @app.route("/Contact")
# def Contact():
#     return render_template("Contact.html")


# @app.route("/dunya")
# def dunya():
#     return render_template("dunya.html")


# @app.route("/kultur")
# def kultur():
#     return render_template("kultur.html")


# @app.route("/kahvesec", methods=['GET', 'POST'])
# def kahvesec():
#     if request.method == 'POST':
#         kahvename = request.form['kahvename']
#         kahvetur = request.form['kahvetur']
#         kahveyıl = request.form['kahveyıl']
#         veriEkle(kahvename, kahvetur, kahveyıl)
#         return redirect(url_for("kahves")) 
#     return render_template("kahvesec.html")

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8080, debug=True)

import sqlite3
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

def veriAl():
    with sqlite3.connect('kahve.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tblkahve")
        data = cur.fetchall()
    return data

def veriEkle(kahvename, kahvetur, kahveyıl):
    with sqlite3.connect('kahve.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO tblkahve (kahvename, kahvetur, kahveyıl) VALUES (?, ?, ?)", (kahvename, kahvetur, kahveyıl))
        con.commit()

def veriSil(id):
    with sqlite3.connect('kahve.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM tblkahve WHERE id=?", (id,))
        con.commit()

def veriGuncelle(id, kahvename, kahvetur, kahveyıl):
    with sqlite3.connect('kahve.db') as con:
        cur = con.cursor()
        cur.execute("UPDATE tblkahve SET kahvename=?, kahvetur=?, kahveyıl=? WHERE id=?", (kahvename, kahvetur, kahveyıl, id))
        con.commit()

def veriDetay(id):
    with sqlite3.connect('kahve.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tblkahve WHERE id=?", (id,))
        data = cur.fetchone()
    return data

@app.route("/kahvesil/<int:id>")
def kahvesil(id):
    veriSil(id)
    return redirect(url_for("index"))

@app.route("/")
@app.route("/index")
def index():
    kahveler = veriAl()
    return render_template("index.html", kahveler=kahveler)

@app.route("/kahves")
def kahves():
    veriler = veriAl()
    return render_template("kahves.html", veri=veriler)

@app.route("/Contact")
def Contact():
    return render_template("Contact.html")

@app.route("/dunya")
def dunya():
    return render_template("dunya.html")

@app.route("/kultur")
def kultur():
    return render_template("kultur.html")

@app.route("/kahvesec", methods=['GET', 'POST'])
def kahvesec():
    if request.method == 'POST':
        kahvename = request.form['kahvename']
        kahvetur = request.form['kahvetur']
        kahveyıl = request.form['kahveyıl']
        veriEkle(kahvename, kahvetur, kahveyıl)
        return redirect(url_for("index"))
    return render_template("kahvesec.html")

@app.route("/kahveguncelle/<int:id>", methods=['GET', 'POST'])
def kahveguncelle(id):
    if request.method == 'POST':
        kahvename = request.form['kahvename']
        kahvetur = request.form['kahvetur']
        kahveyıl = request.form['kahveyıl']
        veriGuncelle(id, kahvename, kahvetur, kahveyıl)
        return redirect(url_for("index"))
    else:
        mevcutVeri = veriDetay(id)
        return render_template("kahveguncelle.html", kahve=mevcutVeri)

@app.route("/kahvedetay/<int:id>")
def kahvedetay(id):
    detay = veriDetay(id)
    return render_template("kahvedetay.html", detay=detay)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/kahvesec", methods=['GET', 'POST'])
def kahvesec():
    if request.method == 'POST':
        kahvename = request.form['kahvename']
        kahvetur = request.form['kahvetur']
        kahveyıl = request.form['kahveyıl']
        veriEkle(kahvename, kahvetur, kahveyıl)
        return redirect(url_for("index"))
    return render_template("kahvesec.html")

if __name__ == "__main__":
    app.run(debug=True)