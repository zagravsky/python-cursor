from flask import Flask, render_template, request, jsonify, make_response, url_for, abort, session
from api import api

Cars = [
    {'Brend': 'Audi','Model': 'A1','Size': 'supermini','Type': 'Sedan','Doors': 3},
    {'Brend': 'BMW','Model': 'X5','Size','Size': 'supermini','Type': 'Hatchback','Doors': 5},
]
