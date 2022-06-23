// Declarative pipeline
pipeline {
    agent any

    stages {
        
        stage ('Build Docker Image') {
            steps {
                sh 'docker-compose build '       
            }
        }
    }
}
