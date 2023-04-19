import json 

def calculate_score(applicant, team):
    """Calculates compatibility score for a single applicant"""
    score = 0
    for member in team:
        # Calculate the difference between each attribute and take the absolute value
        diff_intelligence = abs(applicant["attributes"]["intelligence"] - member["attributes"]["intelligence"])
        diff_strength = abs(applicant["attributes"]["strength"] - member["attributes"]["strength"])
        diff_endurance = abs(applicant["attributes"]["endurance"] - member["attributes"]["endurance"])
        diff_spicyFoodTolerance = abs(applicant["attributes"]["spicyFoodTolerance"] - member["attributes"]["spicyFoodTolerance"])
        
        # Add up the differences
        total_diff = diff_intelligence + diff_strength + diff_endurance + diff_spicyFoodTolerance
        
        # Calculate the compatibility score and add it to the total score for this applicant
        compatibility_score = 1 - (total_diff / 40)  # 40 is the maximum difference that can occur
        score += compatibility_score
    
    # Average the total score across all team members and return the result
    return score / len(team)


def calculate_scores(applicants, team):
    """Calculates compatibility score for all applicants"""
    scored_applicants = []
    for applicant in applicants:
        score = calculate_score(applicant, team)
        scored_applicant = {"name": applicant["name"], "score": score}
        scored_applicants.append(scored_applicant)
    return {"scoredApplicants": scored_applicants}


#Data being used:
input_data = {
    "team": [
        {
            "name": "Eddie",
            "attributes": {
                "intelligence": 1,
                "strength": 5,
                "endurance": 3,
                "spicyFoodTolerance": 1
            }
        },
        {
            "name": "Will",
            "attributes": {
                "intelligence": 9,
                "strength": 4,
                "endurance": 1,
                "spicyFoodTolerance": 6
            }
        },
        {
            "name": "Mike",
            "attributes": {
                "intelligence": 3,
                "strength": 2,
                "endurance": 9,
                "spicyFoodTolerance": 5
            }
        }
    ],
    "applicants": [
        {
            "name": "John",
            "attributes": {
                "intelligence": 4,
                "strength": 5,
                "endurance": 2,
                "spicyFoodTolerance": 1
            }
        },
        {
            "name": "Jane",
            "attributes": {
                "intelligence": 7,
                "strength": 4,
                "endurance": 3,
                "spicyFoodTolerance": 2
            }
        },
        {
            "name": "Joe",
            "attributes": {
                "intelligence": 1,
                "strength": 1,
                "endurance": 1,
                "spicyFoodTolerance": 10
            }
        }
    ]
}

output_data = calculate_scores(input_data["applicants"], input_data["team"])
print(output_data)

# input_data_json = json.dumps(input_data)

# output_data = calculate_scores(json.loads(input_data_json))

# output_data_json = json.dumps(output_data)

# # Print the output data in JSON format
# print(output_data_json)