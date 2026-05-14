from flask import Flask, render_template, redirect, url_for, request
import sqlite3
import pandas as pd

app = Flask('music')
app.secret_key = "music"
app.debug = True
DATABASE = 'ahndata.db'


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/data', methods = ['POST', 'GET'])
def data():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    result = []
    query = ''
    if request.method == 'POST':
        query = request.form['query']

    if query == 'key':
        label = "Total listens per key"
        cursor.execute("SELECT DISTINCT key FROM ahn")
        keys = cursor.fetchall()
        keys_res = []
        if keys:
            for key in keys:
                keys_res.append(key['key'])
                cursor.execute("SELECT SUM(plays) as sum FROM ahn WHERE key=?", (key['key'],))
                result.append(cursor.fetchone()['sum'])
            
            labels = keys_res
            data = result

            return render_template('data.html', labels=labels, data=data, label=label)

    if query == 'year':
        label = "Total listens per release year"
        cursor.execute("SELECT DISTINCT year FROM ahn ORDER BY year ASC")
        years = cursor.fetchall()
        years_res = []
        if years:
            for year in years:
                years_res.append(year['year'])
                cursor.execute("SELECT SUM(plays) as sum FROM ahn WHERE year=?", (year['year'],))
                result.append(cursor.fetchone()['sum'])
            
            labels = years_res
            data = result


            return render_template('data.html', labels=labels, data=data, label=label)
    
    if query == 'bpm':
        label = "Total listens per bpm (beats per minute)"
        cursor.execute("SELECT DISTINCT bpm FROM ahn ORDER BY CAST(bpm AS INT)")
        bpms = cursor.fetchall()
        bpms_res = []
        if bpms:
            for bpm in bpms:
                bpms_res.append(bpm['bpm'])
                cursor.execute("SELECT SUM(plays) as sum FROM ahn WHERE bpm=?", (bpm['bpm'],))
                result.append(cursor.fetchone()['sum'])
            
            labels = bpms_res
            data = result

            return render_template('data.html', labels=labels, data=data, label=label)
        
    
    if query == 'energy':
        label = "Total listens per energy score "
        cursor.execute("SELECT DISTINCT energy FROM ahn ORDER BY energy")
        engs = cursor.fetchall()
        engs_res = []
        if engs:
            for eng in engs:
                engs_res.append(eng['energy'])
                cursor.execute("SELECT SUM(plays) as sum FROM ahn WHERE energy=?", (eng['energy'],))
                result.append(cursor.fetchone()['sum'])
            
            labels = engs_res
            data = result

            return render_template('data.html', labels=labels, data=data, label=label)
    
    if query == 'danceability':
        label = "Total listens per danceability score "
        cursor.execute("SELECT DISTINCT danceability FROM ahn ORDER BY danceability")
        dances = cursor.fetchall()
        dances_res = []
        if dances:
            for dance in dances:
                dances_res.append(dance['danceability'])
                cursor.execute("SELECT SUM(plays) as sum FROM ahn WHERE danceability=?", (dance['danceability'],))
                result.append(cursor.fetchone()['sum'])
            
            labels = dances_res
            data = result

            return render_template('data.html', labels=labels, data=data, label=label)

    if query == 'acousticness':
        label = "Total listens per acousticness score "
        cursor.execute("SELECT DISTINCT acousticness FROM ahn ORDER BY acousticness")
        acs = cursor.fetchall()
        acs_res = []
        if acs:
            for ac in acs:
                acs_res.append(ac['acousticness'])
                cursor.execute("SELECT SUM(plays) as sum FROM ahn WHERE acousticness=?", (ac['acousticness'],))
                result.append(cursor.fetchone()['sum'])
            
            labels = acs_res
            data = result

            return render_template('data.html', labels=labels, data=data, label=label)
        
    if query == 'genre':
        label = "Total listens per genre "
        cursor.execute("SELECT DISTINCT genre FROM ahn")
        genres = cursor.fetchall()
        genres_res = []
        if genres:
            for genre in genres:
                genres_res.append(genre['genre'])
                cursor.execute("SELECT SUM(plays) as sum FROM ahn WHERE genre=?", (genre['genre'],))
                result.append(cursor.fetchone()['sum'])
            
            labels = genres_res
            data = result

            return render_template('data.html', labels=labels, data=data, label=label)
        
    
    if query == 'artist':
        label = "Total listens per artist"
        cursor.execute("SELECT DISTINCT artist FROM ahn WHERE CAST(plays AS SIGNED) > 25")
        artists = cursor.fetchall()
        artists_res = []
        if artists:
            for artist in artists:
                artists_res.append(artist['artist'])
                cursor.execute("SELECT SUM(plays) as sum FROM ahn WHERE artist=? ", (artist['artist'],))
                result.append(cursor.fetchone()['sum'])
            
            labels = artists_res
            data = result

            return render_template('data.html', labels=labels, data=data, label=label)
    
    if query == 'duration':
        label = "Total listens per duration"
        cursor.execute("SELECT duration FROM ahn ORDER BY duration ASC")
        durs = cursor.fetchall()
        durs_res = []
        if durs:
            for dur in durs:
                durs_res.append(dur['duration'])
                cursor.execute("SELECT SUM(plays) as sum FROM ahn WHERE duration=? ", (dur['duration'],))
                result.append(cursor.fetchone()['sum'])
            
            labels = durs_res
            data = result

            return render_template('data.html', labels=labels, data=data, label=label)
        
    labels = []
    data = []

    return render_template('data.html', labels=labels, data=data)

@app.route('/test')
def test():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    artist = "Michael Jackson"
    error = ""
    cursor.execute("SELECT title FROM ahn WHERE artist=? ", (artist,))
    result = cursor.fetchall()
    for row in result:
        print(row['title'])

    if result is None:
        error = "QUERY DID NOT WORK"

    return render_template('test.html', result=result, error=error, artist=artist)

app.run(host='0.0.0.0', port=6677)