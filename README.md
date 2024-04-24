# Migration Analysis
Link to the prototype:- [Chat-Bot-Prototype](https://migrationanalysis.zapier.app/chat)

User Guide for Migration Assistant Chatbot:

Welcome to the Migration Assistant chatbot! This chatbot is designed to help you find the perfect destination to move to based on the latest semantic data and global socio-economic trends. Here's how you can use the chatbot effectively:

1. Open the chatbot interface in your web browser.
2. Type your message or query in the input field provided. Be as specific as possible about your preferences, such as your country of origin, age group, gender, and any other relevant information.
3. Click the "Send" button to submit your message to the chatbot.
4. The chatbot will analyze your input and extract the necessary details to provide a personalized response.
5. If the chatbot requires additional information to generate an accurate response, it will prompt you with specific questions. Please provide the requested information to help the chatbot better understand your needs.
6. Once the chatbot has gathered all the required information, it will provide a response in a structured format, including your country of origin, age group, gender, preferred destination country, and general remarks summarizing your request.
7. You can continue the conversation with the chatbot by typing additional messages or queries in the input field.
8. If you want to start a new conversation or clear the chat history, you can refresh the page.

Remember, the more specific and detailed your input is, the better the chatbot can assist you in finding the perfect destination for your move. Happy exploring with the Migration Assistant chatbot!

---

README for the Chatbot Code:

# Global Migration Analysis Chatbot

This repository contains the code for a Global Migration Analysis Chatbot implemented using Streamlit and OpenAI's GPT-3.5-turbo model. The chatbot assists users in analyzing global migration data and provides personalized recommendations based on user input.

## Features

- Interactive chat interface for user input and chatbot responses
- Integration with OpenAI's GPT-3.5-turbo model for generating chatbot responses
- Extraction of specific details from user input, including country of origin, age group, gender, preferred destination country, and general remarks
- Structured response format using a dictionary
- Graph visualization based on user queries (placeholder implementation)

## Prerequisites

- Python 3.x
- Streamlit
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/global-migration-analysis-chatbot.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Replace `"your-api-key"` in the code with your actual OpenAI API key.

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Access the chatbot interface in your web browser at `http://localhost:8501`.

3. Type your message or query in the input field and click the "Send" button to interact with the chatbot.

4. The chatbot will analyze your input, extract relevant details, and provide a personalized response in a structured format.

5. If the chatbot requires additional information, it will prompt you with specific questions. Provide the requested information to help the chatbot generate an accurate response.

6. The chat history will be displayed in the left column, and a placeholder graph visualization will be shown in the right column.

7. To start a new conversation or clear the chat history, refresh the page.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
