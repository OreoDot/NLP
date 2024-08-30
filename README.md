# NLP_Project
First upload from local drive
# Self-Regulated Learning (SRL) Study App Prototype - NLP Component

This repository contains the implementation of the NLP (Natural Language Processing) component within a broader Self-Regulated Learning (SRL) study app prototype. The NLP component is designed as a functional module to demonstrate the use of natural language processing in educational technology, particularly for automated question generation and answer evaluation.

## Project Structure

This project is divided into three key iterations, each representing a different stage of development for the NLP component:

### Iteration 1: Basic Functionality
- **Description:** The first iteration focuses on creating a simple NLP module that can preprocess text, generate predefined questions, and evaluate user answers using keyword matching.
- **Functionality:** 
  - Text preprocessing (tokenization, lemmatization).
  - Question generation.
  - Simple answer evaluation with basic scoring.
- **Limitations:** Feedback is limited to a score without detailed analysis.

### Iteration 2: Enhanced Feedback
- **Description:** This iteration builds on the initial functionality by providing more detailed feedback to users. It highlights correct and omitted parts of the user's answer, giving clearer insights into their performance.
- **Functionality:**
  - Enhanced answer evaluation with detailed feedback.
  - Highlighting correct and omitted tokens in user responses.
- **Limitations:** Questions are still predefined, and there is no external input support.

### Iteration 3: File Input Support
- **Description:** The final iteration introduces the ability to process text from external `.txt` files. Users can input their own content, and the script will generate questions and evaluate answers based on that content, while maintaining the enhanced feedback from Iteration 2.
- **Functionality:**
  - File input for external text processing.
  - Continued support for detailed feedback.
- **Limitations:** Question generation is still based on predefined questions rather than dynamically generated from the input text.

## Installation

To run the project, you'll need to have Python and the necessary libraries installed.

### Requirements
- Python 3.x
- spaCy (`pip install spacy`)
- termcolor (`pip install termcolor`)

### Setup

1. Clone the repository

2. Install spaCy and download the language model:
    ```bash
    pip install spacy
    python -m spacy download en_core_web_sm
    ```

3. Install termcolor:
    ```bash
    pip install termcolor
    ```

4. Run the script:
    ```bash
    python main.py
    ```

### Usage

- **Iteration 1:** The first script generates predefined questions and evaluates user answers using basic keyword matching.
- **Iteration 2:** This version adds enhanced feedback, highlighting correct and omitted parts of the answer.
- **Iteration 3:** The final script allows for file input, enabling the user to analyze external text files while maintaining detailed feedback.

### Example Usage

- For Iteration 3, you can run the script and provide a `.txt` file containing educational content. The script will generate questions and evaluate the user's answers based on the content of the file.

## Future Development

This project is a proof of concept that demonstrates the potential of NLP in educational technology. Future development could include:
- Dynamic question generation based on input text.
- Integration of machine learning models for more advanced answer evaluation.
- A more user-friendly interface for improved interaction.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or collaboration, reach out at dotore1818@gmail.com
