This lab continues on from the Getting Started WIth Continuous Integration lab. The goal of this lab is to integrate your GitHub repo with Travis CI so that you can automate your tests and deployments. Follow the steps below to setup your first workflow for CI/CD:

**Step One**: Create a free account with Travis CI: 
https://travis-ci.org
 

**Step Two**: Activate the GitHub Repository where compute_stats_refactor.py is held. 

**Step Three**: Add a .travis.yml file to the root or top directory of your GitHub repository. Remember, we want to run our unit tests every time we make a new commit to our main respiratory. 

Learn how to configure your yaml file by reading the docs here: 
https://docs.travis-ci.com/user/languages/python
 

A minimal example is as below: 

  language: python

  script:

    - unittest

Step Four: Trigger your first build. To do this all you have to do is commit it to your local git history and then git push to GitHub. 

Optional Step: If steps 2-4 were confusing then read this page on the Travis CI docs: 
https://travis-ci.org/getting_started
 

Step Five: Deploy compute_stats_refactor.py to PYPI. This is the official package manager for python and hosts the most popular open source python projects. Deploy your python script using Travis CI by following these steps here: 
https://docs.travis-ci.com/user/deployment/pypi
