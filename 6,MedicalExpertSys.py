import spacy
from spacy.matcher import PhraseMatcher

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

knowledge_base = {
    "cold": {
        "symptoms": ["headache", "runny nose", "sore throat"],
        "treatment": [
            "1: Tylenol",
            "2: Panadol",
            "3: Nasal spray",
            "4: Please wear warm clothes!"
        ]
    },
    "influenza": {
        "symptoms": ["fever", "cough", "body ache"],
        "treatment": [
            "1: Tamiflu",
            "2: Panadol",
            "3: Zanamivir",
            "4: Please take a warm bath and do salt gargling!"
        ]
    },
    "typhoid": {
        "symptoms": ["fever", "abdominal pain", "weakness"],
        "treatment": [
            "1: Chloramphenicol",
            "2: Amoxicillin",
            "3: Ciprofloxacin",
            "4: Azithromycin",
            "5: Please do complete bed rest and take soft diet!"
        ]
    },
    "chickenpox": {
        "symptoms": ["rash", "itching", "fever"],
        "treatment": [
            "1: Varicella vaccine",
            "2: Acetaminophen",
            "3: Antihistamines",
            "4: Apply calamine lotion"
        ]
    },
    "measles": {
        "symptoms": ["rash", "high fever", "cough"],
        "treatment": [
            "1: Vitamin A supplements",
            "2: Acetaminophen",
            "3: Plenty of fluids",
            "4: Rest in a dark room"
        ]
    },
    # Add more diseases with symptoms and treatment here
}

def extract_symptoms(user_input):
    matcher = PhraseMatcher(nlp.vocab)
    patterns = [nlp(text) for text in sum([disease["symptoms"] for disease in knowledge_base.values()], [])]
    matcher.add("SYMPTOMS", None, *patterns)
    doc = nlp(user_input)
    matches = matcher(doc)
    return list(set([doc[start:end].text for _, start, end in matches]))

def diagnose_disease(symptoms):
    for disease, info in knowledge_base.items():
        if all(symptom in symptoms for symptom in info["symptoms"]):
            return disease, info["treatment"]
    return None, None

def main():
    print("Welcome to the Medical Diagnosis Expert System!")
    while True:
        user_input = input("Please describe your symptoms: ")
        symptoms = extract_symptoms(user_input)
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




#Example -
# Welcome to the Medical Diagnosis Expert System!
# Please describe your symptoms: having fever and with it weakness and abdominal pain
# You have been diagnosed with typhoid!
# Please take the following medicines and precautions:
# 1: Chloramphenicol
# 2: Amoxicillin
# 3: Ciprofloxacin
# 4: Azithromycin
# 5: Please do complete bed rest and take soft diet!
# Do you want to diagnose another condition? (yes/no): yes

# Please describe your symptoms: am having rash with slight itching and also fever
# You have been diagnosed with chickenpox!
# Please take the following medicines and precautions:
# 1: Varicella vaccine
# 2: Acetaminophen
# 3: Antihistamines
# 4: Apply calamine lotion
# Do you want to diagnose another condition? (yes/no):
#
# Please describe your symptoms: I woke up with a splitting headache, with a runny nose, and a sore throat
# You have been diagnosed with cold!
# Please take the following medicines and precautions:
# 1: Tylenol
# 2: Panadol
# 3: Nasal spray
# 4: Please wear warm clothes!
# Do you want to diagnose another condition? (yes/no):


#pip install spacy


# Integration of spaCy: In the second version, we import and use the spaCy library to process the user's input symptoms.
# We tokenize the input, removing commas, and extract individual symptoms.
# This allows for a more natural way of inputting symptoms and makes the system more user-friendly.
#
# Enhanced Symptom Matching: With spaCy, we can handle variations in symptom input more effectively.
# For example, users can input symptoms in any order, and the system will still match them correctly with the symptoms listed in the knowledge base.
# Additionally, spaCy's linguistic features can help handle misspellings or synonyms of symptoms more robustly.