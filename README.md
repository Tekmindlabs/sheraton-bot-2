# Chatbot with RAG-Enabled Chat Endpoint from [Cohere AI](https://cohere.com/)  

### Overview

Welcome to the Chatbot with RAG-Enabled Cohere AI Chat Endpoint project! In this project, I explore the implementation of Cohere's RAG-enabled chat endpoint to create intelligent and context-aware chat applications. This readme provides an in-depth guide on how to set up and utilize the chatbot, explaining each step and decision made along the way.

### Project Description

#### 1. **Introduction:**
I embarked on this project with the goal of leveraging Cohere's cutting-edge RAG-enabled chat endpoint. This endpoint simplifies the creation of powerful and informative chatbots by incorporating Retrieval-Augmented Generation (RAG) functionality. The chatbot developed here focuses on providing information and handling inquiries related to a hotel, specifically tailored for Sheraton Hotel.

#### 2. **Setting Up the Environment:**
The project begins with setting up the necessary environment, including installing dependencies and obtaining the API key from Cohere.AI. Detailed instructions are provided on how to initialize the environment and configure the necessary files.

#### 3. **Custom Knowledge Base and Prompt Template:**
I have created a custom knowledge base for the chatbot, specifying a format for the documents without relying on external databases. Additionally, a custom prompt template was designed to guide the chatbot's behavior, ensuring it adheres to the context and provides relevant responses.

#### 4. **Chat Functionalities and Cohere Integration:**
The core of the project involves interfacing with Cohere's RAG-enabled chat endpoint. I explain how to send user prompts to the chat endpoint and handle the responses effectively. The readme outlines different modes available in Cohere's chat endpoint, such as Document Mode, Query Generation Mode, and Connector Mode, allowing users to choose the mode that best fits their needs.

#### 5. **Special Handling for Booking Confirmation:**
A unique feature of the chatbot is its ability to summarize conversations and display detailed summaries, especially when confirming hotel bookings. I delve into the code responsible for generating and displaying these summaries, enhancing the user experience.

#### 6. **User Interface and Deployment:**
The readme guides users on how to design the chatbot's user interface using Streamlit, explaining the callback functions and the overall structure of the interface. Additionally, instructions on deploying the chatbot using Streamlit Cloud are provided.

### Project Files and Structure

The project files are organized as follows:

- **`main.py`**: The main Python file containing the chatbot's logic and user interface implemented using Streamlit.
- **`static/styles.css`**: Custom CSS file for styling the chatbot interface.
- **`.streamlit/config.toml`**: Configuration file enabling static serving and allowing customization of the Streamlit app.

### How to Use This Project

1. **Setting Up the Environment:**
   - Clone the repository to your local machine.
   - Install the required dependencies using `pip install -r requirements.txt`.
   - Create a `.streamlit` folder and add your Cohere API key in the `secrets.toml` file.

2. **Running the Chatbot:**
   - Execute the command `streamlit run main.py` to launch the chatbot locally.
   - Interact with the chatbot by entering prompts in the provided input field and clicking the "Ask" button.

3. **Customizing the Chatbot:**
   - Modify the chatbot's behavior by adjusting the custom prompt template and knowledge base documents in the code.

4. **Deployment:**
   - Deploy the chatbot to Streamlit Cloud or any other preferred hosting platform for wider accessibility.

### Conclusion

This project demonstrates the potential of Cohere's new chat endpoint and provides a foundation for building intelligent and context-aware chat applications. The provided code, explanations, and customization options offer a comprehensive guide for developers interested in creating sophisticated chatbots using Cohere's RAG functionality.

Feel free to explore the code, experiment with customizations, and reach out for any questions or suggestions for improvement. Happy coding!

---

**Author:** Aniz B N  
**GitHub Repository:** [hotel-booking-bot](https://github.com/4N1Z/hotel-coChat-Cohere)  
**Live Deployment:** [sheraton-bot-2](https://your-live-deployment-url.com)

For inquiries and feedback, please contact me at [aniz.bn14@gmail.com](mailto:aniz.bn14@gmail.com]).