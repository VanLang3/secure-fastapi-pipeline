# Secure-FastAPI-Pipeline 🛡️

A professional DevSecOps project demonstrating a **"Shift Left"**(securing code early in the process) security strategy. This repository automates the identification of vulnerabilities in both proprietary code and third-party dependencies(libraries) before deployment.



## 🚀 The Mission
In modern software engineering, security cannot be an afterthought. This project integrates security directly into the **Software Development Life Cycle (SDLC)** using an automated CI/CD pipeline.

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **Framework:** FastAPI (High-performance REST API)
* **Automation:** GitHub Actions (CI/CD)
* **Security (SAST):** Bandit (scans code)
* **Security (SCA):** Trivy (scans libraries for CVEs)
* **Cloud:** AWS (Deployment Target)

## 🏗️ Architecture
1. **Developer Push:** Code is pushed to the `main` branch.
2. **CI Trigger:** GitHub Actions wakes up a virtual Ubuntu runner.
3. **Security Gate 1 (Bandit):** Performs **Static Application Security Testing (SAST)** to find hardcoded secrets or logical flaws.
4. **Security Gate 2 (Trivy):** Performs **Software Composition Analysis (SCA)** to find known vulnerabilities (CVEs) in `requirements.txt`.
5. **Deployment:** Only if both gates are **GREEN** does the code proceed to AWS.

## 🛑 Failure Example
If a developer accidentally pushes a hardcoded password:
- **Bandit** will detect a "High Severity" issue.
- The pipeline will return a **Red X**.
- The deployment is blocked, protecting the production environment.
