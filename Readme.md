# Talent Scout - AI-Powered Hiring Assistant
## Project Overview
Talent Scout is a conversational AI-based hiring assistant designed to streamline the recruitment process. Built using Streamlit and Google’s Generative AI, the chatbot guides users through a step-by-step interview process, collecting information about their skills, experience, and preferences. It dynamically generates additional questions and evaluates candidates based on their responses, providing insights for recruiters.

Installation Instructions
Clone the Repository

```bash
git clone https://github.com/your-repo/talent-scout.git
cd talent-scout
```
Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install Required Dependencies

```bash
pip install -r requirements.txt
```
Add API Keys

- Create a .env file in the project root directory.
- Add your Google API Key:
- GOOGLE_API_KEY=your_google_api_key_here
* Run the Application

```bash
streamlit run test.py
```
Access the App

- Open your browser and navigate to http://localhost:8501.


## Usage Guide
Launching the App
After running the app, you'll be greeted with a welcome message and guided through a series of questions.

# Step-by-Step Information Gathering

Enter details like your 
- full name
- email
- years of experience
- technical skills.

Respond to dynamically generated questions crafted by the AI model.

### Candidate Evaluation

Once all questions are answered, the assistant evaluates your responses using predefined criteria.
Recruiters can access the insights to make informed decisions.
## Technical Details
### Libraries Used

#### Streamlit
- Frontend framework for interactive web apps.
#### google.generativeai 
- API for generating questions and evaluations.
#### dotenv 
- Manages environment variables securely.
### Model Details

Utilizes Google's Generative AI (Gemini-pro) for generating content and evaluating candidates.
### Architectural Decisions
![Chatbot Workflow](project_flow/pgagi.drawio.png)

Modular design with an Agents class to encapsulate API interactions.
Session management using st.session_state for seamless user experience.
### Prompt Design
#### Information Gathering
Prompts are designed to elicit precise and structured responses. For example:

- Prompt for name: "What is your full name?"
- Prompt for skills: "What is your tech stack (e.g., Python, Django, SQL)?"
#### Dynamic Question Generation

##### Prompt Design for Question Generation
Our approach to crafting questions is systematic and hierarchical, ensuring a smooth progression in difficulty while analyzing the candidate's expertise. Here's the step-by-step methodology

##### 1. Necessity Question
The first question focuses on the core, essential knowledge of the candidate's stated tech stack. This ensures we establish a baseline understanding of their fundamental knowledge.
Example: "Can you explain the difference between Python lists and tuples?"

##### 2. Progressively Tougher Questions
The next four questions increase in complexity, gradually testing the candidate's problem-solving skills, application of knowledge, and deep understanding of concepts.

- Question 2 (Slightly Tougher): Introduce situational or real-world use cases to test applied knowledge.
  - Example: "How would you optimize a Python program that processes a list of 10 million items?"

- Question 3 (Intermediate): Explore technical depth by requiring a more detailed response.
  - Example: "Explain how Python's GIL (Global Interpreter Lock) impacts multi-threading, and how can it be mitigated?"

- Question 4 (Advanced): Test theoretical understanding and ability to deal with edge cases.
  - Example: "What challenges would you face when integrating Python libraries like NumPy with C++ code, and how would you address them?"

- Question 5 (Expert-Level): Evaluate creativity and mastery by posing an open-ended question that requires a solution-oriented mindset.
  - Example: "Design an API in Python that supports asynchronous requests for real-time data fetching and briefly outline the architecture."
  
### Evaluation
#### Candidate Evaluation Process

Our scoring system evaluates candidates systematically by analyzing their responses to progressively challenging questions. Below is the structured approach used:

##### 1. Necessity Question Assessment
- The **first question** is designed to test the candidate's essential knowledge relevant to their provided tech stack.
- **Scoring Rule**:
  - If the candidate answers the necessity question correctly:
    - They are awarded a score of `1`.
    - The system proceeds to the next set of questions.
  - If the candidate answers incorrectly:
    - They are deemed unsuitable for the role based on their details.
    - The evaluation process terminates.

##### 2. Progressive Question Evaluation
- After the necessity question, the candidate is presented with **four additional questions** of increasing difficulty.
- **Scoring Rule**:
  - For each **correct answer**:
    - A `0` is appended to the candidate's existing score, reflecting incremental competence.
  - For each **incorrect answer**:
    - No changes are made to the score.
    - The system skips to the next question.

##### 3. Final Evaluation
- At the end of the process, the final score reflects the candidate's performance, with emphasis on their ability to answer both basic and progressively harder questions correctly.

##### Example Scoring Scenario
- Candidate answers the necessity question correctly → Score: 1.
- Candidate answers the second question correctly → Score: 10.
- Candidate answers the third question incorrectly → Score remains 10 (skip to the next).
- Candidate answers the fourth question correctly → Score: 100.
- Candidate answers the fifth question incorrectly → Final Score: 100.

This structured approach ensures a fair and progressive evaluation of the candidate’s expertise while aligning with the requirements of the role.


### Challenges & Solutions
#### Session State Management

##### Challenge 
- Ensuring the chatbot flow remained consistent during user interactions.
##### Solution 
- Used st.session_state to persist chat history, user data, and flow stages.
#### Dynamic Question Parsing:

##### Challenge 
- Handling JSON parsing issues with AI-generated questions.
##### Solution 
- Implemented error handling to validate and parse JSON safely.
#### Prompt Engineering

##### Challenge 
- Crafting effective prompts for diverse user inputs.
##### Solution 
- Iterated on prompts to balance specificity and adaptability for varied responses.
