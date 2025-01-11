# NextGenFirewall: Cloud Security Using Data Mining  

## Overview  
This repository contains an end-to-end implementation of a next-generation firewall for cloud security. The project uses advanced data mining techniques and machine learning models to detect and mitigate modern cybersecurity threats, including malware, DDoS attacks, and insider threats.  

## Key Features  
- **Dataset**: Utilizes the UNSW-NB15 dataset, a comprehensive collection of real and synthetic network activities for cybersecurity research.  
- **Machine Learning Models**: Comparative analysis of multiple models, including Random Forests, Gradient Boosting, SVM, and Naive Bayes, for optimal threat detection.  
- **Evaluation Metrics**: Rigorous evaluation using metrics like accuracy, precision, recall, F1 score, and ROC-AUC.  
- **End-to-End System Integration**: Includes a decision simulator for real-time threat detection and visualization using Flask and Streamlit.  

## Tools and Technologies  
- **Programming Language**: Python  
- **Libraries**: Pandas, NumPy, Scikit-learn, Flask, Streamlit  
- **Environment**: Google Colab for training models with GPU support  
- **IDE**: VS Code for seamless integration of backend and frontend  

## Methodology  
1. **Data Preparation and Cleaning**  
   - Removed irrelevant data points, handled missing values, and corrected errors.  

2. **Feature Engineering and Selection**  
   - Extracted and selected impactful features using mutual information and feature importance metrics.  

3. **Model Training and Evaluation**  
   - Trained models on the UNSW-NB15 dataset and evaluated using metrics like ROC-AUC and F1 score.  

4. **System Integration**  
   - Integrated the best-performing model into a decision simulator for real-time threat detection.  

## Dataset  
- **Source**: UNSW-NB15-GT.csv  
- **Description**: Contains 49 features representing real and synthetic network traffic, including benign and malicious activities.  

## Results  
- **Best Model**: Random Forest achieved an accuracy of 90.92% and ROC-AUC of 0.9830.  
- **System**: Demonstrated enhanced detection of network threats with robust scalability for cloud environments. 
