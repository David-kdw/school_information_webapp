pipeline {
  agent {
    docker {
      image 'docker:latest'
      args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
  }
  options {
    
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker-compose build'
      }
    }
    stage('Test') {
      agent {
        docker {
          image 'docker:latest'
          args '-v /var/run/docker.sock:/var/run/docker.sock'
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
        docker {
          image 'jenkins/jenkins:lts'
          args '--workdir=/root'
          mountDocker true
          workDir '/var/jenkins_home'
        }
      }
      steps {
        sh 'docker-compose up -d'
      }
    }
  }
}
