# DataHouseCompatibilityPredictor

This code takes input data in the form of a dictionary input_data, which has two keys: "team" and "applicants". The "team" key contains a list of dictionaries, where each dictionary represents a team member and their attributes, and the "applicants" key contains a list of dictionaries, where each dictionary represents an applicant and their attributes.

The code then calculates a compatibility score for each applicant based on their attributes compared to the team members' attributes. It uses a function calculate_score to calculate the compatibility score for a single applicant and another function calculate_scores to calculate the compatibility scores for all applicants.

The output of the code is a dictionary containing a list of dictionaries, where each dictionary represents an applicant and their compatibility score. The key of the outer dictionary is "scoredApplicants", and the value is the list of dictionaries.

The output data is then printed using print(output_data).