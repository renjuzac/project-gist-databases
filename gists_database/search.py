from .models import Gist
from datetime import datetime

def search_gists(db_connection, **kwargs):
    c = db_connection.cursor()
    sql = ''
 
    if 'github_id' in kwargs and 'created_at' in kwargs:
        sql = 'SELECT * from gists WHERE datetime(created_at)==datetime(?) AND github_id==(?)'
        c.execute(sql,(kwargs['created_at'],kwargs['github_id'],))
    elif 'github_id' in kwargs:    
        sql = 'SELECT * from gists WHERE github_id==(?)'
        print(kwargs['github_id'])
        c.execute(sql,(kwargs['github_id'],))
    elif 'created_at' in kwargs:    
        sql = 'SELECT * from gists WHERE datetime(created_at)==datetime(?)'
        c.execute(sql,(kwargs['created_at'],))
        
        # datetime.strptime(entry['created_at'],"%Y-%m-%dT%H:%M:%SZ")
    else:
        sql = 'SELECT * from gists'
        c.execute(sql)
    result = c.fetchall()
    gistlist  = []
    for gist in result:
        gistlist.append(Gist(gist))
    return gistlist

