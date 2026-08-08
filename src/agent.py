import os

from dotenv import load_dotenv
from openai import OpenAI


# Load the API key from the .env file
load_dotenv()

# Create the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run_agent():
    """Run the basic AI Agent."""

    print("=" * 40)
    print("          BASIC AI AGENT")
    print("=" * 40)
    print("Type 'exit' to stop the agent.")
    print()

    while True:
        user_input = input("You: ")

        # Stop the program when the user types exit
        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break

        # Ignore empty input
        if not user_input.strip():
            print("Agent: Please enter a question.")
            continue

        try:
            # Send the user's message to the AI model
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=user_input
            )

            # Display the AI response
            print("Agent:", response.output_text)
            print()

        except Exception as error:
            print("Agent: An error occurred.")
            print("Details:", error)
            print()


# Start the agent
if __name__ == "__main__":
    run_agent()