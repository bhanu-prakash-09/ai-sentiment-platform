package com.bhanu.sentimentanalytics;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*") // Allows your HTML frontend dashboard to securely read this API
public class ReviewController {

    @GetMapping("/reviews")
    public List<Map<String, Object>> getProcessedReviews() {
        List<Map<String, Object>> reviews = new ArrayList<>();

        // Review Record 1
        Map<String, Object> r1 = new HashMap<>();
        r1.put("id", 1);
        r1.put("customer", "Ananya");
        r1.put("review_text", "I absolutely love this product! It works flawlessly and saved me hours.");
        r1.put("sentiment", "Positive");
        r1.put("score", 2);
        reviews.add(r1);

        // Review Record 2
        Map<String, Object> r2 = new HashMap<>();
        r2.put("id", 2);
        r2.put("customer", "Rahul");
        r2.put("review_text", "The app keeps crashing on launch. Terrible experience, do not buy.");
        r2.put("sentiment", "Negative");
        r2.put("score", 2);
        reviews.add(r2);

        // Review Record 3
        Map<String, Object> r3 = new HashMap<>();
        r3.put("id", 3);
        r3.put("customer", "Bhanu");
        r3.put("review_text", "It is okay. It gets the job done but the delivery took a bit too long.");
        r3.put("sentiment", "Neutral");
        r3.put("score", 0);
        reviews.add(r3);

        return reviews;
    }
}

