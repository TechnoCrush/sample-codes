pipeline {
    agent any 
    stages {
        stage('SCM Checkout'){
            steps {
                git 'https://github.com/buddy-works/simple-java-project.git'
            }
        }

        stage('SQ Analysis')
        {
            sh "sonar-scanner -Dsonar.projectKey=demo-python -Dsonar.sources=. -Dsonar.host.url=http://18.219.103.233:9000 -Dsonar.login=admin"
        }
        
        }
}