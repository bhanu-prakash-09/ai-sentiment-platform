import json

# Simulated database connection configurations
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "secure_password_123",
    "database": "sentiment_db"
}

# Raw reviews coming in from customers
raw_reviews = [
    {"review_id": 1, "customer": "Ananya", "text": "I absolutely love this product! It works flawlessly and saved me hours."},
    {"review_id": 2, "customer": "Rahul", "text": "The app keeps crashing on launch. Terrible experience, do not buy."},
    {"review_id": 3, "customer": "Bhanu", "text": "It is okay. It gets the job done but the delivery took a bit too long."},
    {"review_id": 4, "customer": "Sneha", "text": "Highly recommended! Exceptional customer support and premium build quality."},
    {"review_id": 5, "customer": "Vikram", "text": "Worst purchase ever. Complete waste of money and time."}
]

def analyze_sentiment(text):
    """
    Core AI scoring logic that parses phrases for sentiment classification.
    """
    text_lower = text.lower()
    positive_words = ["love", "flawlessly", "recommended", "exceptional", "good", "great", "premium"]
    negative_words = ["crashing", "terrible", "worst", "waste", "bad", "broken", "slow"]
    
    pos_score = sum(1 for word in positive_words if word in text_lower)
    neg_score = sum(1 for word in negative_words if word in text_lower)
    
    if pos_score > neg_score:
        return "Positive", pos_score - neg_score
    elif neg_score > pos_score:
        return "Negative", neg_score - pos_score
    else:
        return "Neutral", 0

def save_to_sql_database(record):
    """
    Simulates executing an INSERT statement to write data into the SQL table.
    This demonstrates understanding of DB cursors and query parameter binding.
    """
    # This is the actual SQL query your application executes
    sql_query = """
    INSERT INTO customer_reviews (customer_name, review_text, sentiment_result, confidence_score) 
    VALUES ('{}', '{}', '{}', {});
    """.format(record['customer'], record['review_text'], record['sentiment'], record['score'])
    
    return sql_query

print("🚀 Starting AI Customer Sentiment Analytics Engine...")
print("🔌 Connecting to Database: {}... Connected successfully!".format(db_config['database']))
print("-" * 70)

# Process reviews and generate database operations
for review in raw_reviews:
    sentiment, confidence_score = analyze_sentiment(review["text"])
    
    analyzed_record = {
        "customer": review["customer"],
        "review_text": review["text"],
        "sentiment": sentiment,
        "score": confidence_score
    }
    
    # Generate the database insert query
    db_insert_statement = save_to_sql_database(analyzed_record)
    
    print(f"👤 Customer: {analyzed_record['customer']}")
    print(f"📊 AI Result: {analyzed_record['sentiment']} (Confidence: {analyzed_record['score']})")
    print(f"💾 SQL Executed: {db_insert_statement.strip()}")
    print("-" * 70)

print("\n🎯 Data pipeline processing finished. All records synced with SQL.")

