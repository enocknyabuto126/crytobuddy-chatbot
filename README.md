# CryptoBuddy - Your First AI-Powered Financial Sidekick! 🌟

## Week 1 Assignment: Cryptocurrency Advisor Chatbot

A rule-based chatbot that analyzes cryptocurrency data and provides investment advice based on **profitability** (e.g., price trends) and **sustainability** (e.g., energy efficiency, project viability).

## 🎯 What You'll Learn

✅ Basics of AI-driven decision-making  
✅ How to design conversational logic  
✅ Simple data analysis for crypto trends  
✅ Rule-based chatbot development  

## 🚀 Features

### 🤖 Chatbot Personality
- **Name**: CryptoBuddy
- **Tone**: Friendly and professional with emoji flair
- **Personality**: Helpful crypto advisor with a sense of humor

### 📊 Predefined Crypto Database
The chatbot includes data for 3 major cryptocurrencies as specified in the assignment:
- **Bitcoin** - The original cryptocurrency, digital gold
- **Ethereum** - Smart contract platform, foundation of DeFi  
- **Cardano** - Academic approach to blockchain, proof-of-stake

Each crypto includes:
- Price trend (rising/stable/falling)
- Market cap (high/medium/low)
- Energy use (high/medium/low)
- Sustainability score (1-10)

### 💡 Investment Advice Rules

#### Profitability Analysis
- Prioritizes coins with `price_trend = "rising"` and `market_cap = "high"`
- Identifies trending cryptocurrencies
- Recommends based on market performance

#### Sustainability Analysis
- Prioritizes coins with `energy_use = "low"` and `sustainability_score > 7/10`
- Identifies eco-friendly options
- Considers long-term viability

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.6 or higher
- No additional libraries required (uses only built-in Python modules)

### Running the Chatbot

1. **Download the project files**
2. **Navigate to the project directory**
3. **Run the chatbot**:
   ```bash
   python crypto_advisor_bot.py
   ```

### Example Conversation

```
🌟 Welcome to CryptoBuddy - Your First AI-Powered Financial Sidekick! 🌟
============================================================
Hey there! Let's find you a green and growing crypto! 🌱

⚠️  DISCLAIMER: Crypto is risky—always do your own research! This is not financial advice. ⚠️

Type 'quit' or 'exit' to end the conversation.
Type 'help' to see what I can do!
------------------------------------------------------------

You: Which crypto is trending up?
CryptoBuddy: 🚀 Currently trending up: Bitcoin, Cardano! These cryptos are on the move!

You: What's the most sustainable coin?
CryptoBuddy: 🌱 Cardano is the most sustainable with a score of 8/10! Invest in Cardano! 🌱 It's eco-friendly and has long-term potential!

You: Which crypto should I buy for long-term growth?
CryptoBuddy: 💎 For long-term growth, I'd recommend Cardano! Cardano is trending up and has a top-tier sustainability score! 🚀

You: Tell me about Bitcoin
CryptoBuddy: 📊 Bitcoin Analysis:
   • Price Trend: Rising 📈
   • Market Cap: High 💼
   • Energy Use: High ⚡
   • Sustainability Score: 3/10 🌱
```

## 🎮 Available Commands

The chatbot understands natural language queries. Try these examples:

### 📈 Market Analysis
- "Which crypto is trending up?"
- "Show me profitable cryptos"
- "What's the market like?"

### 🌱 Sustainability Focus
- "What's the most sustainable coin?"
- "Show me eco-friendly options"
- "Which cryptos are green?"

### 💰 Investment Advice
- "Which crypto should I buy for long-term growth?"
- "What should I buy for short-term gains?"
- "Which crypto should I hold?"

### 📊 Specific Information
- "Tell me about Bitcoin"
- "What's Ethereum like?"
- "Cardano analysis"

### 🆘 Help & Navigation
- "Help" - Show available commands
- "What can you do?" - List features
- "quit" or "exit" - End conversation

## 🔧 Technical Implementation

### Core Components

1. **Predefined Database**: Hardcoded crypto data as specified in assignment
2. **Rule-based Logic**: If-else statements for query processing
3. **Natural Language Processing**: Simple keyword matching for user queries
4. **Recommendation Engine**: Algorithms for different investment strategies

### Key Functions

- `greet()`: Random friendly greetings
- `get_trending_cryptos()`: Find trending cryptocurrencies
- `get_most_sustainable()`: Find most sustainable crypto
- `get_profitable()`: Find profitable cryptos (high cap + rising)
- `get_eco_friendly()`: Find eco-friendly options
- `process_query()`: Main query processing logic
- `get_crypto_info()`: Detailed crypto analysis

## 🎯 Assignment Requirements Met

✅ **Rule-based chatbot** using if-else logic  
✅ **Cryptocurrency data analysis** for trends and sustainability  
✅ **Investment advice** based on profitability and sustainability  
✅ **Conversational interface** with natural language processing  
✅ **Predefined dataset** as specified in assignment  
✅ **Ethics disclaimer** about crypto risks  
✅ **Friendly personality** with emoji and engaging responses  

## 🚀 Stretch Goals (Future Enhancements)

- **API Integration**: Pull real-time data using CoinGecko's free API
- **NLP Enhancement**: Use NLTK for more natural language queries
- **Machine Learning**: Add sentiment analysis and trend prediction
- **Web Interface**: Create a web-based chatbot interface
- **Database Integration**: Store conversation history and user preferences

## ⚠️ Important Disclaimer

**This is an educational project for learning purposes only. The chatbot provides simulated advice based on predefined data. Cryptocurrency investments carry significant risks, and you should always:**

- Do your own research (DYOR)
- Consult with financial advisors
- Never invest more than you can afford to lose
- Understand that past performance doesn't guarantee future results

## 📝 License

This project is created for educational purposes as part of a Week 1 assignment.

---

**Happy coding and happy learning! 🚀💻**
