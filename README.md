# Chris Hickman

**IAM and Platform Engineer**. I design identity workflows, access controls, and container-native platforms you can run, inspect, and verify locally.

Day-to-day focus: account lifecycle, least-privilege access, integration troubleshooting, and making auth and ops failures diagnosable. Portfolio work below shows the same ideas as runnable labs and reference platforms, with documented trust boundaries rather than marketing claims.

## Featured projects

### [lab-in-a-box](https://github.com/chriswayneh/lab-in-a-box) - identity + infra lab (v2.0.0)

One-command Docker Compose lab: Keycloak, Vault, Gitea, Traefik, Prometheus/Alertmanager/Grafana, and more. [v2.0.0](https://github.com/chriswayneh/lab-in-a-box/releases/tag/v2.0.0) adds Traefik ForwardAuth (oauth2-proxy + Keycloak OIDC/PKCE and realm roles), Alertmanager routing, and hardened observability UI access.

Also includes joiner/mover/leaver automation, a read-only RBAC simulator ("what can this person reach, and why?"), access-review campaigns, and Vault ACL policies. Local lab with documented defaults, not an internet-hardened product.

[Release notes](https://github.com/chriswayneh/lab-in-a-box/releases/tag/v2.0.0) · [README](https://github.com/chriswayneh/lab-in-a-box#readme)

### [kube-foundry](https://github.com/chriswayneh/kube-foundry) - local Kubernetes reference platform (v1.0.0)

Kind-based platform for deploying apps, validating infra changes, and testing recovery without cloud spend. Ships Argo CD GitOps, default-deny networking, scoped observer RBAC, admission policies, TLS routing, monitoring, and verified database recovery. Sample app has no user auth; cluster admins remain trusted operators.

[v1.0.0](https://github.com/chriswayneh/kube-foundry/releases/tag/v1.0.0) · [Architecture](https://github.com/chriswayneh/kube-foundry#readme) · [Verification](https://github.com/chriswayneh/kube-foundry/blob/main/docs/release.md#acceptance-record)

### [local-mcp-toolbox](https://github.com/chriswayneh/local-mcp-toolbox) - read-only MCP inspection (v1.5.2)

Local MCP server scoped to approved files, Git/GitHub metadata, logs, container health, and static Python checks. Controls: explicit allowlists, bounded output, central redaction, sanitized audit records. No arbitrary command execution or mutation tools.

[v1.5.2](https://github.com/chriswayneh/local-mcp-toolbox/releases/tag/v1.5.2) · [README](https://github.com/chriswayneh/local-mcp-toolbox#readme) · [Limits & verification](https://github.com/chriswayneh/local-mcp-toolbox/blob/main/docs/release-1.5.md)

### [detdrift](https://github.com/chriswayneh/detdrift) - detection drift check (v0.5.0)

CLI and CI check for detection field drift (Sigma default; optional KQL): compare before/after NDJSON samples and report which rules would go quiet when fields disappear from a mapping change. Offline, exit-code friendly, not a SIEM and not a matcher. Complements pipeline and detection-as-code work without owning ingest.

[v0.4.2](https://github.com/chriswayneh/detdrift/releases/tag/v0.5.0) · [README](https://github.com/chriswayneh/detdrift#readme) · [Architecture](https://github.com/chriswayneh/detdrift/blob/main/ARCHITECTURE.md) · [Roadmap](https://github.com/chriswayneh/detdrift/blob/main/ROADMAP.md)

### [RedDock](https://github.com/chriswayneh/RedDock) - authorized assessment tooling

Vulnerability discovery and validation for authorized local environments: fail-closed target scope checks, fixed tool arguments, separate validation approvals, and evidence-linked findings. Operator boundary is local authorization, not shared multi-tenant access control.

## Other

### [JobDorking](https://jobdorking.com)

Personal job-search workspace (targeted queries, tracking; optional cloud sync with server-verified sessions). Development currently inactive.

## How I write about security

I prefer naming mechanisms (OIDC, forward-auth, least privilege, policy-as-code, allowlists, audit evidence) over slogans. When a project borrows from zero trust, its README states what is enforced and what is still trusted (see [lab-in-a-box security notes](https://github.com/chriswayneh/lab-in-a-box#security)).

## Contact

[LinkedIn](https://www.linkedin.com/in/chriswhickman/) · [GitHub](https://github.com/chriswayneh)
