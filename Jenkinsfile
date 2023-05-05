pipeline {
  agent {
    docker {
      image 'docker:latest'
      args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
  }
  stages {
    stage('Clone') {
      steps {
        git 'https://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@github.com/David-kdw/school_information_webapp.git'
      }
    }
    stage('Build') {
      agent {
        node {
          label 'docker'
          workspace("$PWD/C:/Users/user/AppData/Local/Jenkins/.jenkins/workspace/DIT-devops_project/")
        }
      }
      steps {
        sh 'docker-compose build'
      }
    }
    stage('Test') {
      agent {
        node {
          label 'docker'
          workspace("$PWD/C:/Users/user/AppData/Local/Jenkins/.jenkins/workspace/DIT-devops_project/")
        }
      }
      steps {
        sh 'docker-compose up -d db'
        sh 'docker-compose up -d sonarqube'
        sh 'docker-compose run --rm app pytest'
      }
      post {
        always {
          sh 'docker-compose down -v'
        }
      }
    }
    stage('Deploy') {
      agent {
        node {
          label 'docker'
          workspace("$PWD/C:/Users/user/AppData/Local/Jenkins/.jenkins/workspace/DIT-devops_project/")
        }
      }
      steps {
        sh 'docker-compose up -d'
      }
    }
  }
}

