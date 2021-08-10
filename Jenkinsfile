pipeline {
    agent any 
    stages {
       stage('SQ Analysis')
        {
            steps{
                sh "sonar-scanner -Dsonar.projectKey=demo-python -Dsonar.sources=. -Dsonar.host.url=http://18.219.103.233:9000 -Dsonar.login=admin"
            }
            
        }
        
        }
}