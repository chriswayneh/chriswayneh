# Chris Hickman

**Identity and infrastructure security**

Experienced IT and identity security engineer, with hands-on work across IAM. GitHub is the technical side: access control, local platforms, and evidence you can read.

## Featured projects

### [Lab-in-a-Box](https://github.com/chriswayneh/lab-in-a-box)

A Docker Compose lab for identity lifecycle automation, access reviews, and secrets management using Keycloak, Vault, and Gitea. Monitoring includes Grafana and Alertmanager, with OIDC sign-in and role-based access to selected interfaces.

[v2.0.0](https://github.com/chriswayneh/lab-in-a-box/releases/tag/v2.0.0) · [Documentation](https://github.com/chriswayneh/lab-in-a-box#readme)

### [kube-foundry](https://github.com/chriswayneh/kube-foundry)

A local Kubernetes platform built on kind with Argo CD, default-deny networking, scoped RBAC, admission policies, and TLS routing. Includes tested procedures for image promotion, rollback, and database recovery on a three-node cluster.

[v1.1.0](https://github.com/chriswayneh/kube-foundry/releases/tag/v1.1.0) · [Documentation](https://github.com/chriswayneh/kube-foundry#readme) · [Test results](https://github.com/chriswayneh/kube-foundry/blob/v1.1.0/docs/operational-proof.md#acceptance-record)

### [Local MCP Toolbox](https://github.com/chriswayneh/local-mcp-toolbox)

A read-only MCP server for inspecting approved files, Git and GitHub metadata, logs, container health, and Python environments. Access is limited by explicit allowlists, with output limits, redaction, and audit records.

[v1.5.2](https://github.com/chriswayneh/local-mcp-toolbox/releases/tag/v1.5.2) · [Documentation](https://github.com/chriswayneh/local-mcp-toolbox#readme) · [Release verification](https://github.com/chriswayneh/local-mcp-toolbox/blob/main/docs/release-1.5.md)

### [detdrift](https://github.com/chriswayneh/detdrift)

A CLI and GitHub Action that checks whether telemetry changes remove fields referenced by detection rules. Supports Sigma, with optional KQL/SPL field extraction, and produces reports and exit codes for CI.

[v1.0.0](https://github.com/chriswayneh/detdrift/releases/tag/v1.0.0) · [Documentation](https://github.com/chriswayneh/detdrift#readme) · [Architecture](https://github.com/chriswayneh/detdrift/blob/main/ARCHITECTURE.md)

### [RedDock](https://github.com/chriswayneh/RedDock)

A local security assessment platform for scoped host and TCP service discovery, HTTP header checks, and TLS certificate checks. Findings link to retained evidence and can be exported in reports and DockPacks.

[v0.8.1](https://github.com/chriswayneh/RedDock/releases/tag/v0.8.1) · [Documentation](https://github.com/chriswayneh/RedDock#readme) · [Security model](https://github.com/chriswayneh/RedDock/blob/master/SECURITY.md)

### [TerraForma-IaC](https://github.com/chriswayneh/TerraForma-IaC)

Create cloud configuration by answering questions instead of writing Terraform syntax from scratch. Terraform is a set of text files describing servers, networks, storage, and access rules so a setup can be reviewed and repeated.

For example, choose an AWS web server, name it, and select its access and encryption options. TerraForma produces editable Terraform files for the server and supporting infrastructure, explains what they describe, and offers local checks with Terraform and TFLint. It runs on your own computer through a browser interface or a command-line questionnaire, with templates for AWS, Azure, and Google Cloud.

**Current scope:** v0.2.0 generates, explains, exports, and validates configuration; it also reviews existing Terraform plan JSON. It does not create cloud resources or run plan/apply/destroy. Development on `main` adds richer input questions and initial Linux VM templates. Complete Linux/Windows VM configuration and approved deployment are planned.

[v0.2.0](https://github.com/chriswayneh/TerraForma-IaC/releases/tag/v0.2.0) · [Documentation](https://github.com/chriswayneh/TerraForma-IaC#readme) · [Roadmap](https://github.com/chriswayneh/TerraForma-IaC/blob/main/docs/ROADMAP.md)

## Other work

### [JobDorking](https://jobdorking.com)

A live site that was public and is now producing. The source stays private. It builds one Google search across job boards and company career pages. No GitHub release; the private source tracks `main`.

### [Hello Due](https://hellodue.com)

A live site that was public and is now producing. The source stays private. It offers a rate calculator, an invoice generator, and paid downloadable packs.

## Contact

[LinkedIn](https://www.linkedin.com/in/chriswhickman/)
