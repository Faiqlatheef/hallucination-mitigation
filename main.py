from grounded_generation import grounded_generation
from prompt_engineering import construct_prompt
from utils import call_openai_api
from fact_verification import extract_factual_statements, verify_facts
from output_calibration import calibrate_output

def process_prompt(user_prompt):
    # Step 1: Grounded Generation
    retrieved_info = grounded_generation(user_prompt)
    
    # Step 2: Prompt Engineering
    prompt = construct_prompt(user_prompt, retrieved_info)
    
    # Step 3: Generate Response from LLM
    llm_response = call_openai_api(prompt)
    
    # Step 4: Fact Verification
    statements = extract_factual_statements(llm_response)
    verified_statements = verify_facts(statements)
    
    # Step 5: Output Calibration
    final_output = calibrate_output(verified_statements)
    
    return final_output

if __name__ == "__main__":
    # Example prompts for testing
    test_prompts = [
        "What is the capital of France?",
        "Explain the theory of relativity.",
        "Who is the current president of Mars?"  # Intentionally ambiguous/non-existent
    ]
    
    for prompt in test_prompts:
        print(f"User Prompt: {prompt}")
        response = process_prompt(prompt)
        print("AI Response:")
        print(response)
        print("-" * 50)
