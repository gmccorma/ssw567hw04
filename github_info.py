import requests
import json

# Homework 04a: Develop with the Perspective of the Tester in Mind
# Author: Gabrielle McCormack
# Date Completed: 09.23.2018
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - Gabrielle McCormack


def get_info(user_id) :
    if user_id == '' :
        return "Error, invalid input."
    output = ""
    count = 0
    r = requests.get("https://api.github.com/users/" + user_id + "/repos")
    j = r.json()
    # prints each repo name
    for repo in j:
        repo_name = repo["name"]
        # get repo commits
        r = requests.get("https://api.github.com/repos/" + user_id + "/" + repo_name + "/commits")
        j = r.json()
        # get number of commits in repo
        num_commits = str(len(j))
        if count == 0 :
            output = output + "Repo: " + repo_name + " Number of commits: " + num_commits
            count = 1
        else :
            output = output + "\n" + "Repo: " + repo_name + " Number of commits: " + num_commits

    return output


if __name__ == '__main__':
    print('Running program...')
    user_id = input("Enter the name of your GitHub username: ")
    #print(user_id)
    get_info(user_id)