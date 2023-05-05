pipeline {
  agent {
    docker {
      image 'jenkins/jenkins:lts'
      args '-p 8080:8080 -v /var/jenkins_home:/var/jenkins_home'
    }
  }
  stages {
    stage('Build') {
      
        {
        sh 'docker-compose build'
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
