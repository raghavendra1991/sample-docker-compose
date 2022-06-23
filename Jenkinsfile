// Declarative pipeline
pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub')
    }

    stages {
        
        stage ('Build Docker Image') {
            steps {
                sh 'docker-compose build '       
            }
        }
        stage ('Rename Docker Image') {
            steps {
                sh 'docker tag docker-compose-feature2_webapp raghaduvva/dcapp'
                sh 'docker tag docker-compose-feature2_db raghaduvva/dcdb'       
            }
        }
        stage ('Login DockerHub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR  --password-stdin'       
            }
        }
        stage ('Deploy Docker images') {
            steps {
                sh 'docker push raghaduvva/dcapp'
                sh 'docker push raghaduvva/dcdb'

            }
        }
        stage ('Remove Unused Docker Images') {
            steps {
                sh 'docker rmi -f $(docker images -a -q)'
            }
        }
    }
}
