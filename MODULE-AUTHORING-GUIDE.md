# Azure Cost Management & FinOps — Module Authoring Guide

| | |
|---|---|
| **Version** | `1.20260214.3` |
| **Last updated** | `14.02.2026` |
| **Author** | DirkBri |

> **Audience:** CSA module authors and AI tools that create, modify, or update workshop modules.
> This guide is the single source of truth for all module authoring rules, conventions, and processes.

### Version History

| Version | Date | Change |
|---------|------|--------|
| `1.20260214.3` | 14.02.2026 | Removed customer-specific sections (3.7, 3.8); added document versioning |
| `1.20260214.2` | 14.02.2026 | Added VBD content design principles (Section 3), enhanced content/demo/publishing sections |
| `1.20260214.1` | 14.02.2026 | Initial release |

---

## 1. Purpose

Every module in the Azure Cost Management & FinOps workshop series is a self-contained PowerPoint deck that teaches **one** topic. Modules are delivered by CSAs to customers in interactive sessions. This guide defines how to create, structure, and maintain these modules so that every deck is consistent, trackable, and ready for delivery.

---

## 2. File Naming Convention

Every module file **must** follow this exact pattern:

```
M-<NNN>-<Category>-<Topic>.pptx
```

| Segment      | Rule |
|--------------|------|
| `M-`         | Fixed prefix. Always uppercase `M` followed by a hyphen. |
| `<NNN>`      | Three-digit, zero-padded module number (e.g., `001`, `042`, `061`). Assign the next unused number in the series. |
| `<Category>` | One of the defined categories (see below). PascalCase, no spaces. |
| `<Topic>`    | Specific topic within the category. PascalCase, no spaces, no hyphens within the topic name. Use concatenated words (e.g., `FinOpsFrameworkIntroduction`, `InvoiceManagement`). |

### Valid Categories

| Category | Description |
|----------|-------------|
| `FinOps` | FinOps framework, methodology, personas, KPIs, benchmarking, implementation |
| `AzureBilling` | Invoices, EA/MCA billing, pricing, marketplace, subscriptions |
| `AzureCostManagement` or `AzureCostMgmt` | Scopes, roles, budgets, alerts, tagging, cost allocation, reporting |
| `AzureCostOptimization` | Reservations, savings plans, hybrid benefits, waste reduction, workload-specific optimization |

### Examples

```
M-001-FinOps-FinOpsFrameworkIntroduction.pptx
M-004-AzureBilling-EA.pptx
M-016-AzureCostMgmt-BudgetsAndAlerts.pptx
M-019-AzureCostOptimization-Workload-AKS.pptx
```

> **Note for AI tools:** When generating a new file name, query the existing module list to determine the next available module number. Do not reuse or skip numbers without reason.

---

## 3. Content Design Principles

These modules are delivered as **Value-Based Delivery (VBD)** engagements — interactive, customer-centric sessions that produce tangible outcomes. Every slide, demo, and discussion must be designed with these principles in mind.

### 3.1 Clear Purpose & Outcomes

Every module must have **one explicit purpose** stated on the title slide subtitle. Before authoring, answer:

- **Why does this module exist?** — What problem or knowledge gap does it address?
- **What will the customer be able to do after?** — Define 2–4 measurable outcomes (decisions made, actions enabled, capabilities understood).
- **What changes?** — Every section must answer "so what?" and "what changes after this?"

> **Rule:** If you cannot articulate the module's purpose in one sentence, the scope is too broad — split it.

### 3.2 Target Audience & Personas

Modules must be designed for a **specific audience**, not a generic one.

| Field | Guidance |
|-------|----------|
| **Primary audience** | Set on the title slide (FinOps, Product, or agnostic). This determines depth, terminology, and examples. |
| **Relevant personas** | Identify which roles benefit: FinOps Practitioner, Finance, Engineering, Procurement, Leadership, Product. |
| **Level alignment** | Do not mix executive overview with deep technical content. If both are needed, create separate modules. |

> **Rule:** When writing content, constantly ask: "Would my target persona understand this without additional context?" If not, add context or reconsider the audience scope.

### 3.3 Scoped Module Boundaries

Every module should clearly communicate what is and is not covered.

| Element | Where to Document | Example |
|---------|-------------------|---------|
| **In scope** | Slide notes on title slide or first content slide | "This module covers EA Prepayment mechanics, tracking, and alerts." |
| **Out of scope** | Slide notes | "MCA-specific billing is covered in M-014." |
| **Assumptions** | Slide notes on title slide | "Assumes the customer has an active EA enrollment." |
| **Prerequisites** | Slide notes or early content slide | "Familiarity with Azure billing hierarchy (see M-003)." |
| **Dependencies** | Slide notes | "Builds on concepts from M-001 (FinOps Framework Introduction)." |

> **Note for AI tools:** When creating a module, analyze the existing module catalog to identify and document cross-references, prerequisites, and dependencies.

### 3.4 Logical Flow & Right-Sized Content

Structure content as a **progressive learning journey**, not a reference document.

| Principle | Guidance |
|-----------|----------|
| **Progressive disclosure** | Start with "why it matters," then "how it works," then "what to do about it." Never lead with configuration details. |
| **Section dividers** | Use Divider layouts to separate major topics. Each section should build on the previous one. |
| **Right-sized slides** | One idea per slide. If a slide requires more than 60 seconds to present, split it. |
| **Realistic pacing** | A typical VBD module runs 45–90 minutes including discussion. Plan for ~2 minutes per content slide plus discussion time. A 20-slide content section ≈ 60–75 minutes delivered. |
| **Discussion checkpoints** | Plan natural pause points after every section (3–5 content slides) where the presenter can engage the customer. Note these in slide notes. |

### 3.5 Outcome-Driven Content

Every slide must earn its place. Apply the **"so what?" test**:

- **Before adding a slide, ask:** "What decision, action, or understanding does this enable?"
- **If a slide is purely informational** with no actionable implication, consider removing it or merging it with an adjacent slide.
- **End each section** with a takeaway or decision point, not just a summary of facts.

### 3.6 Interactive, Not Lecture

VBD sessions are **collaborative workshops**, not presentations. Design for dialogue.

| Technique | How to Implement |
|-----------|-----------------|
| **Guided discussion prompts** | Add discussion questions in slide notes: "Ask the customer: How do you currently track credit expiration?" |
| **Customer artifacts** | Design slides that the presenter can populate live with customer-specific data (org structure, tagging strategy, current spend). |
| **Whiteboard moments** | Mark slides where the presenter should pause for collaborative diagramming. Note in slide notes: "Whiteboard: Map customer's billing hierarchy." |
| **Decision captures** | Include slides or sections where customer decisions are recorded during the session. |

> **Rule:** For every 3–4 content slides, include at least one interaction point (discussion, exercise, or customer-specific exploration). Document these in slide notes.

### 3.7 Consistency & Reusability

All modules must be interchangeable parts of a modular workshop system.

| Element | Standard |
|---------|----------|
| **File naming** | `M-<NNN>-<Category>-<Topic>.pptx` (see Section 2) |
| **Slide structure** | Title → Changelog → Content → Demos → Q&A → Thank You (see Section 6) |
| **Changelog** | Every change tracked with date, slides, type, description, author (see Section 8) |
| **Date tracking** | Slide-level and module-level dates maintained (see Sections 11–12) |
| **Template compliance** | Only template layouts, no custom masters or themes (see Section 5) |
| **Terminology** | Use Azure product names exactly as they appear in official Microsoft documentation |

### 3.8 Follow-Up & Traceability

A VBD module is not complete at session end. Design for **handover and follow-up**.

| Element | Guidance |
|---------|----------|
| **Documented outputs** | Slide notes on the "Key Takeaways" slide should prompt the presenter to record all decisions and actions from the session. |
| **Recommendations mapped to outcomes** | Each recommendation should trace back to a specific module learning objective. |
| **Handover-ready** | After delivery, the deck (with completed notes) should serve as a standalone record of what was discussed, decided, and committed to. |
| **Resource links** | Include relevant Microsoft Learn URLs and FinOps Foundation references on the final content slide. |

---

## 4. Module Scope Rules

| Rule | Detail |
|------|--------|
| **One topic per module** | A module covers exactly one topic. Do **not** combine unrelated subjects. Example: Do not create a module describing the optimization of Azure Storage AND Networking — these must be separate modules. |
| **Holistic coverage** | Cover the chosen topic as completely as possible. Include context, concepts, configuration, best practices, and common pitfalls. |
| **Educational flow** | Structure slides in a logical learning sequence: introduce the concept → explain the details → show practical application → summarize. The audience should build understanding progressively (see Section 3.4). |
| **Audience awareness** | Every module targets a primary audience. Tailor depth, terminology, and examples accordingly (see Section 7 for audience field). |
| **In-scope / out-of-scope** | Explicitly document what the module covers and what it does not. Reference related modules for out-of-scope topics (see Section 3.3). |
| **Assumptions & prerequisites** | State what prior knowledge or environment setup is expected. Reference prerequisite modules by ID (see Section 3.3). |

---

## 5. Template and Slide Layouts

### Template Source

All modules **must** be created from the official template stored on the development SharePoint folder. The template file is named `M-xxx-Category-Topicwithincategory.pptx`. Do not create modules from scratch or from other PowerPoint files.

### Presentation Format

- **Aspect ratio:** 16:9 widescreen (13.33″ × 7.50″)
- **Slide numbering:** Enabled via footer placeholders

### Available Slide Layouts

Modules may **only** use the following layouts defined in the template. Do not create custom layouts.

| # | Layout Name | Use Case |
|---|-------------|----------|
| 0 | `1_Title square photo` | **Title slide** (slide 1 only). Contains module title, subtitle/metadata, and bottom-bar metadata shapes. |
| 1 | `Agenda Layout` | **Demo slide** (slide 3). Blue left bar with title area and large text body. Used for "Suggested live demos." |
| 2 | `Title Only` | General-purpose content slide with a title and free-form area below. Good for diagrams, screenshots, or custom layouts. |
| 3 | `1_Title Only_Blue Bar Layout` | Content slide with a blue accent bar. Use for emphasis or section-key slides. |
| 4 | `Title_Blue Bar_Placeholder layout` | Title + blue bar + one content placeholder. Suitable for single-concept slides with text or an image. |
| 5 | `Title Only_Subtitle_Blank` | Title + subtitle + blank area. Use when a subtitle adds context and the body is free-form. |
| 6 | `Title Only_Subtitle_Blue Bar Layout` | Title + subtitle + blue accent bar. Combines subtitle context with visual emphasis. |
| 7 | `Image Layout` | Title + large image/content placeholder. Use for full-slide screenshots or diagrams. |
| 8 | `Half Image_Blue Bar Layout` | Title + half-width image + blue bar. Use for side-by-side image and text compositions. |
| 9 | `Blue Bar Layout` | Title + blue accent bar, no placeholders. Use for statement slides or section headers with custom shapes. |
| 10 | `Media Layout` | Title + media clip placeholder. Use for embedding video or audio. |
| 11 | `Title_Subtitle_Image Layout` | Title + subtitle + image area. Use for visual concepts with explanatory subtitle. |
| 12 | `Title_Subtitle_Content Layout` | Title + subtitle + multiple text placeholders. Use for multi-point content with a subtitle. |
| 13 | `Blue shape_Title_Subtitle_Content_3 Layout` | Title + subtitle + 3 content areas + blue shape. Use for three-column comparisons or feature breakdowns. |
| 14 | `Divider_1` | **Section divider.** Title + subtitle. Used for the "Any more Questions?" slide and for separating major sections. |
| 15 | `1_Divider_1` | Alternate section divider (variant of Divider_1). |
| 16–20 | `Divider_2` through `Divider_6` | Additional divider variants with different visual styles. Choose based on visual preference. |
| 21 | `Title_Numbered_Content` | Title + 12 numbered text placeholders. Use for ordered lists or step-by-step content. |
| 22 | `Title_Month_Content` | Title + 12 month-labeled placeholders. Use for monthly timelines or calendar views. |
| 23 | `Title_Week_Content` | Title + 12 week-labeled placeholders. Use for weekly timelines or sprint views. |
| 24 | `1_Title Only` | Title + one text placeholder. Simple layout for minimal content slides. |
| 25 | `ThankYou` | **Closing slide** (last slide only). "Thank you." slide with footer. |

---

## 6. Required Slide Structure

Every module **must** contain the following slides in this exact order. Authors insert content slides between slide 2 and the demo slide.

```
┌─────────────────────────────────────────────────────────────┐
│ Slide 1:  Title Slide              (Layout: 1_Title square photo)     │
│ Slide 2:  Module Changelog         (Layout: Title Only) [HIDDEN]      │
│           ── Author inserts content slides here ──                     │
│ Slide N-2: Suggested Live Demos    (Layout: Agenda Layout)            │
│ Slide N-1: Any More Questions?     (Layout: Divider_1)                │
│ Slide N:   Thank You               (Layout: ThankYou)                 │
└─────────────────────────────────────────────────────────────┘
```

### Rules

- **Slide 1 (Title)** and **Slide 2 (Changelog)** are always the first two slides.
- **Content slides** are inserted between slide 2 and the demos slide. Authors may add any number of content slides.
- **Demo slide** must appear immediately before the "Any more Questions?" slide.
- **"Any more Questions?"** and **"Thank you."** are the last two slides and must not be modified or removed.
- **Slide 2 is always hidden** (not shown during presentation).

---

## 7. Title Slide (Slide 1) — Metadata Fields

The title slide uses layout `1_Title square photo` and contains the following elements:

### Placeholder Fields

| Element | Location | Content | Example |
|---------|----------|---------|---------|
| **Title** | Center | Always `Azure Cost Management & FinOps`. Do not change. | `Azure Cost Management & FinOps` |
| **Subtitle line 1** | Below title | `<Category> - <Topic>` — the category and topic of this module. Author fills this in. | `FinOps - FinOps Framework Introduction` |
| **Subtitle line 2** | Below line 1 | `Presented by: <<Presenter>>` — presenter fills in at delivery time. | `Presented by: <<Presenter>>` |
| **Subtitle line 3** | Below line 2 | `Date: <<Date>>` — presenter fills in at delivery time. | `Date: <<Date>>` |

### Bottom-Bar Metadata Shapes

Four rectangular shapes along the bottom of the slide contain module metadata:

| Shape | Content | How to Fill |
|-------|---------|-------------|
| **Module ID** (Rectangle 6) | `M-<NNN>` | Replace `XXXX` with the three-digit module number (e.g., `M-016`). |
| **Module last modified** (Rectangle 13) | `Module last modified: dd.mm.yyyy` | Set to the date of the most recently modified slide in the module (see Section 12). |
| **Primary target audience** (Rectangle 11) | `Primary target audience: <value>` | Replace `<value>` with one of: `FinOps`, `Product`, `agnostic`. |
| **Microsoft contract type** (Rectangle 12) | `Microsoft contract type: <value>` | Replace `<value>` with one of: `EA`, `MCA-E`, `agnostic`. |

### Variable Convention

- **Single angle brackets** `<text>`: Description of what the **author** should enter at authoring time. Replace the entire `<text>` with actual content.
- **Double angle brackets** `<<text>>`: Variable that the **presenter** fills in at delivery time. Leave as-is in the authored module.

---

## 8. Changelog Slide (Slide 2, Hidden)

Slide 2 uses layout `Title Only` and is **always hidden**. It contains:

- **Title:** `Module Changelog`
- **Table** with 5 columns:

| Column | Description | Format |
|--------|-------------|--------|
| **Date** | Date of the change | `dd.mm.yyyy` |
| **Slides** | Slide number(s) affected | Comma-separated numbers (e.g., `3, 5, 7`) |
| **Change Type** | Severity of change | `MAJOR` or `MINOR` (see definitions below) |
| **Change description** | Brief description of what changed | Free text, concise |
| **Author** | Microsoft alias of the person who made the change | e.g., `DirkBri` |

### Change Type Definitions

| Type | When to Use |
|------|-------------|
| `MAJOR` | New module creation, significant content rewrite, structural changes, topic expansion |
| `MINOR` | Typo fixes, date updates, formatting adjustments, adding/updating demo entries, small content additions |

### How to Add a Changelog Entry

1. Add a new row at the **top** of the table (directly below the header row). This ensures the most recent change is always first.
2. Fill in all five columns.
3. If the table is full, add more rows as needed.
4. For a brand-new module, the first entry should be:

| Date | Slides | Change Type | Change description | Author |
|------|--------|-------------|--------------------|--------|
| `dd.mm.yyyy` | `All` | `MAJOR` | `Initial module creation` | `<YourAlias>` |

> **Note for AI tools:** When modifying a module programmatically, always add a changelog entry. Use today's date, list all affected slide numbers, classify the change type, and use the appropriate author alias.

---

## 9. Demo Slide

The demo slide uses layout `Agenda Layout` and appears immediately before the "Any more Questions?" slide. It is **optional but recommended** — include it if applicable and valuable for the module's topic.

### Structure

| Element | Content |
|---------|---------|
| **Title area** (left blue bar) | `Suggested live demos` |
| **Disclaimer** (first paragraph, italic) | `The following demos are optional and non-invasive — no resources will be added, modified, or deleted in your environment.` |
| **Demo entries** (bulleted list) | `Demo 1: <description>` through `Demo 5: <description>` |

### Demo Entry Rules

- Prefix each entry with bold **`Demo N:`** followed by a space and the description.
- Use short, precise keywords. Include links if helpful.
- All demos **must be non-invasive**: view, analyze, filter, export only — never create, modify, or delete customer resources.
- Include 1–5 demos. Not every slot needs to be filled.
- Tailor demos to the module's target audience:

| Audience | Demo Focus |
|----------|------------|
| **FinOps** (central team) | Azure portal billing views, cost analysis, reports, exports, governance |
| **Product** (technical team) | Resource-level config, metrics, workload optimization views |
| **agnostic** | Both FinOps and Product perspectives |

### Customer-Centric Demos

Whenever possible, demos should use **the customer's own environment** rather than generic test data. This reinforces learning through immediate relevance.

- **Pre-session:** Note in slide notes what access or information the presenter needs to prepare (e.g., "Request read access to the customer's billing scope before the session").
- **During session:** Encourage the customer to navigate alongside the presenter in their own portal.
- **Fallback:** If customer environment access is unavailable, use the demo description as a walkthrough guide with generic data, but note this in the slide notes.

---

## 10. Content Slides

Content slides are the core of the module. They are inserted between **slide 2** (hidden changelog) and the **demo slide**.

### Authoring Rules

1. **Use only template layouts** — select from the layouts listed in Section 5. Do not create custom layouts or modify the slide master.
2. **Educational flow** — arrange slides in a logical sequence that builds understanding progressively:
   - **Introduce** the concept (what and why)
   - **Explain** the details (how it works)
   - **Demonstrate** practical application (show it in context)
   - **Summarize** key takeaways
3. **One idea per slide** — avoid overcrowding. If a slide has too much content, split it.
4. **Consistent terminology** — use Azure product names exactly as they appear in official Microsoft documentation.
5. **Slide notes** — every content slide must have `Slide last modified: dd.mm.yyyy` as the first line of its notes section (see Section 11).
6. **Visual consistency** — use the template's built-in color scheme, fonts, and placeholder styles. Do not introduce custom colors or fonts.
7. **Interactive checkpoints** — after every 3–4 content slides, include a natural discussion point. Document it in slide notes (e.g., "Discussion: Ask the customer how they currently handle this."). See Section 3.6.

---

## 11. Slide Notes — Date Tracking Convention

**Every slide** in the module (including the title slide, changelog, demos, and closing slides) must have the following as the **first line** of its notes section:

```
Slide last modified: dd.mm.yyyy
```

### Rules

| Rule | Detail |
|------|--------|
| **Format** | `dd.mm.yyyy` — two-digit day, two-digit month, four-digit year, separated by dots. |
| **When to update** | Every time the slide's visible content or notes are modified, update this date to the current date. |
| **New slides** | Set the date to the creation date. |
| **Unmodified slides** | Do not change the date. |
| **Additional notes** | Any additional speaker notes go **after** the `Slide last modified:` line. |

### Example

```
Slide last modified: 14.02.2026
This slide explains the FinOps framework lifecycle.
Key talking points:
- Inform, Optimize, Operate
- Maturity model levels
```

---

## 12. Date Tracking — Module-Level

The **"Module last modified"** field on the title slide (Rectangle 13) must always reflect the **most recent** `Slide last modified` date across all slides in the module.

### Workflow

1. After editing any slide(s), update the `Slide last modified:` date in the notes of each changed slide.
2. Scan all slides to find the latest `Slide last modified:` date.
3. Set `Module last modified: dd.mm.yyyy` on the title slide to that latest date.

> **Note for AI tools:** After any modification, iterate through all slides, parse the `Slide last modified:` date from each notes section, determine the maximum date, and update the title slide's "Module last modified" shape accordingly.

---

## 13. Change Tracking Workflow

Every modification to a module requires three coordinated updates:

```
1. Update the slide content
         │
         ▼
2. Update "Slide last modified: dd.mm.yyyy" in the notes of each changed slide
         │
         ▼
3. Add an entry to the Changelog table (slide 2)
         │
         ▼
4. Update "Module last modified: dd.mm.yyyy" on the title slide
   (set to the latest "Slide last modified" date across all slides)
```

### Checklist for Every Change

- [ ] Content changes applied to the relevant slides
- [ ] `Slide last modified:` updated in the notes of every modified slide
- [ ] New row added to the top of the Changelog table (slide 2) with date, affected slides, change type, description, and author
- [ ] `Module last modified:` on the title slide updated to the latest date

---

## 14. Publishing Process

When a module has been created or updated and is ready for publishing:

1. **Verify** all checklist items from Section 13 are complete.
2. **Review** the module for educational flow, completeness, and accuracy.
3. **Validate VBD readiness** — confirm the module meets the content design principles in Section 3:
   - Clear purpose and measurable outcomes defined
   - Interactive checkpoints documented in slide notes
   - Logical progressive flow with right-sized content
4. **Save** the file with the correct naming convention (Section 2).
5. **Inform Dirk** that the module is ready for publishing. Include:
   - The module file name
   - Whether this is a new module or an update
   - A brief summary of changes (for updates)

### Post-Delivery Expectations

After a module is delivered:

1. **Complete the deck** — the presenter fills in any decisions, next steps, and action items captured during the session in the slide notes.
2. **Handover** — the completed deck (with session notes) serves as a standalone record that can be shared or used for follow-up planning.
3. **Recommendations traceability** — every recommendation made during the session should trace back to a specific section of the module, ensuring accountability and follow-through.

---

## 15. Quick Reference — New Module Checklist

Use this checklist when creating a brand-new module from scratch:

1. **Copy the template** from the development SharePoint folder.
2. **Rename the file** following the `M-<NNN>-<Category>-<Topic>.pptx` convention.
3. **Slide 1 — Title slide:**
   - Set the subtitle to `<Category> - <Topic>`.
   - Set the module ID (`M-<NNN>`).
   - Set the primary target audience.
   - Set the Microsoft contract type.
   - Leave `<<Presenter>>` and `<<Date>>` as variables.
   - Set `Module last modified:` to today's date.
   - Set `Slide last modified:` in notes to today's date.
4. **Slide 2 — Changelog:**
   - Add the first entry: Date = today, Slides = `All`, Change Type = `MAJOR`, Description = `Initial module creation`, Author = your alias.
   - Set `Slide last modified:` in notes to today's date.
5. **Add content slides** between slide 2 and the demo slide.
   - Use only template layouts.
   - Follow the educational flow: introduce → explain → demonstrate → summarize.
   - Include interactive discussion prompts in slide notes every 3–4 slides.
   - End with a "Key Takeaways" slide summarizing the module's learning objectives.
   - Set `Slide last modified:` in notes to today's date for each new slide.
6. **Document scope** — in slide notes on slide 1 or the first content slide, state what is in scope, out of scope, any assumptions, prerequisites, and dependencies on other modules.
7. **Demo slide:**
   - Fill in 1–5 non-invasive demo descriptions (if applicable).
   - Set `Slide last modified:` in notes to today's date.
8. **Leave closing slides** ("Any more Questions?" and "Thank you.") unchanged.
9. **Update `Module last modified:`** on slide 1 to today's date.
10. **Inform Dirk** that the module is ready.

---

## 16. Quick Reference — Module Update Checklist

Use this checklist when updating an existing module:

1. **Open the existing module** from the development SharePoint folder.
2. **Make content changes** on the relevant slides.
3. **Update `Slide last modified:`** in the notes of every changed slide.
4. **Add a Changelog entry** at the top of the table in slide 2.
5. **Update `Module last modified:`** on slide 1 to the latest date.
6. **Save** the file (do not change the file name unless the topic changed).
7. **Inform Dirk** that the update is ready.

---

## 17. Rules for AI Tools

When an AI tool is used to create, modify, or update a module, it **must** adhere to all rules in this guide. Additionally:

| Rule | Detail |
|------|--------|
| **Always use the template** | Start from `M-xxx-Category-Topicwithincategory.pptx`. Never generate slides from scratch. |
| **Preserve fixed slides** | Do not remove or reorder slides 1, 2, or the closing slides (Q&A + Thank you). |
| **Use only template layouts** | Reference layouts by their exact names as listed in Section 5. Do not create or modify layouts. |
| **Track all changes** | After any modification, update slide notes dates, the changelog, and the module-level date. |
| **Parse dates carefully** | The date format is `dd.mm.yyyy` (European format). `05.02.2026` means February 5, 2026 — not May 2. |
| **Maintain slide order** | Content slides go between slide 2 and the demo slide. Never insert content after the demo slide. |
| **Non-invasive demos only** | Any generated demo descriptions must be read-only operations. Never suggest demos that create, modify, or delete resources. |
| **Module scope** | If asked to add content that belongs to a different topic, create a separate module instead. |
| **Notify after changes** | Remind the author to inform Dirk when the module is ready for publishing. |
| **Apply VBD principles** | All content must follow Section 3 — clear purpose, outcome-driven, interactive checkpoints, logical flow, and consistency. |
| **Document scope in notes** | When creating a module, populate slide notes on slide 1 with in-scope, out-of-scope, assumptions, prerequisites, and dependencies. Cross-reference existing modules by ID. |
| **Include interaction prompts** | Add discussion questions or customer exploration prompts in slide notes every 3–4 content slides. Format: "Discussion: [question for the customer]". |
