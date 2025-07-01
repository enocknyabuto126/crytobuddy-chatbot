#!/usr/bin/env python3
"""
CryptoBuddy - Your First AI-Powered Financial Sidekick! 🌟
Week 1 Assignment: Cryptocurrency Advisor Chatbot

A rule-based chatbot that analyzes cryptocurrency data and provides 
investment advice based on profitability and sustainability.
"""

import random

def greet():
    """Return a random greeting from CryptoBuddy."""
    greetings = [
        "Hey there! Let's find you a green and growing crypto! 🌱",
        "Hello! Ready to explore the crypto universe? 🚀",
        "Hi! I'm CryptoBuddy, your friendly crypto sidekick! 💰",
        "Greetings, future crypto millionaire! Let's chat! 💎"
    ]
    return random.choice(greetings)

# Predefined crypto database as specified in the assignment
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

def get_trending_cryptos():
    """Get all cryptocurrencies with rising price trends."""
    return [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]

def get_most_sustainable():
    """Get the most sustainable cryptocurrency."""
    return max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])

def get_profitable():
    """Get profitable cryptos: price_trend = 'rising' and market_cap = 'high'."""
    return [name for name, data in crypto_db.items() 
            if data["price_trend"] == "rising" and data["market_cap"] == "high"]

def get_eco_friendly():
    """Get eco-friendly cryptos: energy_use = 'low' and sustainability_score > 0.7."""
    return [name for name, data in crypto_db.items() 
            if data["energy_use"] == "low" and data["sustainability_score"] > 0.7]

def get_crypto_info(crypto_name):
    """Get detailed information about a specific cryptocurrency."""
    crypto_name = crypto_name.title()
    if crypto_name in crypto_db:
        data = crypto_db[crypto_name]
        return f"""
📊 {crypto_name} Analysis:
   • Price Trend: {data['price_trend'].title()} 📈
   • Market Cap: {data['market_cap'].title()} 💼
   • Energy Use: {data['energy_use'].title()} ⚡
   • Sustainability Score: {data['sustainability_score']}/10 🌱
        """
    return f"Sorry, I don't have data for {crypto_name}. 🤔"

def process_query(user_query):
    """Process user query and return appropriate response."""
    query = user_query.lower()
    
    # Greeting patterns
    if any(word in query for word in ["hello", "hi", "hey", "greetings"]):
        return greet()
    
    # Trending cryptos
    if any(phrase in query for phrase in ["trending", "trending up", "going up", "rising"]):
        trending = get_trending_cryptos()
        if trending:
            return f"🚀 Currently trending up: {', '.join(trending)}! These cryptos are on the move!"
        else:
            return "📉 No cryptos are currently trending up. Market might be in a consolidation phase."
    
    # Sustainable cryptos
    if any(word in query for word in ["sustainable", "eco", "green", "environment"]):
        eco = get_eco_friendly()
        if eco:
            return f"🌱 Most sustainable cryptos: {', '.join(eco)}! These are eco-friendly choices!"
        else:
            return "🌍 All cryptos have some environmental impact, but some are greener than others."
    
    # Most sustainable
    if "most sustainable" in query:
        recommend = get_most_sustainable()
        return f"🌱 {recommend} is the most sustainable with a score of {crypto_db[recommend]['sustainability_score']}/10! Invest in {recommend}! 🌱 It's eco-friendly and has long-term potential!"
    
    # Long-term investment
    if any(phrase in query for phrase in ["long term", "long-term", "longterm", "hold", "hodl", "growth"]):
        recommend = get_most_sustainable()
        return f"💎 For long-term growth, I'd recommend {recommend}! {recommend} is trending up and has a top-tier sustainability score! 🚀"
    
    # Short-term investment
    if any(phrase in query for phrase in ["short term", "short-term", "quick", "fast"]):
        profitable = get_profitable()
        if profitable:
            return f"⚡ For short-term gains, {profitable[0]} is trending up! But remember, timing is everything! ⏰"
        else:
            return "📊 Check the current market conditions for short-term opportunities!"
    
    # Profitable cryptos
    if any(word in query for word in ["profitable", "profit", "money", "gains"]):
        profitable = get_profitable()
        if profitable:
            return f"💰 Most profitable cryptos (high cap + rising): {', '.join(profitable)}! 💰"
        else:
            return "📊 Check the current market conditions for profitable opportunities!"
    
    # Eco-friendly cryptos
    if any(phrase in query for phrase in ["eco friendly", "eco-friendly", "low energy", "energy efficient"]):
        eco_friendly = get_eco_friendly()
        if eco_friendly:
            return f"⚡ Eco-friendly cryptos (low energy use): {', '.join(eco_friendly)}! 🌱"
        else:
            return "💡 All cryptos are working on energy efficiency improvements!"
    
    # Specific crypto info
    for crypto in crypto_db.keys():
        if crypto.lower() in query:
            return get_crypto_info(crypto)
    
    # Help
    if any(word in query for word in ["help", "what can you do", "commands"]):
        return """
🤖 I can help you with:
   • "Which crypto is trending up?" 📈
   • "What's the most sustainable coin?" 🌱
   • "Recommend for long-term growth" 💎
   • "Show me profitable cryptos" 💰
   • "Tell me about Bitcoin" 📊
   • "Eco-friendly options" ⚡
   • "Help" - Show this menu

Just ask me anything about crypto! 🚀
        """
    
    # Default response
    return "🤔 I'm not sure about that! Try asking me about trending cryptos, sustainability, or specific coins. Type 'help' for more options!"

def main():
    """Main function to run the CryptoBuddy chatbot."""
    print("=" * 60)
    print("🌟 Welcome to CryptoBuddy - Your First AI-Powered Financial Sidekick! 🌟")
    print("=" * 60)
    print(greet())
    print("\n⚠️  DISCLAIMER: Crypto is risky—always do your own research! This is not financial advice. ⚠️")
    print("\nType 'quit' or 'exit' to end the conversation.")
    print("Type 'help' to see what I can do!")
    print("-" * 60)
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\nCryptoBuddy: Thanks for chatting! Remember to DYOR (Do Your Own Research)! 👋")
                break
            
            if not user_input:
                continue
            
            response = process_query(user_input)
            print(f"\nCryptoBuddy: {response}")
            
        except KeyboardInterrupt:
            print("\n\nCryptoBuddy: Oops! You interrupted me. Thanks for chatting! 👋")
            break
        except Exception as e:
            print(f"\nCryptoBuddy: Oops! Something went wrong: {e}. Let's try again!")

if __name__ == "__main__":
    main()
