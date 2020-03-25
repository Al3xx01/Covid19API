from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


def countries_data(c):
    d = {}
    for row in c.execute("SELECT * FROM DatiCovid ORDER BY country"):
        (Id, ContryName, TotalCases, TotalDeaths) = row
        d[Id] = {
            "Id": Id,
            "Nome": ContryName,
            "TotalCases": TotalCases,
            "TotalDeaths": TotalDeaths,
        }
    return d


def state_data(c, state):
    d = {}
    for row in c.execute(f"SELECT * FROM DatiCovid WHERE country LIKE '{state}'"):
        (Id, ContryName, TotalCases, TotalDeaths) = row
        d[Id] = {
            "Id": Id,
            "Nome": ContryName,
            "TotalCases": TotalCases,
            "TotalDeaths": TotalDeaths,

        }
    return d


@app.route('/')
def home():
    return '<center><h1>Maintenance</h1></center>'


@app.route('/api/v1/resources/countries')
def countries():
    database = sqlite3.connect('database.db')
    c = database.cursor()
    return jsonify(countries_data(c))


@app.route('/api/v1/resources/countries/<string:state>')
def state(state):
    database = sqlite3.connect('database.db')
    c = database.cursor()
    return jsonify(state_data(c, state))


app.run()
