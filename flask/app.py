import sqlite3

import flask_cors
from flask import Flask, request, Response
from wtforms import Form, RadioField


# connection = sqlite3.Connection("CMS_REPO.sqlite")


def open_binary_local_file(filename):
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


def save_file_to_repo(name, file_type, binary_file):
    connection = sqlite3.Connection("CMS_REPO.sqlite")
    cursor = connection.cursor()
    sqlite_insert_blob_query = """ INSERT INTO FILES (name, type, file) VALUES (?, ?, ?)"""
    cursor.execute(sqlite_insert_blob_query, (name, file_type, binary_file))
    connection.commit()
    connection.close()


def update_file_in_repo(name, file_type, binary_file):
    connection = sqlite3.Connection("CMS_REPO.sqlite")
    cursor = connection.cursor()
    sqlite_insert_blob_query = """UPDATE FILES SET file=? WHERE name=?"""
    cursor.execute(sqlite_insert_blob_query, (binary_file, name))
    connection.commit()
    connection.close()


def repo_init():
    connection = sqlite3.Connection("CMS_REPO.sqlite")
    cursor = connection.cursor()

    cursor.execute(f"""CREATE TABLE IF NOT EXISTS FILES (name TEXT PRIMARY KEY, type TEXT, file BLOB)""")
    connection.commit()

    cursor.execute("""SELECT count(*) FROM FILES WHERE name='data.json'""")
    response = cursor.fetchall()
    if response[0][0] == 0:
        save_file_to_repo("data.json", "json", open_binary_local_file("baseWebsite/data.json"))
        save_file_to_repo("logo.png", "png", open_binary_local_file(f"baseWebsite/gfx/logo.png"))
        for i in range(5):
            save_file_to_repo(f"slider/photo-{i + 1}.jpg", "jpg",
                              open_binary_local_file(f"baseWebsite/gfx/slider/photo-{i + 1}.jpg"))
        print("Dodano pliki do bazy")

    connection.close()


def get_file_from_db(name):
    connection = sqlite3.Connection("CMS_REPO.sqlite")
    cursor = connection.cursor()
    cursor.execute("""SELECT file, type FROM FILES WHERE name = ?""", (name,))
    result = cursor.fetchall()
    connection.close()
    try:
        return (result[0][0], result[0][1])
    except:
        return False

def count_files_by_name(name):
    connection = sqlite3.Connection("CMS_REPO.sqlite")
    cursor = connection.cursor()
    cursor.execute("""SELECT COUNT(*) FROM FILES WHERE name = ?""", (name,))
    result = cursor.fetchall()
    connection.close()
    try:
        return result[0][0]
    except:
        return False


def get_data_json():
    return get_file_from_db("data.json")[0]


class MenuForm(Form):
    menuRadio = RadioField('Menu', choices=[('ver', 'vertical'), ('hor', 'horizontal')])


app = Flask(__name__)
flask_cors.CORS(app)
repo_init()


@app.route("/data")
def return_json():
    return get_data_json()


@app.route("/data/update", methods=["POST"])
def update_data():
    files = request.files
    file = files.get('file')
    try:
        update_file_in_repo("data.json", "json", file.read())
        return Response(status=200)
    except Exception as ex:
        return Response(status=500)


@app.route("/gfx", methods=["GET", "POST"])
def return_gfx():
    name = request.args["name"]
    return get_file_from_db(name)


@app.route("/gfx/get", methods=["GET", "POST"])
def return_gfx2():
    print(request.get_json())

    name = request.form["name"]
    return get_file_from_db(name)



@app.route("/gfx/insert", methods=["GET", "POST"])
def insert_gfx():
    name = request.args['name']
    files = request.files
    file = files.get('file')
    try:
        if count_files_by_name(name) == 0:
            save_file_to_repo(name, "photo", file.read())
        else:
            update_file_in_repo(name, "photo", file.read())
        return Response(status=200)
    except Exception as ex:
        return Response(status=500)

# {{ wtf.quick_form(form, action=adr)}}


if __name__ == '__main__':
    app.run(debug=True)
