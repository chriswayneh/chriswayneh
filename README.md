# Chris Hickman

Senior security and support engineer focused on identity and access, infrastructure, and reliable operations. My work includes account lifecycle management, access controls, integration troubleshooting, and the investigation of failed logins and automated jobs.

My projects apply zero-trust principles through explicit authorization, least privilege, bounded capabilities, and reviewable evidence. I document the controls each project implements, the identities and infrastructure it still trusts, and the limits of its supported deployment. These are concrete engineering choices, not a blanket security certification.

## Projects

### [kube-foundry](https://github.com/chriswayneh/kube-foundry)

A local Kubernetes reference platform for deploying applications, validating infrastructure changes, and testing recovery without cloud infrastructure. Version 1.0.0 includes Argo CD GitOps delivery, default-deny application networking, scoped observer RBAC, admission policies, TLS routing, monitoring, and verified database recovery. These support zero-trust principles at workload boundaries; the sample application has no user authentication, and cluster administrators remain trusted.

[v1.0.0 release](https://github.com/chriswayneh/kube-foundry/releases/tag/v1.0.0) | [Architecture and setup](https://github.com/chriswayneh/kube-foundry#readme) | [Verification results](https://github.com/chriswayneh/kube-foundry/blob/main/docs/release.md#acceptance-record)

### [lab-in-a-box](https://github.com/chriswayneh/lab-in-a-box)

An identity and infrastructure lab built with Keycloak, Vault, and Gitea. It demonstrates zero-trust principles through group-based access, least-privilege secret policies, effective-access checks, access reviews, and session revocation during identity lifecycle changes. It remains a local lab with documented development defaults and privileged components, not an internet-hardened deployment.

### [RedDock](https://github.com/chriswayneh/RedDock)

A security assessment tool for authorized local environments. Its zero-trust controls include fail-closed target scope checks immediately before contact, fixed tool arguments, separate approvals for validation, and evidence-linked findings. The local operator boundary is not shared-user authentication or authorization for arbitrary targets.

### [local-mcp-toolbox](https://github.com/chriswayneh/local-mcp-toolbox)

A local, read-only MCP server with a completed v1.5 inspection scope. Version 1.5.2 covers approved files, Git and GitHub metadata, logs, container health, and static Python environment checks. Zero-trust controls include explicit allowlists, bounded output, central redaction, and sanitized audit records. No arbitrary command execution or mutation tools are exposed.

[v1.5.2 release](https://github.com/chriswayneh/local-mcp-toolbox/releases/tag/v1.5.2) | [Architecture and setup](https://github.com/chriswayneh/local-mcp-toolbox#readme) | [Verification results and limitations](https://github.com/chriswayneh/local-mcp-toolbox/blob/main/docs/release-1.5.md)

### [jobdorking](https://jobdorking.com)

A personal job-search tool for organizing targeted searches. Optional cloud workspace access uses server-verified session tokens and user-scoped database queries; signed-out work remains local. These are specific access and privacy controls, not a claim of a complete zero-trust architecture. Development is currently inactive. The site is available at [jobdorking.com](https://jobdorking.com).

## Contact

[LinkedIn](https://www.linkedin.com/in/chriswhickman/)
