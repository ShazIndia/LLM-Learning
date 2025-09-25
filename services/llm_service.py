import openai
import json
from typing import Dict, Any
import os
from dotenv import load_dotenv

load_dotenv()

class LLMService:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI()
    
    def generate_troubleshooting_response(self, problem_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate troubleshooting solutions using OpenAI GPT
        """
        prompt = self._create_prompt(problem_data)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system", 
                        "content": "You are a helpful technical support specialist. Provide step-by-step troubleshooting solutions in JSON format."
                    },
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500,
                temperature=0.7
            )
            
            # Parse the response
            content = response.choices[0].message.content
            return self._parse_llm_response(content)
            
        except Exception as e:
            return self._create_fallback_response(str(e))
    
    def _create_prompt(self, problem_data: Dict[str, Any]) -> str:
        """Create a structured prompt for the LLM"""
        prompt = f"""
        Please provide troubleshooting solutions for the following problem:

        Problem Description: {problem_data['problem_description']}
        Category: {problem_data['category']}
        Urgency: {problem_data['urgency']}
        Additional Context: {problem_data.get('additional_context', 'None provided')}

        Please respond with a JSON object containing:
        1. problem_summary: A brief summary of the issue
        2. solutions: An array of step-by-step solutions, each with:
           - step: number
           - description: detailed step description
           - estimated_time: approximate time needed
        3. confidence_score: How confident you are in the solution (0.0-1.0)
        4. additional_resources: Array of helpful links or resources
        5. estimated_total_time: Total estimated time for all solutions

        Provide 3-5 practical solutions ordered by likelihood of success.
        """
        return prompt
    
    def _parse_llm_response(self, content: str) -> Dict[str, Any]:
        """Parse and validate LLM response"""
        try:
            # Try to extract JSON from the response
            start_idx = content.find('{')
            end_idx = content.rfind('}') + 1
            
            if start_idx != -1 and end_idx != 0:
                json_str = content[start_idx:end_idx]
                return json.loads(json_str)
            else:
                # Fallback: create structured response from text
                return self._create_text_fallback(content)
                
        except json.JSONDecodeError:
            return self._create_text_fallback(content)
    
    def _create_text_fallback(self, content: str) -> Dict[str, Any]:
        """Create a fallback response when JSON parsing fails"""
        lines = content.strip().split('\n')
        solutions = []
        
        for i, line in enumerate(lines[:5], 1):
            if line.strip():
                solutions.append({
                    "step": i,
                    "description": line.strip(),
                    "estimated_time": "5-10 minutes"
                })
        
        return {
            "problem_summary": "Troubleshooting assistance provided",
            "solutions": solutions,
            "confidence_score": 0.7,
            "additional_resources": ["https://docs.python.org", "https://stackoverflow.com"],
            "estimated_total_time": "30-60 minutes"
        }
    
    def _create_fallback_response(self, error_msg: str) -> Dict[str, Any]:
        """Create a fallback response when LLM service fails"""
        return {
            "problem_summary": "Unable to generate automated solution",
            "solutions": [
                {
                    "step": 1,
                    "description": "Check system logs for error messages",
                    "estimated_time": "5 minutes"
                },
                {
                    "step": 2,
                    "description": "Restart the affected service or application",
                    "estimated_time": "2 minutes"
                },
                {
                    "step": 3,
                    "description": "Contact technical support with detailed error information",
                    "estimated_time": "Variable"
                }
            ],
            "confidence_score": 0.3,
            "additional_resources": ["https://support.example.com"],
            "estimated_total_time": "15-30 minutes"
        }
