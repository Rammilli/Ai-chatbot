import logging
import sys

from .agent import ask_question

# Configure a clean console logger for the CLI wrapper
logging.basicConfig(
    level=logging.WARNING, # Suppress most underlying LangChain debug spam 
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)
# Enable INFO level just for communicating with the interactive user
logger.setLevel(logging.INFO)

def run_cli_loop():
    """
    Run an interactive command-line loop allowing the user to repeatedly
    ask questions to the RAG agent.
    
    The loop runs indefinitely until the user types 'exit' or 'quit'.
    """
    print("=" * 60)
    print("🤖 Welcome to the RAG AI Chatbot!")
    print("Type 'exit' or 'quit' at any time to end the session.")
    print("=" * 60)
    print()
    
    while True:
        try:
            # Prompt the user for a question
            user_input = input("You: ").strip()
            
            # Handle empty inputs gracefully
            if not user_input:
                continue
                
            # Exit conditions
            if user_input.lower() in ("exit", "quit"):
                print("\n👋 Goodbye!")
                break
                
            print("\nThinking...")
            
            # Query the backend agent
            result = ask_question(user_input)
            
            # Handle failures safely without breaking the loop
            if result is None:
                logger.error(
                    "The agent failed to process your request. "
                    "Ensure the vector database exists and APIs are configured."
                )
                print("-" * 60 + "\n")
                continue
                
            answer = result.get("answer", "No answer generated.")
            sources = result.get("sources", [])
            
            # Print the AI response
            print(f"\n💡 AI: {answer}")
            
            print("\n📚 Sources Metadata:")
            if sources:
                # Iterate and cleanly print out the parsed metadata dictionaries 
                # returned explicitly from our agent's new logic.
                for idx, source_meta in enumerate(sources, start=1):
                    # We print the raw source metadata cleanly formatted
                    print(f"  [{idx}] {source_meta}")
            else:
                print("  No contextual sources accessed.")
                
            print("\n" + "-" * 60 + "\n")
                
        # Catch KeyboardInterrupt (Ctrl+C) to exit cleanly rather than stack tracing
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")
            print("-" * 60 + "\n")

if __name__ == "__main__":
    run_cli_loop()
