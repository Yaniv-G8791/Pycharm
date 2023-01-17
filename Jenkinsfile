pipeline {
agent any
stages {
stage('checkout') {
steps {
git 'https://github.com/Yaniv-G8791/Pycharm'
}
}
stage('build') {
steps {
bat 'python /tree/master/Project/rest_app.py'
}
}
}
}
