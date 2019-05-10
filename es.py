# coding:utf-8

from flask import Flask, render_template, Response,json
import es_sql
from requests import Response

app = Flask(__name__)

def json_success(json_msg, status=200):
    return Response(json_msg, status=status, mimetype='application/json')
@app.route('/')
def hello_world(url=''):
    l=[]
    keys=[]
    result = es_sql.execute_sql(
        url,
        'SELECT app,user   FROM hql  where app =\'dc1\' limit 20 ',
        arguments={'param': 'hql'})
    if result:
        for i in result['result']:
            l.append( i.values())
            keys.append(i.keys())
    return render_template('index.html',my_list=l,keys=keys)



if __name__ == '__main__':
    app.run()