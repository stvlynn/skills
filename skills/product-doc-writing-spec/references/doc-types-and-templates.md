# Document Architecture, Genre Guidelines, and Standard Templates

This reference preserves the complete rules, structural frameworks, writing requirements, and Markdown templates for each product documentation genre: overall documentation architecture (cloud/SaaS & on-premises), descriptive docs, procedural/operational guides, parameter references, troubleshooting guides, FAQs, glossaries, high-risk operation warnings, lifecycle stage guidelines, release notes, and API documentation.

---

## 1. Product Documentation Architecture Framework

### General Principles
1. **Provide complete documentation for all product capabilities.**
2. **Prioritize mandatory documents for urgent launches**, and complete optional documents immediately after release.
3. **Avoid orphan headings in the navigation tree**: if a category has only a single second-level node, promote that node to a first-level directory.

### 1.1 Standard Documentation Tree (Cloud / SaaS Products)

| No. | Level-1 Directory | Level-2 Directory | Core Content | Notes |
| - | - | - | - | - |
| 1 | **Release Notes & Announcements** | **Release Notes (Mandatory)** | Introduces feature launches, enhancements, or billing updates (including title, description, release date, and related doc links). | Exclude changes invisible to users, pure typo/image edits, or internal-only changes. |
| 1 | Release Notes & Announcements | **Announcements** | Lists links to official announcements regarding major feature, lifecycle, or pricing changes. | — |
| 2 | **Beginner's Guide** | — | Curated learning path for new users: 1. Product definition; 2. Billing model; 3. Getting started steps; 4. Console overview; 5. Feature list; 6. Beginner FAQs; 7. Feedback. | Organize as a progressive learning path rather than a raw link dump. |
| 3 | **Product Introduction (Mandatory)** | **Overview (Mandatory)** | 1. Product definition (Mandatory)<br/>2. Main features (Mandatory)<br/>3. Architecture or working principles<br/>4. Related products | Avoid overly broad/narrow definitions; do not make absolute guarantees of effectiveness; clearly distinguish free vs. paid features. |
| 3 | Product Introduction (Mandatory) | **Strengths / Benefits (Mandatory)** | Explains technical and business advantages in the industry. | Do not exaggerate claims, disparage competitors, or make absolute guarantees; ensure diagrams match the text. |
| 3 | Product Introduction (Mandatory) | **Use Cases (Mandatory)** | Describes typical scenarios, problems solved, and business value delivered. | Ensure scenarios are complete and realistic. |
| 4 | **Purchase Guide (Mandatory)** | **Billing Overview (Mandatory)** | Explains pricing models, billable items, and pricing examples (link to price calculator if available). | — |
| 4 | Purchase Guide (Mandatory) | **Purchase Methods (Mandatory)** | Step-by-step purchase instructions (or application/contact channels for beta/private deployments). | — |
| 4 | Purchase Guide (Mandatory) | **Renewal (Mandatory)** | Renewal rules and operating instructions (omit for free products). | — |
| 4 | Purchase Guide (Mandatory) | **Overdue Payment / Arrears (Mandatory)** | Resource status, grace periods, and data retention rules when an account falls into arrears. | — |
| 4 | Purchase Guide (Mandatory) | **Refund / Unsubscription (Mandatory)** | Refund rules, calculation formulas, and unsubscription steps. | — |
| 5 | **Quick Start (Mandatory)** | — | End-to-end tutorial guiding new users through service creation and basic configuration. | Organize by scenario or core workflow. Provide an *Access Guide* for beta/private products. |
| 6 | **Operation Guide (Mandatory)** | — | Task-oriented instructions for all product features (may be titled *Console Guide* if strictly UI-based; omit for API-only products). | — |
| 7 | **Tool Guide** | — | Installation, configuration, and usage instructions for companion CLI/GUI tools. | — |
| 8 | **Best Practices / Tutorials** | — | Practical end-to-end guides for typical real-world architectures and scenarios. | — |
| 9 | **O&M Guide** | — | Routine maintenance operations such as health checks, monitoring, and capacity expansion. | — |
| 10 | **Troubleshooting** | — | How to collect diagnostic information and resolve common faults. | — |
| 11 | **Developer Guide** | — | Application development workflows, conventions, and sample projects. | — |
| 12 | **API Documentation (Mandatory if APIs exist)** | Release History / Introduction / API Overview / Calling Guide / Action References / Error Codes / Data Types / Appendix | Complete API reference covering endpoints, authentication, request/response parameters, examples, error codes, and data structures. | Omit if the product exposes no external APIs. |
| 13 | **SDK Documentation** | — | SDK acquisition, environment setup, initialization, and code examples across supported languages. | — |
| 14 | **Videos** | — | Video tutorials covering fundamentals and hands-on operations. | — |
| 15 | **FAQs (Mandatory)** | — | Answers to frequently asked questions (**at least 5 questions**; group by feature, scenario, or edition when numerous). | — |
| 16 | **Agreements & Certifications** | **SLA (Mandatory)** / Terms of Service / Privacy Statement / Compliance Certifications | Service Level Agreement, user terms, privacy policy, and security compliance certifications. | — |
| 17 | **General Reference** | Benchmark Data / Command Reference | Performance/functional benchmark reports and CLI command syntax/options/examples. | — |
| 18 | **Contact Us (Mandatory)** | — | Pre-sales, after-sales, community, and technical support channels. | — |
| 19 | **Glossary (Mandatory)** | — | Definitions of all domain and product-specific terminology. | — |

### 1.2 On-Premises / Private Deployment Documentation Package Framework

| No. | Document Name | Mandatory | Core Sections (* = Mandatory) | Key Information & Splitting Notes |
| - | - | - | - | - |
| 1 | **Product Presentation (PPT)** | No | Overview*, Industry Trends & Pain Points, Strengths*, Architecture*, Features*, Case Studies*, Demo, Delivery Model | Use diagrams for functional, technical, and security architectures. |
| 2 | **Product Whitepaper** | **Yes** | Overview*, Architecture*, Feature List*, Case Studies | Feature list may be split into a standalone document if extensive. |
| 3 | **Glossary** | No | Terms, definitions, and abbreviations | Can be a standalone manual or an appendix in individual guides. |
| 4 | **Technical Architecture Design** | **Yes** | Technical Strengths*, Technical Metrics*, High-Level Design*, Detailed Design*, Database Design* | High-level design covers overall framework, component relationships, logical/data/technical/security architecture; detailed design covers component internals and inter-module flows. |
| 5 | **Disaster Recovery & High Availability** | No | Overview, DR Capabilities by Tier* | Core metrics (RPO, RTO) and component/host/data-center/cross-region DR schemes. |
| 6 | **Security Capabilities** | No | Security Design*, Reliability Design, DR Design | — |
| 7 | **Release Notes** | **Yes** | Version Compatibility*, Naming Rules, Compatibility Notes, New Features*, Changes*, Bug Fixes | Version number, release date, and detailed change descriptions. |
| 8 | **Deployment Planning Guide** | No | Overall Plan, Deployment Topology*, Hardware/Software Plan*, Resource Design*, Staffing Requirements | May be merged into the *Deployment Guide* if simple. |
| 9 | **Hardware & Software Requirements** | No | Hardware Requirements*, Software Dependencies*, Pre-Check Items & Pass Criteria* | May be merged into the *Deployment Guide* if brief. |
| 10 | **Deployment Guide** | **Yes** | Topology Overview, Workflow, Deployment Plan*, HW/SW Requirements*, Step-by-Step Deployment*, Verification & Rollback* | Deployment steps must cover purpose, prerequisites, steps, expected output, verification, and rollback. |
| 11 | **Acceptance Test Cases (Functional / Performance / HA)** | **Yes** | Severity Definitions, Test Workflow, Case List*, Case Details* | Each case includes: Name, ID, Priority, Purpose, Duration, Prerequisites, Steps, Expected Result, Actual Result. |
| 12 | **Acceptance Test Report** | **Yes** | Process Summary, Test Conclusion Summary*, Customer Sign-off* | Summary of executed test cases and results. |
| 13 | **Operations Management Guide** | No | Resource provisioning, accounts, permissions, quotas, metering, and billing for platform operators | — |
| 14 | **User Guide** | **Yes** | Product Introduction*, Quick Start*, Operations*, Best Practices*, FAQs*, Agreements | Operations must include scenario, prerequisites, risk warnings (especially for delete/uninstall/shutdown/reboot), steps, and verification. |
| 15 | **Developer Guide (SDK Reference)** | No | Environment Setup*, Development Workflow, Conventions & Samples* | — |
| 16 | **API Reference** | **Yes** | API Overview, Endpoint Description*, Request Parameters*, Response Parameters*, Examples*, Error Codes* | Include both request and response examples. |
| 17 | **O&M Guide** | **Yes** | O&M Overview, Product Architecture*, Deployment Architecture*, Dependencies*, Fault Blast Radius*, Preparation*, Health Checks*, Log Management*, Backup*, DR*, High-Risk Operations*, Monitoring Metrics*, Alerts*, Troubleshooting*, Emergency Response Plan*, Common Operations | High-risk operations cover: Name, Risk, Severity, Mitigation, Observation Items. Troubleshooting/Emergency plans cover: Symptom, Blast Radius, Root Causes, Estimated Recovery Time, Diagnostic/Emergency Flow, Prerequisites, Steps, Recovery Verification. |

---

## 2. Descriptive Documentation Standards

### Purpose
Descriptive documents introduce product definitions, features, architecture, and working principles (e.g., *Product Overview*).

### Writing Requirements
- **Headings**: Use concise **noun phrases**; no `&`, `/`, or hyphens for supplementary notes; no super/subscripts.
- **Six-Step Writing Structure**:
  1. **What it is (Mandatory)**: Define the concept clearly using an **"A is B"** sentence pattern.
  2. **What it does (Mandatory)**: Summarize its core purpose first, then list specific capabilities as bullet points.
  3. **How it is structured (Optional)**: Describe its component modules, what each module does, and how they interact (use an architecture diagram first, followed by text).
  4. **Specifications (Optional)**: List available editions/tiers, specification parameters, and target scenarios.
  5. **Limitations (Optional)**: State quotas, regional availability, or technical constraints.
  6. **Related components (Optional)**: Explain how it integrates with upstream or downstream services.

---

## 3. Procedural / Operational Documentation Standards & Template

### Purpose
Procedural documents guide users step-by-step to complete a specific task (e.g., *Operation Guide*, *O&M Guide*, *Installation Guide*).

### Required Sections
1. **Title (Mandatory)**: Use a **"Verb + Object"** structure based on the user's task (e.g., `Connect to a Database`).
2. **Operation Scenario (Mandatory)**: Frame the scenario using the **5W2H1E** model (`How much` and `Effect` are optional; the rest are mandatory):
   - **What**: Purpose and task content.
   - **Who**: Target operator/role.
   - **Where**: Environment or platform where the task takes place.
   - **When**: Timing or lifecycle trigger.
   - **Why**: Business or technical goal achieved after completion.
   - **How**: Method or tool used.
   - **How much (Optional)**: Quantity, scale, or range.
   - **Effect (Optional)**: Resulting state or impact.
3. **System Impact (Optional)**: Exhaustively list any potential impact on running workloads (e.g., service interruption, read-only lock, network reset) so users can assess risk beforehand. Omit this section if there is no impact.
4. **Prerequisites (Optional)**: List all conditions that must be met before starting (e.g., account registration, permissions, network ports opened).
5. **Procedure (Mandatory)**: Step-by-step verifiable instructions:
   - State clearly who performs the action and where.
   - Separate action commands from lengthy explanations and outputs.
   - Place tool download links at the exact step where needed.
   - Place supplementary notes at the end of a step or procedure (using callout blocks), not mid-step.
   - Conclude with a **verification step** to confirm success.
6. **Related Operations (Optional)**: Links to follow-up or alternative tasks, ordered chronologically if sequential.
7. **Appendix (Optional)**: Supplementary reference tables or syntax notes.

### Standard Template: Procedural Document

```markdown
## Operation Scenario
This task guides you (Who) to log in to a Linux virtual server (What) from a local workstation (Where) using a remote SSH client (How) after provisioning and starting the server (When), so that you can deploy applications on the server (Why).

## System Impact
State all potential impacts on the system (for example, service restart or brief network interruption). Omit this section if there is no impact.

## Prerequisites
- You have provisioned and started a Linux server instance.
- The server instance has a public IP address assigned.
- You have obtained the administrator username and password.

## Procedure
1. Download and install an SSH client on your local workstation.
2. Launch the SSH client and configure the following parameters in the **Session Configuration** window:
   - **Host Name**: Enter the public IP address of the server. You can view the public IP address on the instance list page of the [Management Console](https://example.com/console).
   - **Port**: Enter `22`. Ensure inbound port `22` is allowed; for details, see [Security Group Configuration](https://example.com/docs/security-group).
   - **Connection type**: Select **SSH**.
3. Click **Open** to start a new session.
4. In the terminal window, enter the administrator username obtained in the prerequisites and press Enter, then enter the password and press Enter. When the shell prompt appears, you have successfully logged in.

> **Caution:**
> If the connection fails, verify that your instance allows inbound traffic on port `22` in both the [Security Group](https://example.com/docs/security-group) and [Network ACL](https://example.com/docs/network-acl).

## Related Operations
- [Log In Using WebShell](https://example.com/docs/webshell)
- [Log In Using an SSH Key Pair](https://example.com/docs/ssh-key)

## Appendix
| Operating System Family | Default Administrator Username |
| - | - |
| Enterprise Linux Series | `root` |
| Standard Linux Series | `admin` |
```

---

## 4. Parameter Reference Standards & Template

### Writing Requirements
- **Headings**: Use **noun phrases** (e.g., `Specification Parameters`), no `&` or `/`.
- **Standard Parameter Table Columns**:
  - **Name**: Parameter identifier (e.g., `Region`).
  - **Meaning / Description**: Concise definition of the parameter.
  - **Type**: Data type (e.g., `String`, `Integer`, `Boolean`).
  - **Required**: `Yes` or `No`.
  - **Valid Values**: Allowed range or enumerated values, including the default value if applicable.
  - **Notes**: Constraints, dependencies on other parameters, or applicable scenarios; fill with `-` if none.

### Standard Template: Parameter Reference

```markdown
## Parameter Description

| **Name** | **Meaning** | **Type** | **Required** | **Valid Values** | **Notes** |
| - | - | - | - | - | - |
| Region | Deployment region ID | String | Yes | `us-east-1`, `eu-central-1` | - |
| MaxConnections | Maximum concurrent connections | Integer | No | `100` - `10000` (Default: `1000`) | Takes effect after service restart. |
```

---

## 5. Troubleshooting Documentation Standards & Template

### Required Sections & Rules
1. **Title**:
   - **Rule 1**: The title must state the **fault symptom** directly (e.g., `Unable to Log In to Server`).
   - **Rule 2**: Omit redundant words like "Troubleshooting" when the context is already clear:
     - **Correct**: `High CPU Usage (Windows)`
     - **Incorrect**: `High CPU Usage Troubleshooting (Windows)`
2. **Symptom Description**: Describe the background and exact symptoms (error codes, log messages, UI prompts) using **3W (What / Where / When)**.
3. **Possible Causes**: List all known causes, grouped by category if multiple causes belong to the same type.
4. **Resolution Approach**: Summarize the overall diagnostic and recovery logic concisely (use a flowchart if the branching logic is complex).
5. **Troubleshooting Steps**: Step-by-step commands and actions with expected outputs and a final verification step.

### Standard Template: Troubleshooting Guide

````markdown
## Symptom Description
After restarting a Linux server or executing `service network restart`, the server cannot resolve domain names, and the DNS configuration in `/etc/resolv.conf` is cleared.

## Possible Causes
In this OS release, `initscripts` versions earlier than `9.03.49-1` contain a compatibility defect with certain `grep` versions that clears `/etc/resolv.conf` during network restarts.

## Resolution Approach
Upgrade `initscripts` to the latest version and regenerate the DNS configuration.

## Troubleshooting Steps
1. Log in to the server and run the following command to check the installed `initscripts` version:
   ```bash
   $ rpm -q initscripts
   initscripts-9.03.40-2.el6.x86_64
   ```
   As shown above, version `9.03.40-2` is earlier than `9.03.49-1` and is affected by this issue.

2. Run the following commands to upgrade `initscripts` and restart the network service:
   ```bash
   cat /dev/null > /etc/resolv.conf
   service network restart
   yum makecache
   yum -y update initscripts
   ```

3. After the upgrade completes, run the following command to verify the new version:
   ```bash
   $ rpm -q initscripts
   initscripts-9.03.58-1.el6.x86_64
   ```
   If the output shows a version later than `9.03.49-1`, the upgrade succeeded.
````

---

## 6. FAQ Standards

### Rules & Recommendations
- **Rule 1**: Questions must be specific, clear, and concise.
- **Rule 2**: Phrase every question as an **interrogative sentence ending with a question mark (`?`)**.
- **Rule 3**: Answers must directly address the question without evading the core issue.
- **Rule 4**: A product FAQ document must contain **at least 5 questions** (`≥ 5`).
- **Rule 5**: Group questions along a consistent dimension (by feature, scenario, or billing/edition) with parallel phrasing.
- **Recommendation 1**: Keep each FAQ category to **9 items or fewer** (`≤ 9`).
- **Recommendation 2**: For complex troubleshooting questions, provide a brief answer and link to the dedicated troubleshooting guide using `see [Title](url)`.
- **Recommendation 3**: Address one question per Q&A entry and place related questions adjacent to each other.
- **Formatting Style**:
  - **Question**: H3 heading (`### Question?`).
  - **Answer**: Standard body paragraphs/lists below the H3 heading.

---

## 7. Glossary Standards & Template

### Rules & Recommendations
- **Rule 1**: Definitions must be grammatically sound and follow industry standards.
- **Rule 2**: Only include necessary domain concepts, product-specific concepts, and core technical terms.
- **Rule 3**: **Do not define everyday words used in their ordinary sense.**
- **Rule 4**: Define everyday words when they carry a specialized meaning in the product's domain, as well as unfamiliar technical terms.
- **Rule 5**: Maintain a strict **one-to-one mapping** between a concept and its term within the same product or manual (never use multiple synonyms interchangeably for the same concept).
- **Recommendations**:
  - Define parent/sub-concepts in logical order (define concrete sub-components before the overarching system if it aids comprehension).
  - Do not use circular definitions (do not repeat the term itself or its inflected variants inside its definition).
  - Order glossary entries alphabetically or by logical conceptual hierarchy.

### Standard Template: Glossary

| Term (Local Language) | Definition | English Term | Abbreviation |
| - | - | - | - |
| Virtual Server | A scalable virtual computing environment hosted on cloud infrastructure. | Virtual Machine | VM |

---

## 8. High-Risk Operation Warning Standards

### Requirements
When an operation carries a risk of service interruption, unrecoverable data loss, or security exposure, include a prominent risk callout:
- **Rule 1 (Style)**: Use a **callout block** matching the severity level (**Caution**, **Warning**, or **Danger**).
- **Rule 2 (Placement)**: Place the callout at the **most relevant and timely location** — either at the very top of the page or immediately before the high-risk step.
- **Rule 3 (Three Required Elements)**:
  1. **Explicit Trigger Action**: State the exact operation that triggers the risk (e.g., *"When you terminate an instance or format a disk..."*).
  2. **Explicit Consequence**: Highlight the core impact using clear, unmistakable terms such as **"permanently deleted"**, **"irreversible"**, **"cannot be recovered"**, **"data loss"**, **"service interruption"**, or **"data exposure"**.
  3. **Actionable Mitigation**: Provide clear preventive instructions (e.g., *"Before performing this operation, back up your data and confirm that no active workloads depend on this resource."*).

### High-Risk Warning Examples

| Risk Scenario | High-Risk Operation | Standard Warning Copy Example |
| - | - | - |
| **Data Loss** | Terminate/release instance, reset OS disk, delete storage bucket/object | **Deleting an object permanently removes the specified file. This operation is irreversible and deleted data cannot be recovered by any means, which may disrupt your business operations. Back up your data before proceeding.** |
| **Service Interruption** | Force stop/reboot instance, switch virtual network, unbind public IP, delete route table/security group rule | **Switching the virtual network immediately disconnects existing network sessions and makes your service unreachable. Perform this operation during off-peak hours after confirming the business impact.** |
| **Security Exposure** | Open `0.0.0.0/0` inbound security group rules, set storage bucket to public read/write, enable public database access | **Enabling public network access on a database instance introduces high security risks and may expose stored data to unauthorized access, tampering, or brute-force attacks. Follow the principle of least privilege and configure IP allowlists or firewall rules.** |

---

## 9. Feature Lifecycle Stage Guidelines

| Lifecycle Stage | Scenario | Documentation Requirement |
| - | - | - |
| **Planning** | Unreleased feature in planning | Do **not** document unreleased features in public docs to prevent information leaks (official pre-announcements excepted). |
| **Canary / Beta Release** | Net-new feature in canary/beta | Publish as a standalone page. Add a callout at the top of the page stating that the feature is in canary/beta testing and listing beta constraints. Once fully released (GA), update the doc and remove outdated beta docs. |
| **Canary / Beta Release** | Existing feature change in canary/beta | Document in the existing page with before/after sections clearly separated. Add an opening callout explaining how to identify whether an account/region is in the canary scope, pricing differences, and before/after operating steps. |
| **Canary / Beta Release** | Full product/console generation upgrade | Publish the new version as a separate directory branch. Add a dedicated section explaining the beta status, precautions, and how to switch between the old and new versions. |
| **GA (Allowlist-Controlled)** | Feature gated by allowlist / application | Add an opening callout stating that the feature requires application approval, how to apply, and the expected approval turnaround time. |
| **Deprecation / End of Sale** | Feature or tier retiring soon | Mark the feature/specification with **"Retiring Soon"** or **"End of Sale"**, state whether existing instances are affected, and provide migration steps or alternative solutions. |
| **Retired / End of Life** | Feature completely retired | Remove retired features from active documentation to prevent user confusion (official retirement notices excepted). |

---

## 10. Release Notes Standards & Template

### Rules
- **Rule 1**: Present release notes in a 4-column table grouped by month (`### YYYY-MM`):
  - **Update Title**: Concise and focused.
  - **Description**: Clear summary of what changed and the value to users (avoid exaggerated promises).
  - **Release Date**: Format as **`YYYY-MM-DD`**.
  - **Related Docs**: Direct links to help documentation (if 2 or more links are needed, format them as a bulleted list inside the cell).
- **Rule 2**: Keep column width proportions consistent across monthly tables.
- **Rule 3**: Never include unreleased future features in release notes.

### Standard Template: Release Notes

```markdown
### 2026-03

| **Update Title** | **Description** | **Release Date** | **Related Docs** |
| - | - | - | - |
| Smart Recommendations | Recommends relevant items on the home and list pages based on user behavior and preferences. | 2026-03-16 | [Smart Recommendations Guide](https://example.com/docs/recommendations) |
| Multi-Language UI Support | Adds English and Japanese UI language options for international teams. | 2026-03-10 | [Language Settings](https://example.com/docs/language) |
```

---

## 11. API Documentation Checklist & Templates

### 11.1 API Documentation Quality Checklist

| Section | Inspection Focus |
| - | - |
| **Overall** | Includes API endpoint domain, HTTP request methods (`POST`, `GET`), authentication/signature method, error codes, action summary table, and individual action pages. |
| **Action Description** | Complete, clear sentences explaining what the endpoint does and any usage constraints. |
| **Request Parameters** | Complete descriptions, accurate required/optional flags, exhaustive enum values, default values, acquisition methods, valid ranges, and type consistency between the table and request examples. Sample code must be executable. |
| **Response Parameters** | Complete descriptions, type consistency, and exact match between actual API responses and documented examples. |
| **Error Codes** | Complete list of error codes with clear descriptions and actionable resolution measures. |
| **Data Structures** | Clear description of nested structs/classes, referencing endpoints, and field definitions. |

### 11.2 Template: API Overview
```markdown
This document summarizes all available API actions for the service.

## Region Actions

| Action | Description |
| - | - |
| [DescribeRegions](/document/api/service/DescribeRegions) | Queries the list of supported regions. |
| [DescribeZones](/document/api/service/DescribeZones) | Queries the list of availability zones in a region. |
```

### 11.3 Template: Error Codes
````markdown
## Overview
If the API response contains an `Error` object, the API call failed. Example error response:

```json
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "The provided credentials could not be validated. Please check your signature is correct."
        },
        "RequestId": "ed93f3cb-f35e-473f-b9f3-0d451b8b79c6"
    }
}
```
The `Code` field inside `Error` indicates the specific error code.

## Error Code List

| Error Code | Description | Resolution |
| - | - | - |
| `AuthFailure.SignatureFailure` | Signature verification failed. | Check the returned error message and verify that your secret key and signature algorithm match the specification. |
````

### 11.4 Template: Data Structures
```markdown
## EnhancedService

- **Description**: Configuration of enhanced instance services such as security and monitoring agents.
- **Referenced by**: [RunInstances](https://example.com/docs/RunInstances), [ResetInstance](https://example.com/docs/ResetInstance).

| Field | Type | Required | Description |
| - | - | - | - |
| SecurityService | [RunSecurityServiceEnabled](#RunSecurityServiceEnabled) | No | Enables the security agent. Enabled by default if omitted. |
| MonitorService | [RunMonitorServiceEnabled](#RunMonitorServiceEnabled) | No | Enables the monitoring agent. Enabled by default if omitted. |
```

### 11.5 Template: API Release History
```markdown
> **Caution:**
> This document records updates for API v3.0 only. For earlier API versions, see [Legacy API Release History](https://example.com/docs/legacy-history).

Current API Version: v3.0.

| Release Date | Update Description | Version |
| - | - | - |
| 2026-03-02 | Fourth release:<br><ul><li>Removed the `StoppedMode` request parameter from [StopInstances](https://example.com/docs/StopInstances).</li></ul> | v3.0 |
| 2026-02-12 | Initial release:<br><ul><li>Released API v3.0.</li></ul> | v3.0 |
```
