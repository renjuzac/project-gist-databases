import requests
from datetime import datetime


def import_gists_to_database(db, username, commit=True):
    url = "https://api.github.com/users/{username}/gists"

    response  = requests.get(url.format(username=username))   
    if response.status_code != 200 :
        raise requests.exceptions.HTTPError
        
    c = db.cursor()
    for entry  in response.json() :
        # print(entry.values())
        sql = 'INSERT INTO gists (github_id,html_url ,git_pull_url ,git_push_url,commits_url,forks_url ,public ,created_at ,updated_at,comments,comments_url) values (?,?,?,?,?,?,?,?,?,?,?)'
        c.execute(sql,(entry['id'],entry['html_url'],entry['git_pull_url'],entry['git_push_url'], entry['commits_url'],entry['forks_url'],entry['public'],entry['created_at'],entry['updated_at'],entry['comments'],entry['comments_url']))
        print(entry['created_at'])
        
    if commit:
        db.commit()

  

# dict_keys(['url', 'html_url', 'git_push_url', 'description', 'comments_url', 'updated_at', 'user', 'owner', 'truncated', 'files', 'commits_url', 'id', 'git_pull_url', 'created_at', 'public', 'forks_url', 'comments'])
    
    
