## Development Workflow & CI/CD Architecture

To maintain a professional, secure, and highly deterministic build environment aligned with strict software supply chain standards, this repository enforces a DevSecOps pipeline using GitHub Actions.

### 1. Version Control Hygiene (Jupyter Notebooks)
Jupyter notebooks (`.ipynb`) store execution counts, outputs, and metadata that cause severe Git conflicts and pose a risk of leaking sensitive data or proprietary charts. 
* **Requirement:** All developers must use `nbstripout` to automatically strip outputs before committing.
* **Local Setup:** Run `pip install nbstripout && nbstripout --install` to configure your local Git hooks.

### 2. Automated Code Quality and Formatting
To prevent style conflicts and maintain a readable, enterprise-grade codebase, we enforce strict deterministic formatting.
* **Tooling:** We utilize `Ruff` as a unified, ultra-fast linter and formatter for both `.py` scripts and `.ipynb` notebooks.
* **Enforcement:** The CI/CD pipeline will automatically reject pull requests that fail formatting checks (`ruff check` and `ruff format`).

### 3. Software Supply Chain Security
Python's ecosystem is vulnerable to malicious packages. Security is shifted left to catch vulnerabilities early.
* **SCA (Software Composition Analysis):** The pipeline utilizes `pip-audit` to automatically scan all local dependencies against known CVE databases during every build. 

### CI/CD Trigger Mechanism
The GitHub Actions workflow (`.github/workflows/ci.yml`) is triggered automatically on pushes and pull requests to the `main` and `develop` branches. It handles environment setup, notebook cleanup verification, security scanning, and automated testing via `pytest`.