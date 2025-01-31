# genXam 
## Your lightweight multiple choice exam generator

This repository contains a Python script that generates PDF exams from a JSON file containing questions and options. The purpose of this project is to simplify the creation of customizable exams that can be printed or shared electronically.

## Features

- Generate two (or more) versions of an exam.
- Automatic shuffling of questions for different exam versions to minimize chances of academic dishonesty.
- Option to create solved exams that display the correct answers.
- Questions are loaded from a JSON file, allowing for easy modification and updates.

## Requirements

- Python 3.x
- Libraries:
  - `reportlab`
  - `json`

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

    Install the necessary libraries:

    bash

    pip install reportlab

Usage

To generate the exams, run the generate_exam.py Python script. Ensure you have a questions.json file in the same directory that contains your exam questions.
Command

bash

    python generate_exam.py

This command will produce the following PDF files:

    exam_version_A.pdf: Version A of the exam.
    exam_version_B.pdf: Version B of the exam.
    exam_version_A_solved.pdf: Version A of the exam with answers.
    exam_version_B_solved.pdf: Version B of the exam with answers.

JSON File Structure

The questions.json file should have the following structure:

json

    {
        "title": "Example Exam | 1",
        "questions": [
            {
                "text": "What is the capital city of France?",
                "points": 1,
                "options": [
                    {"text": "Berlin", "is_correct": false},
                    {"text": "Madrid", "is_correct": false},
                    {"text": "Paris", "is_correct": true},
                    {"text": "Rome", "is_correct": false}
                ]
            },
            {
                "text": "Which is the largest continent by land area?",
                "points": 1,
                "options": [
                    {"text": "Africa", "is_correct": false},
                    {"text": "Asia", "is_correct": true},
                    {"text": "Europe", "is_correct": false},
                    {"text": "This is a very long answer to showcase that we can deal with linebreaks if needed. Not perfect but works reasonably well.", "is_correct": false}
                ]
            },
            {
                "text": "Which river is the longest in the world?",
                "points": 1,
                "options": [
                    {"text": "Amazon River", "is_correct": false},
                    {"text": "Nile River", "is_correct": true},
                    {"text": "Yangtze River", "is_correct": false},
                    {"text": "Mississippi River", "is_correct": false}
                ]
            },
            {
                "text": "Mount Everest is located in which mountain range?",
                "points": 1,
                "options": [
                    {"text": "Andes", "is_correct": false},
                    {"text": "Rockies", "is_correct": false},
                    {"text": "Himalayas", "is_correct": true},
                    {"text": "Alps", "is_correct": false}
                ]
            },
            {
                "text": "Which country has the largest population?",
                "points": 1,
                "options": [
                    {"text": "India", "is_correct": false},
                    {"text": "United States", "is_correct": false},
                    {"text": "China", "is_correct": true},
                    {"text": "Indonesia", "is_correct": false}
                ]
            },
        ]
    }
