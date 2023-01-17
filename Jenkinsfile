pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/Yaniv-G8791/Pycharm'
            }
        }
        stage('setup import libs') {
            steps {
                bat 'python -m pip install pymysql'

            }
            stage('build') {
                steps {
                    bat 'cd Project & python rest_app.py'

                }
            }
        }
    }
