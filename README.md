Instructions

prerequisites:
- install git
- create a github account, preferably with alliander access, but not necessary
..

Step 1: create a local git project (what is git?!)
- open terminal and go to the main folder of your git project, the same folder this file is resided 
do cmd: git init


Step 2: add and commit a file to your git project (add/commit tracking and not tracking projectfiles)
do cmd: git add my_first_git_project/*
do cmd: git status
do cmd: git commit -m "first init message" 
do cmd: git status


Step 3: create a github project, and upload this current project to github   (sync to github and origin concept)
do cmd: git remote add origin https://github.com/Widgetstein/git_training.git
do cmd: git push -u origin master

check your new project online!


Step 4: run python file and make a small change (rehearse: git status, git add/commit, git push)
do: run python file hello_git
do: fix error
do cmd: git status
do cmd: git add .......
do cmd: git commit -m "....your own message"

Step 5: add a .gitignore file to your project:
create file in main folder: .gitignore
open .gitignore file and put in: .idea/*
optionally add more files that you like to ignore

do cmd: git status  (check what happens when you add .gitignore to your .gitignore file)
do cmd: git add and commit the .gitignore file

do cmd: git puhs origin master
Check changes online

Step 6: branching
