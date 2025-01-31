# SPDX-License-Identifier: MIT
"""
generate_exam.py

This script generates a PDF exam from a JSON file containing questions and options.
"""

import json
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def draw_wrapped_text(c, text, x, y, max_width):
    """
    Draws text on the canvas, wrapping it within the specified width.

    Args:
        c (canvas.Canvas): The canvas to draw on.
        text (str): The text to draw.
        x (int): The x-coordinate.
        y (int): The y-coordinate.
        max_width (int): The maximum width for the text.
    
    Returns:
        int: The y-coordinate after drawing the text.
    """
    lines = []
    words = text.split()
    current_line = words[0]
    
    for word in words[1:]:
        if c.stringWidth(current_line + ' ' + word, "Helvetica", 12) < max_width:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    
    for line in lines:
        c.drawString(x, y, line)
        y -= 15
    return y


def generate_exam_pdf(json_file, output_filename, solved=False, version_name=""):
    """
    Generates a PDF exam from a JSON file.

    Args:
        json_file (str): The path to the JSON file containing the questions.
        output_filename (str): The name of the output PDF file.
        solved (bool): Whether to include the correct answers in the PDF.
        version_name (str): The version name to include in the PDF.
    """
    try:
        with open(json_file, 'r') as f:
            exam_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file {json_file} was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file {json_file} is not a valid JSON file.")
        return
    
    random.seed(output_filename)
    random.shuffle(exam_data['questions'])
    
    left_offset = 50
    c = canvas.Canvas(output_filename, pagesize=letter)
    c.setFont("Helvetica", 16)
    page_start_y = 680
    c.drawString(left_offset, page_start_y + 50, exam_data["title"])
    c.drawString(left_offset, page_start_y + 30, "")
    c.drawString(left_offset, page_start_y + 10, "Student name: ____________________    Student ID: _____________")

    y_position = page_start_y - 40
    page_number = 1

    option_letters = ["a", "b", "c", "d", "e", "f"]
    for question_number, question in enumerate(exam_data['questions'], start=1):
        c.setFont("Helvetica", 12)
        question_text = f"{question_number}. [{question['points']}P] {question['text']}"
        y_position = draw_wrapped_text(c, question_text, left_offset, y_position, 500)
        y_position -= 5
        
        for i, option in enumerate(question['options']):
            option_text = f"{option_letters[i]}) {option['text']}"
            y_position = draw_wrapped_text(c, option_text, left_offset + 70, y_position, 430)
            c.rect(left_offset + 45, y_position + 15, 10, 10)
            if solved and option['is_correct']:
                c.drawString(left_offset + 45, y_position + 15, "✓")
            y_position -= 10
        
        y_position -= 25
        if y_position < 175:
            c.drawString(left_offset + 375, 25, f"Version: {version_name}    Page: {page_number}")
            c.showPage()
            page_number += 1
            y_position = page_start_y

    c.save()
    print(f"PDF generated: {output_filename}")


if __name__ == "__main__":
    generate_exam_pdf("questions.json", "exam_version_A.pdf", version_name="A")
    generate_exam_pdf("questions.json", "exam_version_B.pdf", version_name="B")
    generate_exam_pdf("questions.json", "exam_version_A_solved.pdf", solved=True, version_name="A")
    generate_exam_pdf("questions.json", "exam_version_B_solved.pdf", solved=True, version_name="B")
