# Chris Hickman

**Identity security and platform engineering**

I'm an IT and identity security professional with hands-on work across IAM. I treat identity as a control plane: least privilege, just-in-time and privileged access, non-human identities, and catching drift before it turns into exposure. Lately that includes AI agents, which I think need the same isolation and least privilege as any other identity. These are the labs and tools I build to work through those problems.

## What I'm working on

I build things in my spare time, picking up projects whenever time allows and whatever has my attention right now.

| Project | What it is | Status |
| --- | --- | --- |
| [Lab-in-a-Box](https://github.com/chriswayneh/lab-in-a-box) | Self-hosted identity governance lab with Keycloak, Vault, and Gitea | v2.0.2 |
| [Local MCP Toolbox](https://github.com/chriswayneh/local-mcp-toolbox) | Read-only MCP server with allowlists, redaction, and audit records | v1.5.3 |
| [kube-foundry](https://github.com/chriswayneh/kube-foundry) | Local Kubernetes platform with GitOps, policies, and tested rollback | v1.1.0 |
| [detdrift](https://github.com/chriswayneh/detdrift) | Flags detection rules broken by telemetry schema changes | v1.0.1 |
| [RedDock](https://github.com/chriswayneh/RedDock) | Local scoped discovery and evidence tool for authorized environments | v0.8.1, in progress |
| [TerraForma-IaC](https://github.com/chriswayneh/TerraForma-IaC) | Generates readable Terraform from guided inputs; does not deploy | v0.3.0 |
| [crowdkeeper](https://github.com/chriswayneh/crowdkeeper) | Access audits and joiner, mover, leaver automation for Atlassian Crowd | v0.2.1 |
| [acasentry](https://github.com/chriswayneh/acasentry) | Access and identity review for Azure Container Apps | v0.2.1 |
| bbwarden | CLI tool for Bitbucket | In progress, coming soon |
| Linchpin | Personal project | In progress, coming soon |
| [JobDorking](https://jobdorking.com) | One Google search across job boards and career pages | Inactive |

## Featured projects

### [Lab-in-a-Box](https://github.com/chriswayneh/lab-in-a-box)

A Docker Compose lab for identity lifecycle automation, access reviews, and secrets management using Keycloak, Vault, and Gitea. Monitoring includes Grafana and Alertmanager, with OIDC sign-in and role-based access to selected interfaces.

[v2.0.2](https://github.com/chriswayneh/lab-in-a-box/releases/tag/v2.0.2) · [Documentation](https://github.com/chriswayneh/lab-in-a-box#readme)

### [Local MCP Toolbox](https://github.com/chriswayneh/local-mcp-toolbox)

A read-only MCP server for inspecting approved files, Git and GitHub metadata, logs, container health, and Python environments. Access is limited by explicit allowlists, with output limits, redaction, and audit records.

[v1.5.3](https://github.com/chriswayneh/local-mcp-toolbox/releases/tag/v1.5.3) · [Documentation](https://github.com/chriswayneh/local-mcp-toolbox#readme) · [Release verification](https://github.com/chriswayneh/local-mcp-toolbox/blob/main/docs/release-1.5.md)

### [crowdkeeper](https://github.com/chriswayneh/crowdkeeper)

A CLI for Atlassian Crowd admins that finds inactive and orphaned accounts, tracks group membership drift, and applies joiner, mover, and leaver changes. Changes are dry-run by default and every applied change is written to an audit log.

[v0.2.1](https://github.com/chriswayneh/crowdkeeper/releases/tag/v0.2.1) · [Documentation](https://github.com/chriswayneh/crowdkeeper#readme)

### [acasentry](https://github.com/chriswayneh/acasentry)

A CLI for access and identity review of Azure Container Apps: role assignments, internet-reachable apps, secrets not in Key Vault, and apps without a managed identity. Its two fix commands print dry-run plans unless told to apply.

[v0.2.1](https://github.com/chriswayneh/acasentry/releases/tag/v0.2.1) · [Documentation](https://github.com/chriswayneh/acasentry#readme)

### [kube-foundry](https://github.com/chriswayneh/kube-foundry)

A local Kubernetes platform built on kind with Argo CD, default-deny networking, scoped RBAC, admission policies, and TLS routing. Includes tested procedures for image promotion, rollback, and database recovery on a three-node cluster.

[v1.1.0](https://github.com/chriswayneh/kube-foundry/releases/tag/v1.1.0) · [Documentation](https://github.com/chriswayneh/kube-foundry#readme) · [Test results](https://github.com/chriswayneh/kube-foundry/blob/v1.1.0/docs/operational-proof.md#acceptance-record)

### [detdrift](https://github.com/chriswayneh/detdrift)

A CLI and GitHub Action that checks whether telemetry changes remove fields referenced by detection rules. Supports Sigma, with optional KQL/SPL field extraction, and produces reports and exit codes for CI.

[v1.0.1](https://github.com/chriswayneh/detdrift/releases/tag/v1.0.1) · [Documentation](https://github.com/chriswayneh/detdrift#readme) · [Architecture](https://github.com/chriswayneh/detdrift/blob/main/ARCHITECTURE.md)

### [RedDock](https://github.com/chriswayneh/RedDock)

A local security assessment platform for scoped host and TCP service discovery, HTTP header checks, and TLS certificate checks. Findings link to retained evidence and can be exported in reports and DockPacks.

[v0.8.1](https://github.com/chriswayneh/RedDock/releases/tag/v0.8.1) · [Documentation](https://github.com/chriswayneh/RedDock#readme) · [Security model](https://github.com/chriswayneh/RedDock/blob/master/SECURITY.md)

### [TerraForma-IaC](https://github.com/chriswayneh/TerraForma-IaC)

A tool that creates Terraform configuration files from answers to simple questions, to make cloud setups easier to understand, check, and repeat. It generates the files but does not deploy them yet.

[v0.3.0](https://github.com/chriswayneh/TerraForma-IaC/releases/tag/v0.3.0) · [Documentation](https://github.com/chriswayneh/TerraForma-IaC#readme)

### bbwarden (coming soon)

A CLI tool for Bitbucket. Still private while I finish it.

### Linchpin (coming soon)

A personal project I'm working on. Still private while I finish it.

## Other work

### [JobDorking](https://jobdorking.com) (inactive)

A site that builds one Google search across job boards and company career pages. I'm not actively working on it, and the source is private.

## Contact

[LinkedIn](https://www.linkedin.com/in/chriswhickman/)
