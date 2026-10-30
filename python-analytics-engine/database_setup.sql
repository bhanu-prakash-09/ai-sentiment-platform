-- Create Database for Sentiment Platform
CREATE DATABASE IF NOT EXISTS sentiment_db;
USE sentiment_db;

-- Create Table to Store Processed Customer Reviews
CREATE TABLE IF NOT EXISTS customer_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    review_text TEXT NOT NULL,
    sentiment_result VARCHAR(20) NOT NULL,
    confidence_score INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert Sample Processed Data for Testing
INSERT INTO customer_reviews (customer_name, review_text, sentiment_result, confidence_score) VALUES
('Ananya', 'I absolutely love this product! It works flawlessly and saved me hours.', 'Positive', 2),
('Rahul', 'The app keeps crashing on launch. Terrible experience, do not buy.', 'Negative', 2),
('Bhanu', 'It is okay. It gets the job done but the delivery took a bit too long.', 'Neutral', 0);

