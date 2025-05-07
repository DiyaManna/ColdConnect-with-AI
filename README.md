# ColdConnect-with-AI
Cold email generator for services company using groq, langchain and streamlit. It allows users to input the URL of a company's careers page. The tool then extracts job listings from that page and generates personalized cold emails. These emails include relevant portfolio links sourced from a vector database, based on the specific job descriptions.

# Imagine a scenario:

A company is actively recruiting for a Manager of Business Development Partnerships, aiming to build sustainable revenue streams through strategic collaborations. While they sift through dozens of applications, hoping to find someone who not only understands partner ecosystems but can also drive actionable growth, time is slipping and the pressure to deliver results builds.

Enter Mentee Consulting—a firm specializing in AI-driven business solutions and strategic partnership management. Instead of waiting for the perfect hire, the company could instantly collaborate with a domain expert who understands the landscape, speaks both English and German fluently, and brings a track record of scaling partner programs across diverse environments.
![Screenshot 2025-05-07 130248](https://github.com/user-attachments/assets/789513bb-c362-486e-b759-bc3254531542)

# Architecture Diagram
![architecture](https://github.com/user-attachments/assets/9fc6e41d-ebee-4c94-986b-5292bb06254f)

# Set-up
1. To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside app/.env update the value of GROQ_API_KEY with the API_KEY you created.

2. To get started, first install the dependencies using:

1. pip install -r requirements.txt
   
3. Run the streamlit app:

streamlit run app/main.py

Copyright (C) Codebasics Inc. All rights reserved.
Additional Terms: This software is licensed under the MIT License. However, commercial use of this software is strictly prohibited without prior written permission from the author. Attribution must be given in all copies or substantial portions of the software.
