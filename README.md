# ENIGUARD 
# "Empowering Real-Time Defense with AI"
SMARTSHIELD:  AI-Driven Cybersecurity Incident Response Automation

The SMARTSHIELD project introduces an AI-driven solution to detect and mitigate Distributed Denial of Service (DDoS) attacks automatically. 
Using the CatBoost classification model, this solution integrates effectively within an existing cybersecurity infrastructure to enhance resilience, detection accuracy, and operational efficiency.

# Problem Description
DDoS attacks pose a rising threat to service availability, causing major financial losses for organizations. Current defenses are limited: on-premise solutions can’t handle large-scale attacks, and automated detection is costly and resource-intensive, struggling with prolonged attacks. ENIGUARD overcomes these issues with a powerful, automated response system for effective DDoS detection and mitigation.

# Problem Implementation 
This solution uses a supervised machine learning framework with the CatBoost algorithm to improve DDoS detection. Trained as a classification model, CatBoost distinguishes between normal traffic and malicious activity, making it well-suited for identifying DDoS attack patterns.
The model configuration is tuned to maximize detection accuracy and F1 score.

# Methodology for Each Step 
### Step 1: Model Preparation
1. **Data Loading and Exploration**: The dataset is imported with Pandas, and exploratory analysis is conducted to understand the structure and identify any anomalies.
2. **Preprocessing**: Numerical data is normalized, and categorical variables are encoded for compatibility.
3. **Model Creation**: CatBoost is selected for its accuracy and effective handling of categorical data. Parameters are optimized for DDoS detection.
4. **Training and Validation**: The model is trained and fine-tuned to maximize precision and recall.
5. **Evaluation**: Metrics like Accuracy and F1 Score confirm CatBoost’s effectiveness.

![image](https://github.com/user-attachments/assets/dac98226-a21a-4677-9e90-819d8dbf9813)

The ROC curve in Figure 1 shows the performance of various models for DDoS detection in SMARTSHIELD:

- **Random Forest (AUC = 1.00)**: Achieved perfect classification with no false positives or negatives, ideal for DDoS detection.
- **Logistic Regression (AUC = 0.99)**: Very high accuracy, closely matching Random Forest's performance.
- **CatBoost (AUC = 0.999)**: Chosen as the primary model for its strong accuracy and ability to minimize misclassifications, making it optimal for SMARTSHIELD.
- **Random Classifier (AUC = 0.50)**: Used as a baseline, showing no distinction between classes.

Overall, Random Forest and CatBoost demonstrate excellent precision, with CatBoost selected for its handling of categorical data and balanced performance, ideal for SMARTSHIELD deployment.

### Step 2: Model Dockerization
- **Deployment**: A Docker setup with a Python script and requirements file enables easy deployment. The model is hosted on Hugging Face, and API functionality is verified with Postman.
- The link of Hugging Face : https://huggingface.co/spaces/yasminerekik/IEEEE_model/tree/main
- Tests of Postman : 
![Capture d'écran 2024-11-06 223543](https://github.com/user-attachments/assets/e58c6296-c9d3-4c08-b68b-d399b121bf84)

![Capture d'écran 2024-11-06 223601](https://github.com/user-attachments/assets/3ebf3fdd-d1e3-4bb0-8a92-2d6e4c9bdfed)

### Step 3: Network Architecture
The network architecture simulates an external attacker attempting to target a client within a local network. All traffic is routed through a pfSense firewall configured with IDS/IPS capabilities using Suricata. The pfSense firewall forwards its logs to a Windows Server, where Splunk SIEM is installed to analyze and visualize network traffic and potential threats.  

![archiyas](https://github.com/user-attachments/assets/3c916fa2-f896-40d2-8692-b8f176d00b56)


### Step 4: Model Integration and Visualization
This network security architecture allows for effective testing and monitoring of DDoS attacks using an integrated firewall and SIEM setup. The configuration enables real-time analysis of traffic through Suricata and log management in Splunk, providing essential insights into network security threats. This setup serves as a foundational model for proactive monitoring and alerting on network-based attacks.

https://github.com/user-attachments/assets/da100cb6-612f-48c0-aaa3-95abf22dd565




