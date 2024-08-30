import spacy
from termcolor import colored

# Load spaCy model
nlp = spacy.load('en_core_web_sm')


# Function to preprocess text
def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return tokens


# Function to generate questions based on the input text file
def generate_questions():
    questions = [
        ("What is the principle of conservation of energy?",
         "The principle of conservation of energy states that energy cannot be created or destroyed, only transferred or transformed from one form to another."),
        ("List the three states of matter.", "Solid, Liquid, Gas")
    ]
    return questions


# Function to evaluate the answers
def evaluate_answer(user_answer, correct_answer):
    user_tokens = preprocess_text(user_answer)
    correct_tokens = preprocess_text(correct_answer)
    matched_tokens = [token for token in user_tokens if token in correct_tokens]
    omitted_tokens = [token for token in correct_tokens if token not in user_tokens]
    score = len(matched_tokens) / len(correct_tokens) * 100 if correct_tokens else 0

    highlighted_correct_answer = ' '.join(
        [colored(token, 'red') if token in omitted_tokens else token for token in correct_answer.split()])

    return score, highlighted_correct_answer


# Main function to process text, generate questions, and evaluate answers
def main():
    file_path = input("Enter the path to the text file: ")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            input_text = file.read()
            print(f"\nInput text from file:\n{input_text}\n")

        questions = generate_questions()
        total_score = 0

        for question, correct_answer in questions:
            print(question)
            user_answer = input("Your answer: ")
            score, highlighted_correct_answer = evaluate_answer(user_answer, correct_answer)
            total_score += score
            print(f"Score for this answer: {score:.2f}%")
            print(f"Correct answer: {highlighted_correct_answer}\n")

        average_score = total_score / len(questions) if questions else 0
        print(f"Your average score: {average_score:.2f}%")

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")


if __name__ == "__main__":
    main()
