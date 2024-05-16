pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                echo 'Stage1: Checkout from GITHUB'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/AnkurGuptaDhuri/12_JenkinsDockerAnsiblekubectl.git']])
            }
        }
        /* stage('Build Docker Image from Dockerfile') {
            steps {
                echo 'Stage2: Build docker Image'
                sh 'docker --version'
                echo 'Build number is ${BUILD_ID}'
                sh 'docker build -t flaskapp:1.${BUILD_ID} .'
            }
        }
         
        stage('Push Image to Docker Hub') {
            steps {
                echo 'Stage3: Image push to Docker Hub'
                withCredentials([string(credentialsId: 'docker_hub_pwd_token', variable: 'docker_hub_pwd')]) {
                    // some block
                    sh 'docker tag flaskapp:1.${BUILD_ID} ankur5yk/12_flaskjenkinsansiblekubernetes:1.${BUILD_ID}'
                    sh "docker login -u ankur5yk -p ${docker_hub_pwd}"
                    sh 'docker push ankur5yk/12_flaskjenkinsansiblekubernetes:1.${BUILD_ID}'
                    
                    sh 'docker tag flaskapp:1.${BUILD_ID} ankur5yk/12_flaskjenkinsansiblekubernetes:latest'
                    sh 'docker push ankur5yk/12_flaskjenkinsansiblekubernetes:latest'
                }
                              
            }
        }
        stage('Remove the old images from Jenkins docker') {
            steps {
                sh 'docker rmi flaskapp:1.${BUILD_ID}'
                sh 'docker rmi ankur5yk/12_flaskjenkinsansiblekubernetes:1.${BUILD_ID}'
                sh 'docker rmi ankur5yk/12_flaskjenkinsansiblekubernetes:latest'
            }
        }*/
        stage('Ansible: copy the files to ansible server'){
            steps {
		        sshagent(['ansible-ubuntu']) {
                    // some block
                    sh 'ssh -o StrictHostKeyChecking=no ubuntu@172.31.44.21'
                	sh 'scp -r /var/lib/jenkins/workspace/12_FlaskJenkinsAnsibleKubernetes/* ubuntu@172.31.44.21:/home/ubuntu'
            	}
	        }
        }

    }
}
