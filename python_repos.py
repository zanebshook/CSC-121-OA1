"""Request Data using an API"""
import requests #import requests module
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
#process results
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
#explore information about the repositories
#print the number of repositories in the return dictionary
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
#examine all repositories
print("\nSelected information about the first repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")