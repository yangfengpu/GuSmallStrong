#!/usr/bin/env python
# -*- coding: utf-8 -*-

from greency import app
from greency.forms import *
from flask import render_template, redirect, url_for, request
from flask import jsonify 
from flask import session
from flask.ext.pymongo import PyMongo
from pymongo import MongoClient
from dao2 import mongoDao
import random

client = MongoClient()
db1 = client.alf
c1 = db1.gu

#---------- Start Login relevance ---------
app.name = 'educocoMongoLog'
mongo = PyMongo(app)

@app.route('/login', methods=('GET', 'POST'))
def submit():
    if __isLogined():
        return redirect('/')
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route('/loginError', methods=('GET', 'POST'))
def loginError():
    if __isLogined():
        return redirect('/')
    form = SignupForm()
    form.error = "alf is wrong!" 
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('index.html', form=form)


@app.route('/')
def index():
    if __isLogined():
        return redirect('/bom')
    return redirect('/login')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect('/login')


@app.route('/success',  methods=['POST'])
def success():
    data = {}
    name=request.form["username"]
    pwd=request.form["password"]
    if (__roleValidate(name, pwd)):
        session['username'] = name
        return redirect('/bom')
    else:
        return redirect('/loginError' )

#---------- End Login relevance ---------

@app.route('/bom')
def bom():
    if __isLogined():
        guguDao = mongoDao()
        records = guguDao.read_records()
        return render_template('bom.html', data = records, leaf_level = True, not_bom = False)
    return redirect('/login')

@app.route('/bomByPn/<pn>')
def bomByPn(pn):
    if __isLogined():
        guguDao = mongoDao()
        records = guguDao.read_records_by_pn(pn)
        return render_template('bom.html', data = records, leaf_level = True, not_bom = True)
    return redirect('/login')

@app.route('/gugupost',  methods=['POST'])
def saveRecord():
    content = request.json
    content['pcs'] = int(content['pcs'])
    guguDao = mongoDao()
    guguDao.add_a_record(content)
    return ""
@app.route('/guguremove/<oid>')
def removeRecord(oid):
    guguDao = mongoDao()
    guguDao.remove_a_record(oid)
    return ""


#------ Helper functions --------

def __isLogined():
    if 'username' in session:
        return True
    else:
        return False

def __roleValidate(user, pwd): #TODO
    if (user == "wicgkuo" and pwd == "gugu0104"):
        return True
    else:
        return False

@app.route('/test/<id>')
def test(id):
    if (int(id) > 5):
        return redirect('/result')
    return 'test'

@app.route('/purchase-item')
def purchase_item():
    form = PurchaseItemForm()
    return render_template('purchase_item.html', form = form)

@app.route('/testJson', methods=('GET', 'SET'))
def tj():
    f = {}
    f['a'] = '1'
    f['b'] = 2
    return jsonify(**f)

@app.route('/summary', methods=(['GET']))
def summary():
    guguDao = mongoDao()
    w = guguDao.aggregrate_records()
    return render_template('summary.html', data = w)

@app.route('/precaculatePcs/<targetPn>/<opType>/<pcs>')
def precaculate_pcs(targetPn, opType, pcs):
    guguDao = mongoDao()
    f = guguDao.pre_saving_test(targetPn, pcs, opType)
    return str(f)