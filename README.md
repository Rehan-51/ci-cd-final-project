# DevOps Capstone Project

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://shields.io/)
[![CI Build](https://github.com/Rehan-51/devops-capstone-project/actions/workflows/workflow.yml/badge.svg)](https://github.com/Rehan-51/devops-capstone-project/actions)

## Project Name Details

**Project Name:** Account REST API Service  
**Repository:** devops-capstone-project  
**Course:** IBM DevOps and Software Engineering Professional Certificate - DevOps Capstone Project  
**Author:** Rehan  

## Description

This repository contains the microservice for the Account REST API Service developed as part of the **IBM DevOps and Software Engineering Professional Certificate Capstone Project**. It demonstrates end-to-end DevOps practices including:
- Test Driven Development (TDD) and Behavior Driven Development (BDD)
- Continuous Integration (CI) with GitHub Actions (linting with `flake8` and unit testing with `nosetests`)
- Containerization with Docker
- Continuous Delivery (CD) using Tekton pipelines on OpenShift / Kubernetes

## Project Layout

```text
├── service/        <- microservice package
│   ├── common/     <- common log and error handlers
│   ├── config.py   <- Flask configuration object
│   ├── models.py   <- persistent model
│   └── routes.py   <- REST API routes
├── .github/        <- GitHub Actions CI workflows
│   └── workflows/
│       ├── ci-build.yaml
│       └── workflow.yml
├── .tekton/        <- Tekton CD pipeline definitions
│   ├── tasks.yml
│   └── pipeline.yaml
├── Dockerfile      <- container image specification
└── tests/          <- test cases (nosetests)
```

## Running the Service

```bash
gunicorn --bind=0.0.0.0:8000 --log-level=info service:app
```

## License

Licensed under the Apache License, Version 2.0.
