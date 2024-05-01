knowledge_base = {
    "cold": {
        "symptoms": ["headache", "runny nose", "sneezing", "sore throat", "fever"],
        "treatment": [
            "1: Tylenol",
            "2: Panadol",
            "3: Nasal spray",
            "4: Please wear warm clothes!"
        ]
    },
    "influenza": {
        "symptoms": ["sore throat", "fever", "headache", "chills", "body ache"],
        "treatment": [
            "1: Tamiflu",
            "2: Panadol",
            "3: Zanamivir",
            "4: Please take a warm bath and do salt gargling!"
        ]
    },
    "typhoid": {
        "symptoms": ["headache", "abdominal pain", "poor appetite", "fever"],
        "treatment": [
            "1: Chloramphenicol",
            "2: Amoxicillin",
            "3: Ciprofloxacin",
            "4: Azithromycin",
            "5: Please do complete bed rest and take soft diet!"
        ]
    },
    # Add more diseases with symptoms and treatment here
}

def get_user_symptoms():
    print("Enter your symptoms separated by commas (e.g., headache, fever, sore throat): ")
    symptoms = input().strip().lower().split(", ")
    return symptoms

def diagnose_disease(symptoms):
    for disease, info in knowledge_base.items():
        if all(symptom in symptoms for symptom in info["symptoms"]):
            return disease, info["treatment"]
    return None, None

def main():
    print("Welcome to the Medical Diagnosis Expert System!")
    while True:
        symptoms = get_user_symptoms()
        disease, treatment = diagnose_disease(symptoms)
        if disease:
            print(f"You have been diagnosed with {disease}!")
            print("Please take the following medicines and precautions:")
            for item in treatment:
                print(item)
        else:
            print("Sorry, we couldn't diagnose your condition based on the provided symptoms.")

        choice = input("Do you want to diagnose another condition? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you for using the Expert system!")
            break

if __name__ == "__main__":
    main()
