This repository would guide you through deploying a sample deployment on your Kubernetes cluster via Portainer GitOps.

## Prerequisites
1. An existing Kubernetes cluster.
1. A Portainer Agent/Server deployed in Cluster. If you don’t have an existing Portainer deployment, you can follow this [tutorial]( https://install.portainer.io/) to install the GUI. 

## To deploy a sample application 
After you have followed the [tutorial]( https://install.portainer.io/) you should be able to access the Portainer Dashboard. 
1.	Navigate to the left panel and click on `Application`
2.	Click on Create from Manifest
3.	Select the Namespace and assign a name to your Application
4.	For Build Method, select ` Git Repository `
5.	The deployment Type would be ` Kubernetes`
6.	Repository URL: https://github.com/hrittikhere/portainer-demo
7.	Repository Reference would be ` refs/heads/main ` as the repository is on the main branch
8.	Compose Path: ` portainer-deployment.yaml `
9.	Uncheck Authentication as this is a public repository
10.	Click on Deploy 

Your Application would be running, and you can access that on http://localhost:3111/ 

