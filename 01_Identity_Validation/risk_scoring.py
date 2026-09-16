import pandas as pd
# NOTE:
# This is a proposed portfolio scoring model using synthetic data.
# The weights and thresholds are illustrative and do not represent
# PayJoy's internal fraud rules, policies, or scoring methodology.
#
# The model is designed to demonstrate how multiple validation
# indicators could be combined to prioritise cases for review.
# Load the synthetic application dataset
df = pd.read_csv("synthetic_applications.csv")


# --------------------------------------------------
# RISK SCORING RULES
# --------------------------------------------------

def calculate_risk_score(row):

    score = 0

    # Identity verification
    if row["id_verified"] == "No":
        score += 30

    # Name mismatch
    if row["name_match"] == "No":
        score += 30

    # Phone verification
    if row["phone_verified"] == "No":
        score += 15

    # Document quality
    if row["document_quality"] == "Poor":
        score += 10
    elif row["document_quality"] == "Acceptable":
        score += 3

    # Multiple previous applications
    if row["previous_applications"] >= 3:
        score += 10

    # Multiple applications from same device
    if row["applications_same_device"] >= 3:
        score += 20

    # Multiple applications using same phone
    if row["applications_same_phone"] >= 3:
        score += 20

    # Multiple applications associated with same address
    if row["applications_same_address"] >= 3:
        score += 10

    # Recent SIM change
    if row["recent_sim_change"] == "Yes":
        score += 10

    return score


# Apply the scoring model
df["risk_score"] = df.apply(calculate_risk_score, axis=1)


# --------------------------------------------------
# RISK CLASSIFICATION
# --------------------------------------------------

def classify_risk(score):

    if score < 30:
        return "LOW"

    elif score < 60:
        return "MEDIUM"

    else:
        return "HIGH"


df["risk_level"] = df["risk_score"].apply(classify_risk)


# --------------------------------------------------
# RECOMMENDED ACTION
# --------------------------------------------------

def recommended_action(risk_level):

    if risk_level == "LOW":
        return "Proceed with standard validation"

    elif risk_level == "MEDIUM":
        return "Additional verification / manual review"

    else:
        return "Hold application and investigate"


df["recommended_action"] = df["risk_level"].apply(
    recommended_action
)


# --------------------------------------------------
# SAVE RESULTS
# --------------------------------------------------

df.to_csv(
    "scored_applications.csv",
    index=False
)


# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

print("\nRISK LEVEL SUMMARY")
print("------------------")

print(
    df["risk_level"].value_counts()
)

print("\nAVERAGE RISK SCORE")
print("------------------")

print(
    round(df["risk_score"].mean(), 2)
)

print("\nTOP 10 HIGHEST-RISK APPLICATIONS")
print("--------------------------------")

print(
    df[
        [
            "application_id",
            "risk_score",
            "risk_level",
            "recommended_action"
        ]
    ]
    .sort_values("risk_score", ascending=False)
    .head(10)
)
