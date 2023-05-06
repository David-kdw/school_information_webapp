# DIT-project_devops (CI/CD) 
---
 [Repo](https://github.com/David-kdw/school_information_webapp.git)

 # Welcome to this project.
In this project, we are deploying a web application code source in a docker container via Jenkinsfile. The application is about giving information on school management to its users 

Make sure to have Administrative access on the system used to run this project
# Languages :
- Python
- html 
- css 

# Requirements
- install and run docker. In docker parametres check the box **Expose daemon on tcp://localhost:2375 without TLS** and apply. 
![Docker expose](/static/img/docker1.PNG)

*Note : Exposing the Docker daemon on a network without TLS (Transport Layer Security) encryption can be insecure, as it allows unencrypted traffic to be sent over the network, which can potentially be intercepted by a malicious actor. By default, the Docker daemon listens on a local Unix socket, which is secure and only accessible by the root user on the host machine. However, if you expose the Docker daemon on TCP without TLS, anyone who has access to the network can potentially access and control the Docker daemon.*

If you need to expose the Docker daemon on TCP, it is recommended to enable TLS encryption to secure the connection. This involves configuring the Docker daemon to use TLS certificates and configuring the Docker client to use those certificates to authenticate the connection to the daemon.

**For our projects purposes we assume to expose daemon on tcp://localhost:2375 without TLS**

# How to deploy :
---

## Prequisite
> Install and run Jenkins on your computer : 
 Follow tutoriel official tutoriel at [Installing Jenkins](https://www.jenkins.io/doc/book/installing/). Note that the installation of Jenkins requires a java JDK 8 or 11, and add Java to path environment variable

 > Configure Jenkins to use Github : 
it is now time to create our GitHub credentials (PAT) inside the Jenkins server.
1) Click on new item 
![New item](/static/img/Jks1.webp)
2) Give the process a name, select Pipeline and click on OK:
![Pipeline name](/static/img/Jks2.webp)
3) Make configurations 
Check GitHub hook trigger for GITScm polling in order to generate the build when some event occurs in GitHub (push, pull request…):
![Automatic trigger](/static/img/Jks3.webp)
4) Add the GitHub repository where: Clone my repository and add your GitHub Credentials generated via Tokens. To generate your Github tokens go to Settings/Developer settings/Generate new token. Make sure in the parameters you have select cases repo& admin:repo_hook
![Automatic trigger](/static/img/Jks4.webp)
5) Finally, check the brain name /master or /main where appropritate according to your repository branch name. Put the name of Jenkinsfile file into Script path and then hit Save.

 > Configure Jenkins to use Docker to build container images : 
Jenkins has a Docker plugin that enables communication with Docker hosts. To install the plugin in Jenkins, do the following:
1. Select Manage Jenkins in the menu on the left side of the Jenkins dashboard.
2. Click Manage Plugins in the Manage Jenkins window.
3. Select the Available tab in the Plugin Manager window.
4. Type Docker in the search field, and select the box next to the Docker plugin that appears in the search results.
5. Click the Download now and install after restart button
6. When all the necessary plugin components download, select the box at the bottom of the screen to restart Jenkins.
7. Login again into jenkins and go to manage jenkins, the configure system
8. Scroll down until Docker builder and under Docker URL server REST API URL, insert tcp://localhost:2375 to enable communication between jenkins ans docker andt that is all.

>Adding repository polling on GitHub
Go to your repository on GitHub, then go to Settings > Webhooks > Add webhook
![Git repo webhook](/static/img/git1.webp)
In Payload URL add your Jenkins server address, adding **/github-webhook/** at the final, to look like: http://{IP Jenkins Server}:8080/github-webhook/
In our case we are deploying on loaclhost so it should be **http://localhost:8080/github-webhook/**
In Content type, choose application/json, Leave Secret blank
Choose in which events you want to trigger the webhook( on push)
Check the Active checkbox
Hit Add webhook
![Git repo webhook](/static/img/git2.webp)



## Now for each push, jenkins will deploy automatically the application inside docker. You can also get inside jenkins and laucnh build so all services will run

You can check if the build is operational inside Jenkins dashboard 
![Success build](/static/img/Jkns.PNG)

Then you can launch the app with localhost:8081 

THANK YOU! bye 

