# Fraud Investigation Cases

## Purpose

This section demonstrates how a validation support representative could investigate potentially suspicious applications using identity, device, phone, address and document-quality indicators.

All cases in this portfolio are fictional and use synthetic scenarios. They do not represent PayJoy's internal fraud rules, thresholds, systems or customer data.

The objective is not to automatically reject high-risk applications. The objective is to assess available evidence, consider legitimate explanations, protect customers from identity-related fraud and escalate cases when additional investigation is required.

---

# Case 01 — Identity Verification Failure

### Risk indicators

* Government ID verification failed
* Name does not match the submitted application
* Phone verification passed
* Document quality was acceptable

### Initial assessment

The combination of an unsuccessful identity verification and name mismatch creates a significant identity-risk concern.

### Investigation approach

I would:

1. Review the submitted identity information.
2. Check whether the mismatch could be caused by a legitimate name change or data-entry error.
3. Review the available verification results.
4. Avoid requesting unnecessary personal information.
5. Escalate for additional verification if the discrepancy cannot be resolved.

### Decision

**Manual review required.**

The application should not automatically be treated as confirmed fraud solely because of the risk indicators.

### Customer impact

The customer should receive a clear explanation that additional verification is required, without revealing internal fraud-detection rules.

---

# Case 02 — Multiple Applications From One Device

### Risk indicators

* Four applications associated with the same device
* Identity verification passed
* Name match passed
* Phone verification passed
* Document quality was good

### Initial assessment

Multiple applications from one device may indicate coordinated activity, but it can also have legitimate explanations.

### Investigation approach

I would determine:

* Whether the identities associated with the applications are different.
* Whether the applications belong to members of the same household or legitimate customer group.
* Whether other risk indicators are present.
* Whether the activity occurred within an unusually short period.

### Decision

**Additional verification / manual review.**

The device indicator alone should not be treated as proof of fraud.

### Customer impact

Avoid unnecessarily blocking legitimate customers who may share a device or have a legitimate reason for repeated applications.

---

# Case 03 — Multiple Applications Using One Phone Number

### Risk indicators

* Three applications associated with the same phone number
* One application has a name mismatch
* Identity verification failed on one application
* Recent SIM change detected

### Initial assessment

Several indicators appear together, increasing the need for investigation.

### Investigation approach

I would review the relationship between the applications and determine whether the activity could indicate account takeover, identity misuse or another explanation.

I would also verify whether the phone-number information is being used consistently across the applications.

### Decision

**Hold application and investigate.**

The combination of indicators warrants escalation rather than immediate approval.

### Customer impact

Where appropriate, the legitimate customer should be given a path to verify their identity and resolve the issue.

---

# Case 04 — Poor Document Quality

### Risk indicators

* Poor document quality
* Identity verification passed
* Name match passed
* Phone verification passed
* No unusual device activity

### Initial assessment

Poor image quality can create a validation problem without necessarily indicating fraud.

### Investigation approach

I would determine whether the document is simply difficult to read or whether there are signs of manipulation or inconsistency.

If the problem is image quality only, I would request a clearer submission through the appropriate process.

### Decision

**Additional verification required.**

### Customer impact

This approach reduces false positives by distinguishing a technical/document-quality problem from an actual identity concern.

---

# Case 05 — Legitimate Shared Household Device

### Risk indicators

* Three applications from the same device
* Applications belong to different individuals
* All identities successfully verified
* Names match
* Phones are different
* Addresses are consistent with a shared household

### Initial assessment

The shared-device indicator initially appears suspicious.

However, the remaining evidence provides a plausible legitimate explanation.

### Investigation approach

I would consider the complete evidence rather than relying on one indicator.

### Decision

**Proceed with standard validation**, assuming all other required checks are satisfactory.

### Key learning

A fraud-control process should account for legitimate customer behaviour.

A shared device is an indicator for investigation, not automatic proof of fraud.

---

# Case 06 — Recent SIM Change

### Risk indicators

* Recent SIM change
* Identity verification passed
* Name match passed
* Phone verification requires additional review
* No previous applications

### Initial assessment

A recent SIM change can be relevant to identity and account-security investigations, but it can also occur for legitimate reasons.

### Investigation approach

I would consider:

* Whether identity verification passed.
* Whether other suspicious indicators are present.
* Whether the customer's explanation is consistent with the available information.

### Decision

**Additional verification / manual review.**

### Customer impact

The customer should not be treated as fraudulent simply because a SIM change occurred.

---

# Case 07 — High Risk Score With Conflicting Evidence

### Risk indicators

* High calculated risk score
* Identity verification passed
* Name match passed
* Multiple applications from the same device
* Multiple applications associated with the same phone
* Recent SIM change

### Initial assessment

The calculated score indicates elevated risk, but some core identity checks have passed.

### Investigation approach

I would investigate the underlying indicators rather than relying exclusively on the numerical score.

The purpose of the score is to prioritize cases for human review, not replace human judgment.

### Decision

**Hold application and investigate.**

### Key learning

Risk scoring should support investigators rather than make decisions without context.

---

# Case 08 — Possible False Positive

### Risk indicators

* Same address associated with multiple applications
* Identity verification passed
* Name match passed
* Phone numbers are different
* Devices are different

### Initial assessment

A shared address can appear unusual, but it may be completely legitimate.

### Investigation approach

I would consider whether the applications could reasonably belong to different people living at the same address.

No decision should be based solely on the shared-address indicator.

### Decision

**Proceed with standard validation**, provided all other required checks are satisfactory.

### Key learning

Fraud prevention must balance fraud detection with the risk of incorrectly restricting legitimate customers.

---

# Case 09 — Customer Dispute

### Scenario

A customer contacts support because their application was placed under review. They state that they are the legitimate applicant and do not understand why additional verification is required.

### Investigation approach

I would:

1. Listen carefully to the customer's explanation.
2. Verify the available case information.
3. Avoid disclosing sensitive internal fraud rules.
4. Explain the verification process clearly.
5. Determine whether additional documentation or verification is appropriate.
6. Escalate if the case cannot be resolved within the available support process.

### Decision

**Continue the verification process while maintaining clear customer communication.**

### Customer-service principle

Fraud prevention and customer support should work together. A customer can be treated respectfully even when an application requires additional investigation.

---

# Case 10 — Escalation for Possible System Issue

### Scenario

Several legitimate-looking applications suddenly begin failing the same validation step.

### Initial assessment

A repeated pattern across multiple apparently legitimate cases could indicate something other than individual customer fraud.

### Investigation approach

I would:

* Compare affected cases for common characteristics.
* Document the repeated failure.
* Check whether the issue appears isolated or widespread.
* Avoid manually overriding controls without authorization.
* Escalate the pattern to the appropriate technical or operational team.

### Decision

**Escalate potential system/tool issue.**

### Key learning

A validation representative should be able to distinguish between a suspicious customer pattern and a possible system problem.

---

# Investigation Principles Demonstrated

These cases demonstrate five principles:

1. **Investigate before concluding.**
2. **Use multiple indicators rather than relying on one signal.**
3. **Consider legitimate explanations and false positives.**
4. **Protect customer information and avoid unnecessary data exposure.**
5. **Escalate appropriately when evidence or system behaviour requires further investigation.**

## Portfolio Disclaimer

This is an independent portfolio project created using fictional scenarios and synthetic data. The scoring methodology and investigation thresholds are proposed for demonstration purposes and do not represent PayJoy's internal policies, fraud models, operational procedures or confidential information.
