pipeline {
    agent any
    stages {
        stage ('Checkout') {
            steps {
                git 'https://github.com/example/project.git'

            }

        }
        stage('Build') { 
            steps  {
                sh'make'
            } 
        }
        stage('Deployment') 
            steps { 
                sh 'scp build/output.jar userserver@:/deploy/directory '
            }              
        }
    }
}        