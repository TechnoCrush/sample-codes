pipeline {
    agent any
    stages{
        stage('Sonar Scanner'){
        def scannerhome = tool 'sonar-scanner';
        withSonarQubeEnv('sonarqube'){

            sh """${scannerhome}/bin/sonar-runner -D sonar.login=admin -D sonar.password=qwerty -D sonar.sources=. """

        }
    }

    }    
}