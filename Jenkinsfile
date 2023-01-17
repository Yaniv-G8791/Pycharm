pipeline {
agent any
stages {
stage('checkout') {
steps {
git 'https://github.com/Yaniv-G8791/Pycharm/'
}
}
stage('build') {
steps {
bat 'python rest_app.py'
}
}
}
}
