# Identity Validation & Risk Scoring

## Overview

This section demonstrates a proposed validation and risk-assessment workflow using a synthetic dataset of **500 fictional fintech applications**.

The objective is to demonstrate how multiple validation indicators can be combined to help prioritise applications for standard processing, additional verification, manual review, or investigation.

**Important:** This is an independent portfolio project. The dataset is entirely fictional, and the scoring weights, thresholds, and recommended actions are proposed for demonstration purposes. They do not represent PayJoy's internal fraud rules, systems, policies, or procedures.

---

## What I Built

I created a synthetic dataset containing application-level validation indicators and developed a Python-based risk-scoring model.

The model evaluates indicators including:

* ID verification
* Name matching
* Phone verification
* Document quality
* Previous applications
* Applications associated with the same device
* Applications associated with the same phone number
* Applications associated with the same address
* Recent SIM changes

The indicators are combined into a proposed risk score.

---

## Risk Classification

For this portfolio model:

| Risk Level | Score | Proposed Action                         |
| ---------- | ----: | --------------------------------------- |
| LOW        |  0–29 | Proceed with standard validation        |
| MEDIUM     | 30–59 | Additional verification / manual review |
| HIGH       |   60+ | Hold application and investigate        |

These thresholds are fictional and are used only to demonstrate a potential validation workflow.

---

## Why Multiple Indicators Matter

A single unusual indicator does not necessarily mean that an application is fraudulent.

For example:

* Multiple applications from one device could indicate suspicious activity.
* However, the same device could legitimately be shared by members of the same household.
* A recent SIM change may require additional verification, but it is not by itself proof of identity theft.
* A document-quality issue may simply require the customer to submit a clearer document.

For this reason, the model is designed to help **prioritise cases for review rather than automatically determine that fraud has occurred**.

---

## Python Risk-Scoring Model

The `risk_scoring.py` script:

1. Loads the synthetic application dataset.
2. Evaluates the validation indicators.
3. Calculates a proposed risk score.
4. Classifies each application.
5. Assigns a recommended action.
6. Saves the results to `scored_applications.csv`.
7. Produces a summary of the risk levels.
8. Displays the highest-risk applications for further investigation.

---

## Files

| File                         | Purpose                                                 |
| ---------------------------- | ------------------------------------------------------- |
| `synthetic_applications.csv` | 500 fictional application records                       |
| `risk_scoring.py`            | Python risk-scoring model                               |
| `scored_applications.csv`    | Applications with calculated scores and classifications |

---

## Skills Demonstrated

* Identity and document validation
* Fraud-risk awareness
* Pattern recognition
* Risk assessment
* Data analysis
* Python
* Pandas
* Decision-making
* Manual-review prioritisation
* False-positive awareness
* Customer-centric validation

---

## Validation Philosophy

The purpose of validation is not simply to reject applications.

A strong validation process should aim to:

**Identify genuine risk → investigate evidence → protect legitimate customers → escalate appropriately → improve the process**

This project therefore considers fraud prevention alongside customer experience, accuracy, privacy, and operational efficiency.

