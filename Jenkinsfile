pipeline {
  agent {
    docker {
      image 'docker:latest'
      args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
  }
  stages {
    stage('Build') {
      steps {
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
