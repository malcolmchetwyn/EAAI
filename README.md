# AI Enabled & Programmatic  Enterprise Architecture

## Overview
This project showcases the integration of AI tools to enhance and automate governance within the enterprise architecture (EA) framework as part of a DevOps pipeline. The objective is to ensure that solution changes consistently adhere to architectural guardrails and standards throughout the development lifecycle.

When applied across the entire lifecycle, this approach enables EA to closely track code development. It also offers stakeholders, particularly those in operations teams, faster and automated visibility into decisions that might deviate from EA or solution architecture (SA) guidelines, thereby reducing time-to-visibility.

Note: this code example shows how we apply Salesforce Well Architected to designs.

[![](https://i.postimg.cc/HxGchxcv/Screenshot-2024-08-20-at-5-04-14-PM.png)](https://i.postimg.cc/HxGchxcv/Screenshot-2024-08-20-at-5-04-14-PM.png)

By minimizing time-to-visibility, stakeholders can stay informed about decisions without disrupting development teams. Not all exceptions need to be blocked; in fact, many operational exceptions are acceptable and sometimes necessary.

Ultimately, reducing time-to-visibility allows solution architects, enterprise architects, and other stakeholders to mitigate risks more swiftly and with greater transparency.

### Enterprise Architecture Governance in DevOps Pipeline

Overview: The diagram illustrates how enterprise architecture (EA) models, standards, and guardrails are integrated into a DevOps pipeline to ensure alignment with architectural standards throughout the development lifecycle. It emphasizes the use of AI tools to enhance governance.

[![](https://i.postimg.cc/N0zTqw99/Screenshot-2024-08-20-at-4-56-44-PM.png)](https://i.postimg.cc/N0zTqw99/Screenshot-2024-08-20-at-4-56-44-PM.png)

#### Key Components:
- Enterprise Architecture Models: Includes blueprints, standards, and solution design that are evaluated against defined guardrails.
- Pre-Commit Hooks: Ensures code compliance with architectural standards before being committed.
- Continuous Integration (CI) Pipelines: Checks the code against all guardrails after it is pushed to the repository, running more resource-intensive tests without disrupting workflows.
- Purpose: The goal is to provide continuous feedback, maintain code quality, and reduce time-to-visibility, allowing stakeholders to mitigate risks more quickly and with greater transparency.

###  AI Confidence Index
 Overview: This image presents an AI Confidence Index used to measure the quality and accuracy of AI-generated responses.
 [![](https://i.postimg.cc/zX7QDY0f/Screenshot-2024-08-20-at-4-57-05-PM.png)](httphttps://i.postimg.cc/zX7QDY0f/Screenshot-2024-08-20-at-4-57-05-PM.png://)

#### Index Details:
- The index ranges from 0 (Untrustworthy) to 10 (Excellent).
- Each level describes the response quality, from "Highly accurate and well-articulated" to "Completely inaccurate or irrelevant."
- Purpose: The index serves as a tool to evaluate and rate AI outputs, helping users understand the reliability and precision of AI-driven insights.
 
 
### AI-Enabled Enterprise Architecture Governance
 Overview: This diagram focuses on the programmatic governance of enterprise architecture by leveraging AI tools across the entire software development lifecycle.
 [![](https://i.postimg.cc/FzyHkH18/Screenshot-2024-08-20-at-4-57-38-PM.png)](https://i.postimg.cc/FzyHkH18/Screenshot-2024-08-20-at-4-57-38-PM.png)
#### Key Elements:
- Enterprise Architecture Models: Includes standards and guardrails that feed into solution design and planning phases.
- Solution Index Ratings: AI-generated ratings that assess the compliance of solutions with established standards.
- Lifecycle Connection: The architecture models are visually connected with LLMs (Large Language Models), ensuring consistent alignment between code, configuration, and standards throughout the lifecycle, from planning to pre-production.
- Purpose: The objective is to enable continuous governance and monitoring of architecture models, ensuring that every stage of the development lifecycle adheres to architectural standards and practices.


------------



by Malcolm Fitzgerald and Chris Huggins

