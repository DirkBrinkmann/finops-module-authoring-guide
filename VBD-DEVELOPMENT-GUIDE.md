# Azure Cost Management & FinOps — VBD Development & Maintenance Guide

> **Audience:** Microsoft CSAs creating and updating modules for the Azure Cost Management & FinOps workshop series.
> This guide covers the end-to-end process from content intake to production publishing.
> For detailed slide-level authoring rules, refer to the [Module Authoring Guide](MODULE-AUTHORING-GUIDE.md).

### Version History

| Version | Date | Change |
|---------|------|--------|
| `1.20260227.1` | 27.02.2026 | Initial release |

---

## 1. Overview

The Azure Cost Management & FinOps workshop series is a modular, Value-Based Delivery (VBD) program. Workshops are composed of individually authored PowerPoint modules, each covering a single topic. Modules are assembled into scenarios tailored to specific audiences and customer needs.

This guide documents **how** modules move from idea to production — the governance, development, review, and publishing processes. It complements the [Module Authoring Guide](MODULE-AUTHORING-GUIDE.md), which defines **what** goes into each module.

### Who Can Author?

Anyone at Microsoft can be a Module Author. However, creation of new modules must be approved by the PPE TPM or VBD Lead before development begins.

---

## 2. Key Repositories & Sites

| Resource | Purpose | Link |
|----------|---------|------|
| **Development SharePoint** | Working copies of all modules under development | [Modules repository](https://microsoft.sharepoint.com/:f:/t/ASDIPDevelopment/IgBn2mwDbwSeQ57re7KGukjCAfyxsckLtsdejY04LbxP4YY?e=oeFITs) |
| **Release SharePoint** | Published modules ready for delivery | [Modules repository](https://microsoft.sharepoint.com/:f:/r/teams/ASDIPRelease/AzureCloudAI/SP1%20VBD/Cost%20%26%20FinOps/Modules%20repository?csf=1&web=1&e=eDbSKM) |
| **IP Publishing Tool** | Tool for publishing IP content to production | [aka.ms/ipcontentpublishing](https://aka.ms/ipcontentpublishing) |
| **VBD Authoring Repo** | This repository — authoring guide, templates, scripts, and data model documentation | Current repository |
| **VBD Delivery Repo** | Production-ready modules and scenario data for CSA consumption | [asd-management/azure-cost-finops](https://github.com/asd-management/azure-cost-finops) |
| **Module Repository Database** | Excel workbook tracking all modules, scenarios, audiences, and FinOps capabilities | [FinOpsCost-Module-Repository.xlsx](https://microsofteur-my.sharepoint.com/personal/dirkbri_microsoft_com/Documents/250-IP/FinOps/VBD/Modules/FinOpsCost-Module-Repository.xlsx?web=1) |
| **PPTX Template** | Official module template — all modules must start from this file | [Download template](https://microsoft.sharepoint.com/:p:/t/ASDIPDevelopment/IQBrpqvqH3ffRIAqsi7jQQz9AW71Dektsc1t2LuC0uxkYuU?e=zuKnrx) |

---

## 3. Content Sources

New modules, updates to existing modules, and new VBD scenarios originate from the following sources:

| Source | Description |
|--------|-------------|
| **Corp / Product Group (PG)** | Feature launches, product updates, and strategic priorities from Microsoft product teams |
| **Solution Areas via PPE** | Requests and priorities from the Proactive Portfolio Experience Team |
| **VBD Feedback** | Field feedback from CSAs and customers submitted via [https://aka.ms/vbdfeedback](https://aka.ms/vbdfeedback) |
| **IP Champs & VBD v-Team** | Content ideas and improvement suggestions from the IP Champions network and the VBD virtual team |

---

## 4. Content Creation Governance

All modules must follow the rules documented in the [Module Authoring Guide](MODULE-AUTHORING-GUIDE.md). Key governance principles:

| Principle | Detail |
|-----------|--------|
| **One topic per module** | Each module covers exactly one topic (see [Authoring Guide §4](MODULE-AUTHORING-GUIDE.md#4-module-scope-rules)) |
| **Template compliance** | All modules must be created from the [official PPTX template](https://microsoft.sharepoint.com/:p:/t/ASDIPDevelopment/IQBrpqvqH3ffRIAqsi7jQQz9AW71Dektsc1t2LuC0uxkYuU?e=zuKnrx) (see [Authoring Guide §5](MODULE-AUTHORING-GUIDE.md#5-template-and-slide-layouts)) |
| **Required slide structure** | Title → Changelog → Glossary → Content → Demos → Q&A → Thank You (see [Authoring Guide §6](MODULE-AUTHORING-GUIDE.md#6-required-slide-structure)) |
| **VBD design principles** | All content must be outcome-driven, interactive, and audience-specific (see [Authoring Guide §3](MODULE-AUTHORING-GUIDE.md#3-content-design-principles)) |
| **Change tracking** | Every modification requires slide-level date updates, a changelog entry, and module-level date update (see [Authoring Guide §14](MODULE-AUTHORING-GUIDE.md#14-change-tracking-workflow)) |
| **File naming** | `M-<NNN>-<Category>-<Topic>.pptx` (see [Authoring Guide §2](MODULE-AUTHORING-GUIDE.md#2-file-naming-convention)) |

---

## 5. Development Process

### 5.1 Process for New Modules

**Prerequisite:** Creation of a new module must be approved by the PPE TPM or VBD Lead.

```
┌──────────────────────────────────────────────────────────────────────┐
│ Step 1: Approval & Assignment                                        │
│   PPE TPM or VBD Lead approves the new module                        │
│   VBD Lead selects a Module Author and assigns a new Module ID       │
│                         │                                            │
│                         ▼                                            │
│ Step 2: Authoring                                                    │
│   Module Author creates the module following the                     │
│   Module Authoring Guide (see MODULE-AUTHORING-GUIDE.md)             │
│                         │                                            │
│                         ▼                                            │
│ Step 3: Upload to Development Site                                   │
│   Module Author copies the completed module to the                   │
│   Development SharePoint Modules repository                          │
│                         │                                            │
│                         ▼                                            │
│ Step 4: Peer Review                                                  │
│   New modules must be reviewed by at least TWO                       │
│   IP Champs or VBD v-Team members                                    │
│                         │                                            │
│                         ▼                                            │
│ Step 5: Notify VBD Lead                                              │
│   Module Author sends the VBD Lead the required information          │
│   (see Section 5.3 below)                                            │
└──────────────────────────────────────────────────────────────────────┘
```

### 5.2 Process for Updating Existing Modules

**Who:** Module Author

| Step | Action |
|------|--------|
| 1 | Validate the new or updated content and integrate it into the existing module stored on the [Development SharePoint](https://microsoft.sharepoint.com/:f:/t/ASDIPDevelopment/IgBn2mwDbwSeQ57re7KGukjCAfyxsckLtsdejY04LbxP4YY?e=oeFITs) |
| 2 | Validate spelling and grammar |
| 3 | Follow the change tracking workflow — update slide dates, changelog, and module date (see [Authoring Guide §14](MODULE-AUTHORING-GUIDE.md#14-change-tracking-workflow)) |
| 4 | Have the content reviewed by at least **one** IP Champ or VBD v-Team member |
| 5 | Inform the VBD Lead (DirkBri) about the update, including required changes to the module content & outcome description and whether the module type changes (`mandatory`, `recommended`, `optional`) |

### 5.3 Information Required When Notifying the VBD Lead

When a new or updated module is ready for publishing, the Module Author must provide the VBD Lead with:

#### 1. Module Content & Outcome Summary

Generate a concise summary of the module's content and outcomes. Use the following prompt with the completed module as input:

> *"You will receive a VBD Module (PowerPoint) from the worldwide CSU VBD series for Azure Cost Management & FinOps. Your task is to extract the essence of the module and produce two concise sections. You will find the Target audience for this text defined on the title slide. Your output must contain exactly these two sections:*
>
> *1. Content — Provide: One sentence describing what this module covers. 3–4 short, precise bullet points summarizing the key content elements. Write it so both Microsoft internal and customer stakeholders clearly understand the purpose of this module.*
>
> *2. Outcome — Provide: One sentence summarizing what the audience will learn or be able to do after completing this module. 3–4 short, precise bullet points describing the key takeaways, outcomes, or skills.*
>
> *Rules: Use VBD catalog language (very short, marketing-style). Be clear, concise, and business-focused. Focus only on the content that appears in the provided module. Avoid fluff or marketing language. Keep terminology aligned with Azure Cost Management & FinOps best practices. Use no special characters, no Markdown, just clean text."*

#### 2. Scenario Classification

Specify:
- **Which existing scenario(s)** the module applies to (e.g., `S-F-01`, `S-P-01`)
- **Module type** within each scenario: `mandatory`, `recommended`, or `optional`

> For background on the scenario and module data model, see the [Module Repository Data Documentation](scripts/Module-Repository-Data-Documentation.md).

---

## 6. Review Guidelines

| Module Type | Minimum Reviewers | Reviewer Pool |
|-------------|-------------------|---------------|
| **New module** | 2 | IP Champs, VBD v-Team members |
| **Updated module** | 1 | IP Champs, VBD v-Team members |

### What to Review

Reviewers should verify:

- [ ] Module follows the [Module Authoring Guide](MODULE-AUTHORING-GUIDE.md) conventions
- [ ] Content is accurate, up-to-date, and aligned with current Azure product documentation
- [ ] Educational flow progresses logically (introduce → explain → demonstrate → summarize)
- [ ] Interactive discussion prompts are included every 3–4 content slides
- [ ] Target audience and contract type are correctly set on the title slide
- [ ] Glossary of Acronyms (slide 3) includes all acronyms used in the module
- [ ] Demo entries (if present) are non-invasive and audience-appropriate
- [ ] Spelling and grammar are correct
- [ ] Change tracking is complete (slide dates, changelog, module date)

---

## 7. Publishing to Production

**Who:** VBD v-Team

After the Module Author completes the review process and notifies the VBD Lead, the VBD v-Team publishes the module to production.

```
┌──────────────────────────────────────────────────────────────────────┐
│ Step 1: Update Module Database                                       │
│   Update FinOpsCost-Module-Repository.xlsx with the latest module    │
│   metadata, adjusting content/outcome descriptions as needed         │
│                         │                                            │
│                         ▼                                            │
│ Step 2: Update Power BI                                              │
│   Refresh the Power BI dataset with the updated database content     │
│   Verify the data and publish to the Power BI Service                │
│                         │                                            │
│                         ▼                                            │
│ Step 3: Publish to Production SharePoint                             │
│   Copy updated modules from the Development SharePoint folder        │
│   to the Production SharePoint folder                                │
│                         │                                            │
│                         ▼                                            │
│ Step 4: Export Scenario Data                                         │
│   Run: python scripts/export_scenario_modules.py                     │
│   This regenerates scenario_modules.csv from the Module Repository   │
│                         │                                            │
│                         ▼                                            │
│ Step 5: Update Delivery Repository                                   │
│   Commit the updated module(s) and scenario_modules.csv to the       │
│   VBD Delivery Repo (asd-management/azure-cost-finops)               │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 8. Module Lifecycle

Modules progress through defined lifecycle stages. Only modules at stage `30` are considered production-ready.

| Stage | Name | Description |
|-------|------|-------------|
| `00` | Envisioned | Module concept has been identified but not yet approved |
| `10` | In Development | Module creation is in progress |
| `20` | In Review | Module is complete and undergoing peer review |
| `30` | Published & Maintained | Module is production-ready and actively maintained |
| `40` | Sunset, not maintained | Module is still available but no longer updated |
| `90` | Retired | Module has been removed from active use |

> The lifecycle stage is tracked in the [Module Repository Database](https://microsofteur-my.sharepoint.com/personal/dirkbri_microsoft_com/Documents/250-IP/FinOps/VBD/Modules/FinOpsCost-Module-Repository.xlsx?web=1) (`VBD Module.Module Lifecycle`).

---

## 9. Quick Reference — End-to-End Workflow

### New Module

| # | Who | Action |
|---|-----|--------|
| 1 | Module Author | Get approval from PPE TPM or VBD Lead |
| 2 | VBD Lead | Assign Module Author and Module ID |
| 3 | Module Author | Create module using [Module Authoring Guide](MODULE-AUTHORING-GUIDE.md) and [PPTX template](https://microsoft.sharepoint.com/:p:/t/ASDIPDevelopment/IQBrpqvqH3ffRIAqsi7jQQz9AW71Dektsc1t2LuC0uxkYuU?e=zuKnrx) |
| 4 | Module Author | Upload module to Development SharePoint |
| 5 | IP Champs / v-Team | Review module (minimum 2 reviewers for new modules) |
| 6 | Module Author | Address review feedback |
| 7 | Module Author | Send VBD Lead: content/outcome summary + scenario classification |
| 8 | VBD v-Team | Update Module Database, Power BI, Production SharePoint, and Delivery Repo |

### Updated Module

| # | Who | Action |
|---|-----|--------|
| 1 | Module Author | Update module on Development SharePoint |
| 2 | Module Author | Follow change tracking workflow ([Authoring Guide §14](MODULE-AUTHORING-GUIDE.md#14-change-tracking-workflow)) |
| 3 | Module Author | Validate spelling and grammar |
| 4 | IP Champs / v-Team | Review changes (minimum 1 reviewer for updates) |
| 5 | Module Author | Inform VBD Lead of update details |
| 6 | VBD v-Team | Update Module Database, Power BI, Production SharePoint, and Delivery Repo |

---

## 10. Related Documents

| Document | Location | Description |
|----------|----------|-------------|
| [Module Authoring Guide](MODULE-AUTHORING-GUIDE.md) | This repository | Detailed slide-level authoring rules, layouts, metadata, and conventions |
| [Module Repository Data Documentation](scripts/Module-Repository-Data-Documentation.md) | This repository | Data model documentation for the Module Repository Excel workbook |
| [PPTX Template](templates/M-xxx-Category-Topicwithincategory.pptx) | This repository | Official PowerPoint template for new modules |
| [VBD Feedback Form](https://aka.ms/vbdfeedback) | External | Field feedback submission form |
