# Automated-MLOps-Pipeline-for-Scalable-Sentiment-Classification

This project is an **end-to-end Production-Grade Sentiment Classification MLOps Pipeline** designed for robust, scalable, and automated machine learning deployments. It encompasses the entire ML lifecycle, from data versioning and experimentation to continuous model deployment and monitoring.

## Project Objectives

The core objectives of this project were to establish a comprehensive MLOps framework that enables:

* **Experiments:** Efficient management and tracking of machine learning experiments.
* **Code and Data Versioning:** Robust version control for both code and large datasets, ensuring reproducibility.
* **Data Ingestion from S3:** Streamlined process for ingesting and managing data directly from AWS S3.
* **Pipeline Build and Automation:** Automated construction and orchestration of the entire machine learning pipeline.
* **Model Registry:** Centralized system for versioning, tracking, and managing the lifecycle of trained models.
* **Model Serving:** Deploying models as scalable services for real-time inference.
* **Model Retraining:** Implementing mechanisms for automated model retraining to maintain performance.
* **CI/CD:** Continuous Integration and Continuous Deployment for automated testing and deployment of ML assets.
* **Kubernetes (EKS) Deployment:** Deploying and managing containerized applications on a Kubernetes cluster (AWS EKS).
* **Monitoring & Alerting:** Comprehensive monitoring of pipeline health, model performance, and system resources, with integrated alerting.

## Tools Stack

This project leverages a modern and robust MLOps technology stack to achieve its objectives:

* **Cookiecutter:** Used for project scaffolding and maintaining a standardized project structure.
* **DVC (Data Version Control):** For managing and versioning large datasets and machine learning models alongside code.
* **MLflow:** Employed for experiment tracking, model logging, and a lightweight model registry.
* **Git - GitHub Actions:** Git for source code version control, with GitHub Actions enabling powerful CI/CD workflows for automation.
* **Docker:** For containerizing all application services and ML models, ensuring consistent environments.
* **AWS:** As the primary cloud provider, utilizing key services including:
    * **S3:** For scalable and secure data storage.
    * **IAM:** For managing access and permissions.
    * **ECR (Elastic Container Registry):** For storing and managing Docker images.
    * **EKS (Elastic Kubernetes Service):** For managed Kubernetes clusters to deploy scalable ML services.
    * **CloudFormation:** For infrastructure as code (IaC) to provision and manage AWS resources.
    * **EC2:** For virtual compute instances, including Kubernetes worker nodes.
* **Kubernetes:** The container orchestration platform managing deployed services.
* **Prometheus-Grafana:** For comprehensive monitoring of system metrics, application performance, and setting up alerts.
* **Pre-requisites:** (This typically refers to foundational tools like `kubectl`, `aws cli`, `minikube` for local development, Python, etc.)

VISIT - [click](https://docs.google.com/document/d/1iUCK06895yOGELGyTAdYr9SRYbzywLPY/edit?usp=sharing&ouid=101578109680909709365&rtpof=true&sd=true)

---
