pipeline {
        agent {
                dockerfile {
                        filename 'Dockerfile.tests'
                }
        }
        stages {
                stage('Test') {
                        steps {
                                sh 'tox -e py36'
                                sh 'tox -e py37'
                                sh 'tox -e flake8'
                                sh 'tox -e pylint'
                                sh 'tox -e mypy'
                        }
                }
        }
}
