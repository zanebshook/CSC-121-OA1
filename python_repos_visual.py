"""Request Data using an API"""
import requests #import requests module
import plotly.express as px #import plotly.express module as a variable
#assign the url of the api call to the url variable
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
#request version 3 of the api and in json format
headers = {'Accept': 'application/vnd.github.v3+json'}
#assign the response of the api call to the variable r
r = requests.get(url, headers=headers)
#print status code to verify a succesful response
print(f"Status code: {r.status_code}")
#convert the response to a dictionary, save is as a variable
response_dict = r.json()
#print message to confirm we have complete results
print(f"Complete results: {not response_dict['incomplete_results']}")
#process and plot repository data
repo_dicts = response_dict['items']
#empty lists to store repo links, stars, hover text info
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    #turn names into links
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
#build hover texts for the plot
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

#plot the data
title = 'Most-Starred Python Projects on GitHub' #create variable for the title
labels = {'x': 'Repository', 'y': 'Stars'} #create variable for axes labels
fig = px.bar(
    x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
#update the layout
fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
#update colors
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()