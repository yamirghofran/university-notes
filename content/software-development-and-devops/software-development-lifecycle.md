---
title: Software Development Lifecycle
---

Structured process for building and maintaining software from idea to retirement.

Structured processes ensure software is delivered reliably, on-time, and aligned with user needs.

![](../attachments/pasted-image-20250913135512.png)
# Phases
SLDC has many phases
1. Planning
2. Requirements Analysis
3. Design
4. Development
5. Testing
6. Deployment
7. Operations & Maintenance

There are also **extended phases**
- Proof of Concept (PoC)
- Continuous Improvement
- 
## Planning
aka Feasibility Study, Concept Phase, Project Initiation
- Define objectives, scope, stakeholders, and high-level requirements
- Assess feasibility (technical, financial, operational, etc.)

## Requirements Analysis
aka Business Analysis, Discovery, Requirement Engineering
- Collect functional & non-functional requirements
	- functional: what the product does and how it behaves
	- non-functional: more broad metrics (e.g. uptime, etc.)
- Document requirements in Software Requirements Specification (SRS)
## Design
aka System Design, Architecture & Modeling, Technical Design
- Translate requirements into system architecture
- High-level design (HLD): architecture, modules, data flow
- Low-level design (LLD): detailed algorithms, database schemas
## Development
aka Implementation, Coding, Programming
- Actual programming of the software
- Translate design and requirements into working code
- Integrating modules, building features

## Testing
aka Verification, Validation, Quality Assurance (QA)
- Ensure the software meets requirements.
- Types of testing
	- Unit Testing
	- Integration Testing
	- System Testing
	- User Acceptance Testing
	- Regression Testing

## Deployment
aka Release, Delivery
- Delivering the product to the user environment
- Involves setting up servers, databases, and configurations

## Operations & Maintenance
aka Maintenance, Operations, Support
- Bug fixing, patching, performance tuning
- Performance monitoring
- Feature upgrades
- Adapting to new requirements

## Proof of Concept
aka Prototyping
- Building a mock-up or prototype before full development
- Common in Agile, Spiral, and Design Thinking

## Continuous Improvement
- Agile/Devops treat this as an ongoing cycle
- Integrates monitoring and user feedback after deployment


# Models
## Waterfall
Royce, 1970
- Linear, **sequential** process
- Clear **documentation**
- Rigid structure, inflexible to change
- Weakness: design **issues found later** intesting
![](../attachments/pasted-image-20250913135653.png)
![](../attachments/cleanshot-2025-09-13-at-1356582x.png)
## V-Model
Late 80s, early 90s
- Matches dev phases with test phases
- Focus on quality and testing early in the process.
- Weakness: still rigid, better for slow-changing requirements
![](../attachments/pasted-image-20250913135821.png)
## Spiral
Boehm, 1088
- Iterative cycles combining development + risk analysis
- Good for large, complex, or high-risk projects
- Weakness: can be costly and require strong risk management
![](../attachments/pasted-image-20250913135914.png)
## Agile
### Manifesto
- Individuals and interactions over processes and tools
- Working software over comprehensive documentation
- Customer collaboration over contract negotiation
- Responding to change over following a plan
### Methodologies
- Iterative, incremental delivery in short cycles.
- Focus on customer collaboration, adaptability, and continuous feedback
- Integrated with Devops: automation, CI/CD, and continuous improvement.

# Roles and Responsibilities
## Business Analyst / Product Owner
- Defines requirements & priorities
## Software Architect / Designer
- Creates system architecture & design
## Developer / Programmer
- Builds features & integrates components
## Tester / QA Engineer
- Verifies quality through testing
## Agile Coach
- Facilitates team process & removes blockers
## Devops Engineer
- Automates builds, testing, deployment, and monitoring
## UI/UX Designer
- Ensures usability and customer experience
## Site Reliability Engineer (SRE)
- Focuses on reliability, scalability, and performance.