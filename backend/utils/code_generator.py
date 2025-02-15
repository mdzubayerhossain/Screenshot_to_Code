from groq import Groq
import os
import logging

# Set up logging
logger = logging.getLogger(__name__)

def get_groq_client():
    """Initialize and return Groq client with API key validation"""
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        logger.error("GROQ_API_KEY environment variable not set")
        raise ValueError("API key missing. Please set GROQ_API_KEY environment variable")
    
    try:
        return Groq(api_key=api_key)
    except Exception as e:
        logger.error(f"Failed to initialize Groq client: {str(e)}")
        raise

def generate_code(text, framework="react"):
    """Generate code using Groq API based on extracted text"""
    try:
        client = get_groq_client()
    except Exception as e:
        return f"Error initializing API client: {str(e)}"

    prompt = f"""
    Generate clean, modern {framework} code based on this UI description:
    {text}
    
    Requirements:
    1. Use proper semantic HTML/JSX structure
    2. Include Tailwind CSS classes for styling
    3. Add necessary JavaScript/React functionality
    4. Format as plain code without markdown
    5. Include all required imports
    
    Return only the code with comments explaining key sections.
    """
    
    try:
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{
                "role": "user",
                "content": prompt
            }],
            temperature=0.7,
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"API request failed: {str(e)}")
        return f"Code generation failed: {str(e)}"