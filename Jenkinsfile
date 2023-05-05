pipeline {
  agent {
    docker {
      image 'jenkins/jenkins:lts'
      args '-p 8080:8080'
    }
  }
  stages {
    stage('Build') {
      steps {
        dir('/home/jenkins/workspace/DIT-devops_project')
        {
        sh 'docker-compose build'
        }
      }
    }
    stage('Test') {
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
      steps {
        sh 'docker-compose up -d'
      }
    }
  }
}
