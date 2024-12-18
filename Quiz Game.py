# Simple Multiple-Choice Quiz Game

# Define the questions, choices, and correct answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "choices": ["A) Harper Lee", "B) J.K. Rowling", "C) Ernest Hemingway", "D) Mark Twain"],
        "answer": "A"
    }
]

# Function to ask questions and check answers
def run_quiz(quiz_data):
    score = 0  # Initialize score
    for q in quiz_data:
        print(q["question"])
        for choice in q["choices"]:
            print(choice)
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1  # Increase score if correct
        else:
            print(f"Wrong! The correct answer was {q['answer']}\n")
    
    print(f"Quiz over! Your final score is {score}/{len(quiz_data)}")

# Main program
if __name__ == "__main__":
    print("Welcome to the Quiz Game!\n")
    run_quiz(quiz_data)
