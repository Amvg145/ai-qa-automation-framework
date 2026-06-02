pipeline{
    agent any
    stages {
        stage('Checkout'){
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies'){
            steps{
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Install Playwright Browser'){
            steps{
                bat 'playwright install'
            }
        }
        stage('Run API Tests'){
            steps{
                bat 'pytest api_tests -v'
            }
        }
        stage('Run UI Tests') {
            steps {
                bat 'pytest ui_tests -v'
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat 'pytest --alluredir=reports'
            }
        }
    }
    post {

        always {

            archiveArtifacts(
                artifacts: 'reports/*',
                fingerprint: true
            )
        }
    }
}