# Cosmetics Recommendation System

This project introduces a Cosmetics Recommendation System to simplify skincare product choices amidst a vast market. It utilizes Content-Based Filtering (CBF) to match user preferences like skin type, product categories, and desired effects with a database of skincare products. Using TF-IDF vectorization, it analyzes user profiles and product descriptions to compute cosine similarity, providing personalized recommendations. This approach ensures informed skincare decisions tailored to individual needs, enhancing user satisfaction through effective algorithmic matching.


## Major Contributions to the Project

**1. Data Collection and Preprocessing:**
- Collected cosmetics data from an online retailer.
- Included essential attributes like product type, brand, notable effects, suitable skin types, and price.
- Applied data preprocessing techniques to ensure dataset quality and integrity.

**2. Exploratory Data Analysis (EDA):**
- Conducted in-depth exploration to understand product type distribution, popular brands, notable effects, and suitable skin types.
- Utilized visualizations such as bar graphs, pie charts, and histograms to present key findings and industry trends.

**3. TF-IDF (Term Frequency - Inverse Document Frequency) Vectorization:**
- Utilized TF-IDF vectorization to convert textual data (notable effects descriptions) into numerical representations.
- Captured the importance of words within each notable effects category for meaningful product comparisons.

**4. Cosine Similarity Calculation:**
- Computed cosine similarity based on the TF-IDF matrix to quantify similarity between cosmetics products.
- Identified products with similar notable effects profiles to facilitate personalized recommendations.

**5. Recommendation Generation:**
- Developed a user-friendly website using Streamlit where users can input product names.
- Generated recommendations for skincare products closely matching a given product based on cosine similarity scores.
- Enabled users to interact with the website to retrieve top recommendations based on notable effects similarities.

**6. Deployment and Integration:**
- Deployed the recommendation system as part of an interactive web application using Streamlit.
- Enabled seamless access to personalized recommendations and integration with e-commerce platforms for streamlined purchasing.

## Data Collection and Preprocessing

The dataset utilized in this study comprises comprehensive information about cosmetic products extracted from the Myntra website, specifically from the Myntra HackerRamp 2021 challenge. With a total of 966 products, the dataset serves as a valuable resource for training machine learning models aimed at predicting user preferences and recommending relevant cosmetic products.
The dataset contains eight attributes, each providing essential insights into the characteristics of the products:

![Dataset Description](https://ibb.co/Yyx15Q7)

Upon acquisition of the dataset, rigorous preprocessing procedures were conducted to ensure data quality and integrity. These preprocessing steps included:

**1. Handling Missing Values:** The dataset was carefully examined for any missing values, and appropriate strategies were employed to either impute missing values or remove incomplete observations, ensuring the completeness of the dataset.

**2.  Removing Duplicate Entries:** Due to the nature of data scraping, duplicate entries were identified and subsequently removed to eliminate redundancy and maintain the uniqueness of each product record.

**3. Encoding Categorical Features:** Categorical features such as notable_effects and skintype were encoded into numerical representations using techniques such as one-hot encoding or label encoding. This transformation facilitated the inclusion of categorical data in machine learning models, enabling the extraction of meaningful insights and patterns.

## Exploratory Data Analysis (EDA)

Exploratory data analysis (EDA) covered various aspects of the cosmetics dataset, including brand distribution, product types, skin type suitability, and notable effects. Through visualizations such as bar charts and pie charts, the study provided insights into market presence, product variety, consumer engagement, and product benefits. This comprehensive analysis provided valuable insight into the dynamics of the cosmetics industry and helped understand consumer preferences, market trends and product effectiveness.

**1. Brand Distribution Analysis:** The study examined brand distribution to assess market presence, using bar charts to visualize product count per brand. Top brands were identified based on product count, revealing popularity and variety.

![Brand Distribution Analysis](https://ibb.co/9VN8Hjj)

**2. Product Type Distribution Analysis:** The study examined product type distribution using pie charts, identified dominant types and their proportions, and provided insights into product diversity.

![Product Type Distribution Analysis](https://ibb.co/RB59ch9)

**3. Skin Type Suitability Analysis:** Study of product suitability for different skin types. Bar charts visualize products suitable for each type and identify the predominant objectives. 

![Skin Type Suitability Analysis](https://ibb.co/F6BbMYM)

**4. Analysis of notable effects:** Notable effects associated with cosmetic products were examined using pie charts to reveal the predominant effects of their frequencies.

![Analysis of notable effects](https://ibb.co/84tWm4C)

## Algorithm Overview

**Content-Based Filtering:** Content-based filtering is a recommendation system approach that analyzes the intrinsic characteristics of items to suggest similar items to users based on their preferences. By examining item characteristics such as skin types, notable effects, product type, and product description, the system identifies similarities between items and recommends those that match previous interactions or explicit feedback from the user. Unlike collaborative filtering, content-based filtering is not based on user behavior data and is therefore suitable for scenarios where this data may be limited or unreliable. This approach provides personalized recommendations tailored to individual user preferences, improving user experience and encouraging engagement with recommended items.

![Difference between Collaborative and Content-Based Filtering](https://ibb.co/GCFWNLT)

**TF-IDF (Term Frequency - Inverse Document Frequency) Vectorizer:** TF-IDF Vectorizer is a text feature extraction method that converts a collection of documents into numerical vectors. In this case, notable effects of products are converted into numerical vectors that highlight the importance of terms in each document while taking into account their rarity across the entire data set. The TF-IDF matrix is ​​created, which represents the products and their notable effects. 

**Cosine Similarity:** Cosine similarity is a metric that measures the cosine of the angle between two vectors. The TF-IDF vectors of skin care products are used. Cosine similarity ranges from -1 to 1, with a higher value indicating greater similarity. It calculates how similar the noticeable effects of different skin care products are to each other. Therefore, similar products are recommended.


## Implementation Steps

**1. TF-IDF (Term Frequency - Inverse Document Frequency) Vectorizer Implementation:** The modelling phase of the project focused on implementing the TF-IDF Vectorizer for the recommendation system. This involved using the tfidfvectorizer() function from the sklearn library to perform an IDF calculation on the notable_effects data. The notable_effects data was converted into a matrix form using TF-IDF vectors. 

**TF-IDF Matrix:**

- Rows: Correspond to skin care products. 
- Columns: Represent terms with notable effects. 
- Values: TF-IDF values ​​quantify the importance of terms within each product. 

![TF-IDF](https://ibb.co/SQwGSLN)

**2. Cosine Similarity Calculation:** After TF-IDF transformation, cosine similarity values ​​were calculated to measure the similarity between different notable_effects categories. These ratings served as a quantitative representation of the similarity between pairs of products based on their notable effects.

**Cosine Similarity Matrix:**

- Each row and column correspond to skin care products. 
- Values ​​represent cosine similarity values ​​between pairs of products. 
- Higher values ​​indicate greater similarity for notable effects.

![Cosine Similarity](https://ibb.co/Y0j3X8n)

**3. Recommendation Generation:** Cosine similarity scores were used to generate product recommendations within the recommendation system. The similarity scores formed the basis for identifying products with similar notable_effects and enabled personalized recommendations for users.

![Recommendations Generated](https://ibb.co/S0PkKRR)



## Development of Website Interface

**1. Initialization and Configuration**
- **Streamlit Setup:** Initialize Streamlit and configure page settings such as title, icon and layout.

**2. Sidebar Menu**
- **Menu Configuration:** Create a sidebar menu with options for Home, Get Recommendation, Skin Care Guide, and Contact Us. 
- **Icons and Style:** Use icons for menu items and style the menu for better visual appeal and user experience.

**3. Home Page**
- **Introduction:** Provide an introduction to the application and explain its purpose and functionality.
- **Video display:** Embed a video to give users a visual overview of the application and its features.
- **Information:** Provide information about the skin care products available and encourage users to explore recommendations and skin care tips.

**4. Get Recommendation Page**
- **Input Selection:** Allow users to select their skin type, skin concerns, desired benefits, and brand preference. 
- **Recommendation generation:** Recommend suitable skin care products based on user input using a content-based filtering algorithm. 
- **Interactive Features:** Implement interactive elements such as dropdowns, multi-selects, and buttons for a seamless user experience.

**5. Skincare Guide Page**
- **Skincare Tips:** Present tips and tricks for maximizing the effectiveness of skincare products. 
- **Visuals:** Add images to supplement the information provided and make the content more engaging. 
- **Educational Content:** Educate users on the proper use and benefits of various skin care products and routines.

**6. Contact Page**
- **Contact Information:** View contact information for inquiries and feedback, including email, phone, website and social media links.
- **Accessibility:** Ensure users can easily request help or more information.

## Proposed Architecture

The proposed architecture for the project “Cosmetics Recommendation System” involves building a Python web application using Streamlit that enables users to explicitly select  various product types, skin types, skin problems and notable effects which are utilized to provide personalized recommendations. The architecture consists of two main components: Web Design and Recommendation Engine.

**1. User Interaction:** A user-friendly Streamlit web interface allows users to effortlessly enter their desired product type, skin type and desired effects through intuitive forms.

**2. Feature Extraction:** User input is converted into a numeric format for seamless integration with recommendation algorithms that Enable personalized product recommendations based on preferences.

**3. Filtering:** The system filters the data set to identify user-specified products with similar notable effects, ensuring personalized skin care recommendations tailored to individual needs.

**4. Data pre-processing and Analysis:** The dataset is cleaned, coded, examined and analyzed to ensure reliability and suitability for developing recommender systems. Visualizations help understand product attributes and relationships within the data.

**5. TF-IDF and Cosine Similarity:** TF-IDF converts notable effects into numerical vectors, enabling the creation of a TF-IDF matrix. Cosine Similarity measures the similarity between products based on their TF-IDF values, enabling tailored recommendations.

**6. Recommendations:** Using TF-IDF and Cosine Similarity, the system suggests skin care products that best match user preferences, sorted by similarity scores for personalized and well-organized recommendations.

![Architecture for Cosmetics Recommendation System](https://ibb.co/t8j1bsx)
## Experimental Results

In this section, we present the results of the cosmetic recommendation system. We present the recommendations generated by the model based on user input and highlight the personalized nature of the suggestions. Through a detailed analysis of the results, we provide a comprehensive understanding of how the recommendation system works in real-world scenarios and its impact on improving user experience in the cosmetics industry.
After executing the code, the website will open and display as shown below. The sidebar menu can be resized and also hidden.

![Website look of the Cosmetics Recommendation System](https://ibb.co/ctkJ8Gf)

When the user clicks on the home page, the page appears like this:

![Home Page](https://ibb.co/nwf7Y1L)

When the user interacts with the Get Recommendation page To get personalized recommendations for the products, the page looks like this:

![Get Recommendation Page](https://ibb.co/q0RvGVt)

When the user clicks on the Skin Care Guide page, the page looks like this:

![Skin Care Guide Page](https://ibb.co/jG81FWh)

When the user clicks on the contact page, the page looks like this

![Contact Page](https://ibb.co/XxcWDp1)
## Conclusion

The Cosmetics Recommendation System is a cutting-edge solution carefully designed to revolutionize the way skin care recommendations are made. By incorporating sophisticated techniques such as content-based filtering, TF-IDF vectorization, and cosine similarity, this system provides a personalized approach to suggesting skin care products through an easy-to-use Streamlit web application interface. 

Through a detailed analysis of the unique properties of different skin care products, the system generates tailored recommendations based on users' individual preferences. This includes considering factors such as product category, different skin types, specific skin care concerns, and the remarkable benefits each product delivers. With an emphasis on intuitive interface design and the use of advanced algorithms, users can seamlessly explore a curated selection of skincare solutions, allowing them to make informed decisions regarding their skincare routines.

Leveraging TF-IDF vectorization allows the system to effectively capture the essence of each product's remarkable effects, enabling precise recommendations tailored to each user's different preferences and goals. By prioritizing user experience and leveraging data-driven insights, the Cosmetics Recommendation System stands out as a pioneer in providing tailored skincare recommendations. 

Additionally, by facilitating exploration of products with similarly remarkable effects, the system ensures an enjoyable and enriching skincare journey tailored to each user's diverse needs and desires. Overall, this innovative system sets a new standard in providing personalized skin care solutions that are both effective and user-focused.
