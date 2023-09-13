from flask import Flask, render_template, request, redirect, send_file
import flask
from time import sleep
from threading import Thread
app = Flask(__name__)

authed = []
def auth(ip):
    authed.append(ip)
    sleep(120)
    authed.remove(ip)
@app.route("/downloadlink", methods=["GET"])
def nignig():
    ip = request.remote_addr
    if ip not in authed:
        return "Nigga you are not authed you DO need to login dick muncher"
    path = "templates/dw/ActionsDetrimentals.zip"
    return send_file(path, as_attachment=True)

@app.route("/download", methods=["GET"])
def dw():
    ip = request.remote_addr
    if ip not in authed:
        return "Nigga you are not authed you DO need to login dick muncher"
    return render_template("download.html")
def read_credentials():
    credentials = {}
    with open('user_site.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            username, password = line.strip().split(':')
            credentials[username] = password
    return credentials
@app.route('/')
def main():
    return flask.send_from_directory("templates","index.html")
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        ip = request.remote_addr
        username = request.form['username']
        password = request.form['password']

        credentials = read_credentials()
        if username in credentials and credentials[username] == password:
            Thread(target=auth, args=[ip,]).start()
            return redirect("/download")
        else:
            return 'Invalid username or password. Fuck off.'

    return render_template('mimic.html')

if __name__ == '__main__':
    app.run()
