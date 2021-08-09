pipeline {
    agent any
    stages{
        steps('Sonar Scanner'){
        def scannerhome = tool 'sonar-scanner';
        withSonarQubeEnv('sonarqube'){

            sh """${scannerhome}/bin/sonar-runner -D sonar.login=admin -D sonar.password=qwerty -D sonar.sources=. """

        }
    }

    }    
}