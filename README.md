# Chris Hickman

**Security & Infrastructure Engineer**

My work spans identity and access management, systems engineering, and security engineering. I build software and automation for account lifecycle management, access controls, infrastructure delivery, and security assessment.

## Featured projects

### [Lab-in-a-Box](https://github.com/chriswayneh/lab-in-a-box)

A self-hosted infrastructure and identity lab built with Docker Compose, Keycloak, Vault, and Gitea. Includes joiner/mover/leaver automation, RBAC analysis, access-review campaigns, and secrets management.

Version 2.0 adds OIDC-based access controls through Traefik and oauth2-proxy, role-based access to monitoring interfaces, and Alertmanager routing.

[v2.0.0](https://github.com/chriswayneh/lab-in-a-box/releases/tag/v2.0.0) · [Documentation](https://github.com/chriswayneh/lab-in-a-box#readme)

### [kube-foundry](https://github.com/chriswayneh/kube-foundry)

A local Kubernetes reference platform built on kind, with Argo CD delivery, default-deny networking, scoped RBAC, admission policies, TLS routing, and monitoring.

Version 1.1 includes tested workflows for image promotion and rollback, policy rejection and remediation, and database restore verification. Acceptance testing was performed on an isolated three-node cluster.

[v1.1.0](https://github.com/chriswayneh/kube-foundry/releases/tag/v1.1.0) · [Documentation](https://github.com/chriswayneh/kube-foundry#readme) · [Test results](https://github.com/chriswayneh/kube-foundry/blob/v1.1.0/docs/operational-proof.md#acceptance-record)

### [Local MCP Toolbox](https://github.com/chriswayneh/local-mcp-toolbox)

A read-only MCP server that gives AI clients controlled access to local files, Git and GitHub metadata, logs, container health, and static Python checks. Uses explicit allowlists, output limits, centralized redaction, and audit records.

[v1.5.2](https://github.com/chriswayneh/local-mcp-toolbox/releases/tag/v1.5.2) · [Documentation](https://github.com/chriswayneh/local-mcp-toolbox#readme) · [Release verification](https://github.com/chriswayneh/local-mcp-toolbox/blob/main/docs/release-1.5.md)

### [detdrift](https://github.com/chriswayneh/detdrift)

A CLI and GitHub Action for identifying detection rules affected by telemetry schema changes. Compares before-and-after event samples to flag missing fields used by Sigma rules, with optional KQL and SPL support. Produces structured reports and exit codes for CI pipelines.

[v1.0.0](https://github.com/chriswayneh/detdrift/releases/tag/v1.0.0) · [Documentation](https://github.com/chriswayneh/detdrift#readme) · [Architecture](https://github.com/chriswayneh/detdrift/blob/main/ARCHITECTURE.md)

### [RedDock](https://github.com/chriswayneh/RedDock)

A security assessment platform for vulnerability discovery and validation in authorized local environments. Enforces target scope, restricts tool arguments, requires separate approval for validation, and links findings to supporting evidence.

[v0.8.1](https://github.com/chriswayneh/RedDock/releases/tag/v0.8.1) · [Documentation](https://github.com/chriswayneh/RedDock#readme) · [Security model](https://github.com/chriswayneh/RedDock/blob/master/SECURITY.md)

## Other work

### [JobDorking](https://jobdorking.com)

A job-search workspace with targeted queries, saved searches, and optional cloud sync. Development is currently inactive.

## Contact

[LinkedIn](https://www.linkedin.com/in/chriswhickman/)
