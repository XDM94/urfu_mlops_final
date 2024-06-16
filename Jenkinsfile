pipeline {
    agent any

//     environment {
//         JENKINS_HOME = "$JENKINS_HOME"
//         BUILD = "${JENKINS_HOME}/workspace/urfu_mlops_final"
//     }

    stages {
         stage('Start') {
            steps {
                script {
                    echo 'Начало работы скриптов.'
                }
            }
        }
        stage('Preparation') {
            steps {
                // Очистка рабочего пространства
                cleanWs()
                checkout scm
            }
        }

        stage('Checkout') {
            steps {
                script {
                    // Получаем исходный код из репозитория Git
                    git branch: 'main', url: 'https://github.com/XDM94/urfu_mlops_final.git'
                }
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                // Создание виртуального окружения
                script {
                    if (isUnix()) {
                        sh 'python -m venv venv'
                    }
                }
            }
        }

        stage('Activate venv') {
            steps {
                // Активация виртуального окружения
                script {
                    if (isUnix()) {
                        sh './venv/scripts/activate/'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                // установка зависимостей
                script {
                    if (isUnix()) {
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Create dataset Titanic') {
            steps {
                script {
                    // Создаем датасет
                    if (isUnix()) {
                        dir('src') {
                            sh 'python create_dataset.py'
                            //sh 'python create_dataset.py'
                        }
                    }
                }
            }
        }

        stage('Create model Titanic') {
            steps {
                script {
                    // Создаем и обучаем модель
                    if (isUnix()) {
                        dir('src') {
                            sh 'python create_model.py'
                        }
                    }
                }
            }
        }

        stage('App tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'pytest -v'
                    }
                }
            }
        }

        stage('Build Docker image') {
            steps {
                 script {
                    // Для Линукс
                    if (isUnix()) {
                        sh 'sudo docker build -t titanic-img .'
                    }
                 }
            }
        }

        stage('Finish') {
            steps {
                script {
                    echo 'Работа скриптов завершена успешно'
                }
            }
        }
    }
}