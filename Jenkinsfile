pipeline {
        agent {
                docker {
                        image 'xsteadfastx/tox-python:minimal'
                }
        }
        environment {
                TOX_WORK_DIR = '/tmp'
        }
        stages {
                stage('Test') {
                        steps {
                                sh 'sudo apk add --no-cache git make'
                                sh 'tox -e py36'
                                sh 'tox -e py37'
                                sh 'tox -e flake8'
                                sh 'tox -e pylint'
                                sh 'tox -e black-only-check'
                                sh 'tox -e cookiecutter'
                        }
                }
        }
}
