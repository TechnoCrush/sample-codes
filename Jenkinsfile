pipeline {
    agent any 
    stages {
       stage('SQ Analysis')
        {
            steps{
                withSonarQubeEnv('sonarqube'){
                    sh "sonar-scanner -Dsonar.projectKey=demo-python -Dsonar.host.url=http://18.219.103.233:9000 -Dsonar.login=admin -Dsonar.password=qwerty"
                }
                
            }
            
        }
        stage('Quality Gate')
        {
            steps{
                sleep(10)
                waitForQualityGate abortPipeline: true
            }
        }
        
    }
    post {
        cleanup {
            cleanWs()
            }
    }
}