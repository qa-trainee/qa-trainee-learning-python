# How to setup a GitHub account/repository

So you want to learn coding and you want to do it right?

Apart from downloading the apps and language libraries, vms or any other files required to actually code, you will also need to set up an account on GitHub.

This is a quick guide I created on day 1 of my latest attempt to become a coder.

If you already know what GitHub is and what's it use is then go to ##‘Basic steps to GitHub setup

## What is GitHub
GitHub is a Website which one can use to store code(or other files). It allows you to manage multiple versions of the code while you update it and has features to help multiple people work on same code files at the same time without being in the same office network(files shared on Internet). So it helps you to make sure your changes don't have conflicts with others or vice versa.

In fancier terms you would call that distributed revision control and source code management (SCM) functionality of Git as well as adding its own features

## Why do I need a GitHub
Why is it required for someone who is just starting to learn code?

- You want to be able to access your latest code from multiple devices / multiple locations (Example, your desktop when at home, your laptop when you are at coffee shop, your office machine at office)
- You want to be able to share your practice code to your mentors in order to get feedback.
- Employers use version control softwares and this is something they want to see in your resume
- Your code repository is your work. It speaks for you. A person might get lucky in an interview but a legitimate original code repository with a history is a solid proof of your work experience

## Basic steps to GitHub setup
Register on GitHub.com with a user id and email id which can go on your resume.

Once you register as a new user, where since you don't have any existing repository  it will ask you to create one under bootcamp.

Before creating a repository first download and Install the software that is needed to manage this GitHub repository from your desktop.

There are two versions desktop and command line. Install the desktop version. it will give you command line git module (gitshell) too. https://desktop.GitHub.com/

Desktop ui is easy but you should use and learn the command line git and avoid desktop version to perform action. Desktop version can be usefull to gain a visual understanding of whats happening with your code.

## Short Video tutorial
While the software is getting downloaded see [this](https://www.youtube.com/watch?v=0fKg7e37bQE) video. You can skip the first 5 mins if you know some basics. Also increase the playback speed to 1.25 times to save some time.

### Notes from the video tutorial.
(I will suggest you to write your own notes while pausing the video when required, it will help with remembering the commands and their uses)

Create a repository online on GitHub website then use below commands on gitshell

1. git clone \<project repository path name>
Which creates a first copy ie copies all code in GitHub repository from GitHub website to your local drive.from where you ran the command

2. git status [enter]
gives the difference between the code on your local directory and the latest version of code in GitHub code repository

3. git add \<file name> [enter]
Adds \<file name> file from local desktop to local git repo
git add -a to add all
Check the git status again, it will show one the file to be committed

4. git commit -m “message of the check in”
Basically commits all pending files from previous adds to local GitHub repo with a comment mentioned in quotes with option -m

5. git push
Final commit from local to GitHub repo on website

6. git pull
Gets the latest new changes from GitHub.com repo to local directory

## How to use these commands on daily basis?
Pull - Run this command everyday just before you start your work so that you pull latest code from git with overnight changes

Status - You make changes in the code through out the day and by using status frequently you can see the difference between local and git

Add - Use Add to add changes from local desktop to local git repo

Commit - To commit all added changes in local git repo

Push - To push and commit all changes from local git repo to GitHub.com repo.

## Installation and verification
By the time above youtube video completes GitHub desktop should be downloaded and ready to Install.

- Install your GitHub desktop, remember to use the [private]( https://help.GitHub.com/articles/setting-your-commit-email-address-on-GitHub/) version of email to avoid spams
login using the GitHub desktop

- GitHub desktop is a shortcut in start menu, right click open file location, here you will find Git Shell, click git shell to get a powershell window.

- Run 'git' [enter] if this gives you a list of git commands, you are good.

- Now go to GitHub website, create a new repository with .gitignore file of the languange you are using and readme.md file

- Once the repository is created, add it to git desktop.

- Now go to the folder on your desktop where you want to store your code locally.

- Open git shell and go at the same path.

- Run git clone \<path to the repo> This will give you the files from repo copied to your local directory asking with a hidden .git directory

- Make some changes in readme.MD file by opening it in notepad and then save the changes. Use the git add, commit, push commands to upload changes to git.

This covers just the basics of using GitHub.

While you are learning a coding language you will be (mostly) working alone on your code. At max you might have to share your code to get a feedback.

For that purpose, I am hoping that this much knowledge should be good enough.

Once you start to actually work on something with other folks you will need to learn and use advance features

## Additional resources

https://help.GitHub.com/articles/markdown-basics/

https://try.GitHub.io/levels/1/challenges/1

https://guides.GitHub.com/

http://readwrite.com/2013/09/30/understanding-GitHub-a-journey-for-beginners-part-1




Questions? [Ask them here](www.reddit.com/r/learnprogramming)
