pipeline {
  agent {
    docker {
      image 'docker:latest'
      args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
  }
  options {
    // Set an absolute workspace path
    workspace("$PWD/.")
  }
  stages {
    stage('Clone') {
      steps {
        git 'https://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@github.com/David-kdw/school_information_webapp.git'
      }
    }
    stage('Build') {
      steps {
        sh 'docker-compose -f . build'
      }
    }
    stage('Test') {
      steps {
        sh 'docker-compose -f . up -d db'
        sh 'docker-compose -f . up -d sonarqube'
        sh 'docker-compose -f . --rm app pytest'
      }
      post {
        always {
          sh 'docker-compose -f . down -v'
        }
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker-compose -f . up -d'
      }
    }
  }
}
