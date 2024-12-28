# Install Google's Generative AI library
# pip install google-generativeai

# Install abseil-py for logging management
# pip install absl-py

import google.generativeai as genai
import os
import absl.logging
import logging

# Configure the API key
GOOGLE_API_KEY = "INSERT API KEY HERE"
genai.configure(api_key=GOOGLE_API_KEY)

# Add this line before configuring the API key
absl.logging.set_verbosity(absl.logging.ERROR)
logging.getLogger('absl').setLevel(logging.ERROR)

def analyze_products(product_list):
    # Using Gemini-Pro model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Craft the prompt
    prompt = f"""
    Analyze these products and recommend which ones have the best potential for affiliate marketing based on:
    1. Current market trends
    2. Commission rates
    3. Product popularity
    4. Price point
    5. Potential ROI
    (Don't just pick the product with the highest commission, unless if it already has the most potential)

    For each recommended product, provide:
    - Product name
    - Commission amount
    - Commission rate
    - Brief reason for recommendation
    
    Here are the products:
    {product_list}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Welcome to AffiliateBot!")
    print("Please paste your product list,(press Ctrl+D or Ctrl+Z when finished):")
    
    # Collect input until EOF
    try:
        product_list = ""
        while True:
            line = input()
            product_list += line + "\n"
    except EOFError:
        pass
    
    print("\nAnalyzing products...\n")
    analysis = analyze_products(product_list)
    print(analysis)

if __name__ == "__main__":
    main()
