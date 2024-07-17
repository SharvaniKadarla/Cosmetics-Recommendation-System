<a name="br1"></a> 

Cosmetics Recommendation System based

on Content-Based Filtering

Janapati Himaja<sup>a</sup>, Sharvani Kadarla<sup>a</sup> and Kantha Ananya<sup>a</sup>

<sup>a</sup> Department of Computer Science and Engineering, Stanley College of Engineering & Technology for

Women, Hyderabad, India.

himajajanapati7@gmail.com, sharvanikads@gmail.com, kanthaananya31@gmail.com

**KEYWORDS**

**ABSTRACT**

*In this digital era, an ocean of skincare products often*

*overwhelm consumers, leading to ineffective choices and*

*dissatisfaction. In response to the expanding array of cosmetic*

*products available in the market, this project introduces a*

*sophisticated Cosmetics Recommendation System. Our*

*Cosmetics*

*Recommendation*

*System;*

*Content-Based*

*Filtering Algorithm;*

*Term Frequency -*

*Inverse Document*

*Frequency;*

*web-based design approach emphasizes simplicity and*

*user-friendliness, allowing users to input relevant information*

*such as skin type, product categories, notable effects and other*

*constraints. Utilizing this input, the recommendation system*

*employs a Content-Based Filtering (CBF) algorithm to analyze*

*the user data and match it with a comprehensive database of*

*skincare products. Our approach involves a comprehensive*

*analysis of the textual content of both user profiles and product*

*descriptions, capturing the importance of terms relative to the*

*entire corpus using the TF-IDF(Term Frequency - Inverse*

*Document Frequency) vectorizer. Cosine similarity is then*

*employed to compute the similarity between user profiles and*

*skincare products, resulting in personalized recommendations.*

*By harnessing the power of simple algorithms, this project*

*empowers users to make informed skincare choices tailored to*

*their unique preferences and needs.*

*Cosine Similarity.*

**1. Introduction**

Recently, people have been paying much more attention to taking care of their skin and following

beauty trends. This is why tons of new skin care and beauty products are flooding the market. With so

many options, it is difficult for people to determine which products are best for them. This is where

recommendation systems come into play. This research work is about a special kind of

recommendation system for cosmetics. It uses so-called “content-based filtering” and sophisticated

computer programs to examine various product features and suggest products that meet each person’s

needs and preferences. The goal is to make shopping for skin care items easier and more personalized.

The system considers things likthe type of product, the brand that made it, what it's good for (e.g.



<a name="br2"></a> 

moisturizing or anti-aging), and what type of skin it's best for. It then compares all of these details to

find products that are similar and likely to be a good fit for each person. In this way, the system aims to

make finding the right skin care products easier without feeling overwhelmed by all the choices. It's

like having a helpful friend who knows all about skin care and can recommend the perfect products.

This research report is about how the recommendation system works, how it is built and tested, and

how well it helps people find the skin care products they love. It's about making shopping for skin care

products easier and more enjoyable for everyone.

**Major Contributions are as follows:**

**1. Data Collection and Preprocessing:**

●

●

Collected cosmetics data from an online retailer.

Included essential attributes like product type, brand, notable effects, suitable skin types, and

price.

●

Applied data preprocessing techniques to ensure dataset quality and integrity.

**2. Exploratory Data Analysis (EDA):**

●

Conducted in-depth exploration to understand product type distribution, popular brands,

notable effects, and suitable skin types.

●

Utilized visualizations such as bar graphs, pie charts, and histograms to present key findings

and industry trends.

**3. TF-IDF (Term Frequency - Inverse Document Frequency) Vectorization:**

●

Utilized TF-IDF vectorization to convert textual data (notable effects descriptions) into

numerical representations.

●

Captured the importance of words within each notable effects category for meaningful product

comparisons.

**4. Cosine Similarity Calculation:**

●

Computed cosine similarity based on the TF-IDF matrix to quantify similarity between

cosmetics products.

●

Identified products with similar notable effects profiles to facilitate personalized

recommendations.

**5. Recommendation Generation:**

●

●

Developed a user-friendly website using Streamlit where users can input product names.

Generated recommendations for skincare products closely matching a given product based on

cosine similarity scores.

●

Enabled users to interact with the website to retrieve top recommendations based on notable

effects similarities.

**6. Deployment and Integration:**

●

Deployed the recommendation system as part of an interactive web application using

Streamlit.

●

Enabled seamless access to personalized recommendations and integration with e-commerce

platforms for streamlined purchasing.



<a name="br3"></a> 

**2. Literature Survey**

Table 1: Publications of the Cosmetics Recommendation System

**AUTHORS**

**S.NO YEAR**

**TITLE**

**DATASET USED**

Hsiao-hui Li

Yuan-Hsun Liao

Yen-nun Huang

Po-Jen Cheng.[1]

1

2020

Based on machine It uses images of various human

learning for

personalized skin care

products

faces for skin type classification.

The attributes for the

recommendation system are

recommendation collected from Taiwan Food and

engine.

Drug Administration.

Yoko Nakajima

Hirotoshi Honma

Haruka Aoshima

2

2019

Recommender

System Based on from Cosme and Bihada- Mania

Data (Reviews, Ingredients)

Tomoyoshi Akiba

Shigeru Masuyama.[2]

User Evaluations and

Cosmetic Ingredients

Sites.

Gyeongeun Lee.[3]

3

4

2020

2018

A Content-based

Skincare Product

Recommendation

System

The data set is from an online

book retailer and fashion

retailer.

Joanna Cristy Patty

Elika Thea Kirana

Made Sandra Diamond

Khrismayanti Giri.[4]

Recommendations

System for Purchase database of cosmetics from the

of Cosmetics Using

Content-Based

Filtering

There is an already existing

Ministry of Industry (2016).

Ting-Yu Lin.

Hung-Tse Chan.

Chih-Hsien Hsia.

Chin-Feng Lai.[5]

5

2022

Facial Skincare

Products’

Recommendation self-created datasets were used

Public database Finger Vein

USM(FV-USM) and the

with Computer Vision

Technologies

for this work.



<a name="br4"></a> 

[Jinhee](https://pubmed.ncbi.nlm.nih.gov/?term=Lee+J&cauthor_id=38411029)[ ](https://pubmed.ncbi.nlm.nih.gov/?term=Lee+J&cauthor_id=38411029)[Lee](https://pubmed.ncbi.nlm.nih.gov/?term=Lee+J&cauthor_id=38411029)

[Huisu](https://pubmed.ncbi.nlm.nih.gov/?term=Yoon+H&cauthor_id=38411029)[ ](https://pubmed.ncbi.nlm.nih.gov/?term=Yoon+H&cauthor_id=38411029)[Yoon](https://pubmed.ncbi.nlm.nih.gov/?term=Yoon+H&cauthor_id=38411029)

[Semin](https://pubmed.ncbi.nlm.nih.gov/?term=Kim+S&cauthor_id=38411029)[ ](https://pubmed.ncbi.nlm.nih.gov/?term=Kim+S&cauthor_id=38411029)[Kim](https://pubmed.ncbi.nlm.nih.gov/?term=Kim+S&cauthor_id=38411029)

6

2024

Deep learning-based Collected cosmetic data from

skin care product several cosmetic websites,

recommendation: A companies, and associations and

focus on cosmetic refined them for use in our

ingredient analysis model. Facial skin images were

[Chanhyeok](https://pubmed.ncbi.nlm.nih.gov/?term=Lee+C&cauthor_id=38411029)[ ](https://pubmed.ncbi.nlm.nih.gov/?term=Lee+C&cauthor_id=38411029)[Lee](https://pubmed.ncbi.nlm.nih.gov/?term=Lee+C&cauthor_id=38411029)

[Jongha](https://pubmed.ncbi.nlm.nih.gov/?term=Lee+J&cauthor_id=38411029)[ ](https://pubmed.ncbi.nlm.nih.gov/?term=Lee+J&cauthor_id=38411029)[Lee](https://pubmed.ncbi.nlm.nih.gov/?term=Lee+J&cauthor_id=38411029)

[Sangwook](https://pubmed.ncbi.nlm.nih.gov/?term=Yoo+S&cauthor_id=38411029)[ ](https://pubmed.ncbi.nlm.nih.gov/?term=Yoo+S&cauthor_id=38411029)[Yoo](https://pubmed.ncbi.nlm.nih.gov/?term=Yoo+S&cauthor_id=38411029).[6]

and facial skin

conditions

collected from LUMINI Kiosk

V2® to train each model of skin

analyzer. The skin image

analyzer and ingredient analyzer

are constructed independently

Chih-Hsien Hsia

Ting-Yu Lin

Jhe-Li Lin

Heri Prasetyo

7

2020

System for

Recommending

Facial Skincare (ROI) is identified as the cheeks.

The original facial skin image is

input, and the region of interest

Shih-Lun Chen

Hsien-Wei Tseng.[7]

Products

The ROI image is used to

identify the skin type and detect

acne.

Jiyoung Yoon

Soonhee Joung.[8]

8

2020

A Big Data Based

Cosmetic

The dataset comprises

information on 140,000

Recommendation cosmetics collected through web

Algorithm

crawling from the "Hwahae

App," a Korean cosmetics

application lacking Open APIs.

It includes attributes such as

product ratings, reviews, clicks,

and remaining time. This data is

utilized for text mining and

trend analysis to develop a

personalized recommendation

system based on consumer

preferences and characteristics.

Anam Naz Sodhar

Umair Ali Khan

9

2022

Product

The dataset is typically collected

Irum Naz Sodhar

Abdul Hafeez Buller

Jahanzeb Sodhar.[9]

Recommendation from various sources, including

Using Machine e-commerce websites such as

Learning a Review of Amazon, eBay, Alibaba, or other

the Existing

Techniques

online platforms where users

interact with products.

Villia Putriany

Jaidan Jauhari

Rahmat Izwan

Heroza.[10]

10 2019

Item Clustering as An

Input for Skin Care website(femaledaily.com web

Data from Female Daily

Product

forum for skin-care of women)

Recommended

System using Content

Based Filtering



<a name="br5"></a> 

Muskan Chaurasia

Neha Pathak

Meerut Rani

Muskan Verma

Nandini Gauhri.[11]

11 2022

A Machine Learning The dataset comprises of 1472

Based

Recommendation

System For

products and contains details

about each item's

name,brand,rank,price,skintype,

and chemical ingredients of

product.

Cosmetics

Goeravi Malalur

Rajrgoeda

Yannis Spyridis

Barbara Viklarini

Vasileios

12 2024

13 2023

14 2021

An AI -Assisted A new dataset was developed by

routine

recommendation

system in XR

collecting free images from

different sources of internet

Argyriou.[12]

Prof. V. S. Kadam

Kalyani Dhande

Pradnya Kadam

Gayatri Chinchansure

Aishwarya Jadhav.[13]

A Cosmetic Product A large dataset of random faces

Recommendation of people from various sources,

System Based on

Skin Type Using

AI/ML

such as Google, Kaggle, and

other similar websites.

A. Kothari

D. Shah

T. Soni

Cosmetic Skin Type

The data is collected by the

Classification Using input faces, and skin metrics are

CNN With Product collected from it. Faces are the

S. Dhage.[14]

Recommendation

input.

Nagarajaiah

Kavyashree

Hanakere

15

2022

Artificial Intelligence Skin Faces from Kaggle with

based Smart

Cosmetics

120000 records

Madhu.[15]



<a name="br6"></a> 

Table 2: Performance Summary of Publications on the Cosmetics Recommendation System

**PERFORMANCE**

**PAPER NO**

**ALGORITHM USED**

**MEASURES**

1

YOLOv4 for facial skin recognition. The machine

learning algorithm for recommendations.

Accuracy: 78.8%

Error Rate: 15%

Sensitivity: 0.211%

2

3

4

5

Accuracy: 77.89%

Error Rate: 14.40%

Sensitivity: 0.922%

IF-IPF(Ingredient Frequency- Inverse Product

Frequency) Filtering

Content-based Filtering(CBF)&

Accuracy: 75%

Error Rate: 25%

Sensitivity: 0.08%

Ingredient Frequency-Inverse Product

Frequency(IF-IPF) Filtering

Content-Based Filtering(CBF)

Accuracy: 82%

Error Rate: 20%

Sensitivity: 0.875%

CNN and Support Vector Machine (SVM)

Accuracy: 90%

Error Rate: 10%

Sensitivity: 0.944%

Region-Based Convolutional Neural Network

(R-CNN)

Accuracy: 98%

Error Rate: 2%

Sensitivity: 0.989%

Deep Convolutional Neural Network (DCNN)

Accuracy: 96%

Error Rate: 4%

Sensitivity: 0.979%



<a name="br7"></a> 

6

Deep Neural Network

Accuracy: 81.7%

Precision: 44.6%

Recall: 47.3%

F1 Score: 43.6%

7

8

Machine Learning

Accuracy: 80%

Accuracy: 82%

Term Frequency – Inverse Document Frequency

(TF-IDF)

Cosine Similarity Algorithm

9

Machine Learning Techniques: Content-Based

Filtering and Collaborative Filtering

\-

10

11

12

K-means Clustering and Content-based filtering

Purity metric: 0.29

Purity metric: 0.29

The nonlinear dimensionality reduction algorithm

t-distributed Stochastic Neighbour Embedding

The developed algorithm relies on the "Haar

Cascade" classifier, which is an object detection

application, using a machine learning approach to

identify objects in image streams.

Accuracy: 96%

Precision: 83%

Recall: 76%

F1-score: 79%

13

14

Deep Learning, Convolutional Neural Network

\-

Content-Based Filtering Approach with

Convolutional Neural Network

Accuracy: 85%

15

Convolutional Neural Network (CNN)

Accuracy: 80%



<a name="br8"></a> 

**3. Methodology**

**3.1 Data Collection and Preprocessing**

The dataset utilized in this study comprises comprehensive information about cosmetic products

extracted from the Myntra website, specifically from the Myntra HackerRamp 2021 challenge. With a

total of 966 products, the dataset serves as a valuable resource for training machine learning models

aimed at predicting user preferences and recommending relevant cosmetic products.

The dataset contains eight attributes, each providing essential insights into the characteristics of the

products:

Table 3: Dataset Description

**S.No Attribute Name**

**Data Type**

**Description**

Hyperlink directly linking to the

corresponding product page, facilitating

access to additional details.

1

product\_href

Text or String

Specific name of the product, providing a

unique identifier for each cosmetic item

within the dataset.

2

3

4

5

6

7

8

product\_name

product\_type

brand

Text or String

Categorization of products based on their

classification, showcasing the variety and

range of items.

Categorical or

Text/String

Manufacturer or creator of the product,

offering insights into the diversity of

brands in the dataset.

Text or String

Categorical

Categorical

Numerical

Distinct impacts or benefits associated

with the usage of each cosmetic product,

aiding decision-making.

notable\_effects

skintype

Suitable skin types for optimal results

with each product, enhancing the

relevance of recommendations.

Cost of each product, allowing users to

consider budget constraints and make

informed purchase decisions.

price

Source of the product image, aiding in

product identification and selection

through visual representation.

picture\_src

Text or String

Upon acquisition of the dataset, rigorous preprocessing procedures were conducted to ensure data

quality and integrity. These preprocessing steps included:



<a name="br9"></a> 

**1. Handling Missing Values:** The dataset was carefully examined for any missing values, and

appropriate strategies were employed to either impute missing values or remove incomplete

observations, ensuring the completeness of the dataset.

**2. Removing Duplicate Entries:** Due to the nature of data scraping, duplicate entries were identified

and subsequently removed to eliminate redundancy and maintain the uniqueness of each product

record.

**3. Encoding Categorical Features:** Categorical features such as notable\_effects and skintype were

encoded into numerical representations using techniques such as one-hot encoding or label encoding.

This transformation facilitated the inclusion of categorical data in machine learning models, enabling

the extraction of meaningful insights and patterns.

**3.2 Exploratory Data Analysis (EDA)**

Exploratory data analysis (EDA) covered various aspects of the cosmetics dataset, including brand

distribution, product types, skin type suitability, and notable effects. Through visualizations such as bar

charts and pie charts, the study provided insights into market presence, product variety, consumer

engagement, and product benefits. This comprehensive analysis provided valuable insight into the

dynamics of the cosmetics industry and helped understand consumer preferences, market trends and

product effectiveness.

**1. Brand Distribution Analysis:** The study examined brand distribution to assess market presence,

using bar charts to visualize product count per brand. Top brands were identified based on product

count, revealing popularity and variety.



<a name="br10"></a> 

**2. Product Type Distribution Analysis:** The study examined product type distribution using pie

charts, identified dominant types and their proportions, and provided insights into product diversity.

**3. Skin Type Suitability Analysis:** Study of product suitability for different skin types. Bar charts

visualize products suitable for each type and identify the predominant objectives.

**4. Analysis of notable effects:** Notable effects associated with cosmetic products were examined using

pie charts to reveal the predominant effects of their frequencies.



<a name="br11"></a> 

**3.3 Modelling**

**3.3.1 Algorithm Overview**

**Content-Based Filtering:** Content-based filtering is a recommendation system approach that analyzes

the intrinsic characteristics of items to suggest similar items to users based on their preferences. By

examining item characteristics such as skin types, notable effects, product type, and product

description, the system identifies similarities between items and recommends those that match previous

interactions or explicit feedback from the user. Unlike collaborative filtering, content-based filtering is

not based on user behavior data and is therefore suitable for scenarios where this data may be limited or

unreliable. This approach provides personalized recommendations tailored to individual user

preferences, improving user experience and encouraging engagement with recommended items.

Figure 1: Difference between Collaborative and Content-Based Filtering

**TF-IDF (Term Frequency - Inverse Document Frequency) Vectorizer:** TF-IDF Vectorizer is a text

feature extraction method that converts a collection of documents into numerical vectors. In this case,

notable effects of products are converted into numerical vectors that highlight the importance of terms

in each document while taking into account their rarity across the entire data set. The TF-IDF matrix is

created, which represents the products and their notable effects.

**Cosine Similarity:** Cosine similarity is a metric that measures the cosine of the angle between two

vectors. The TF-IDF vectors of skin care products are used. Cosine similarity ranges from -1 to 1, with

a higher value indicating greater similarity. It calculates how similar the noticeable effects of different

skin care products are to each other. Therefore, similar products are recommended.

**3.3.2 Implementation Steps**

**1. TF-IDF (Term Frequency - Inverse Document Frequency) Vectorizer Implementation:** The

modelling phase of the project focused on implementing the TF-IDF Vectorizer for the

recommendation system. This involved using the tfidfvectorizer() function from the sklearn library to



<a name="br12"></a> 

perform an IDF calculation on the notable\_effects data. The notable\_effects data was converted into a

matrix form using TF-IDF vectors.

**TF-IDF Matrix:**

●

●

●

Rows: Correspond to skin care products.

Columns: Represent terms with notable effects.

Values: TF-IDF values quantify the importance of terms within each product.

Figure 2: TF-IDF (Term Frequency - Inverse Document Frequency) Matrix

**2. Cosine Similarity Calculation:** After TF-IDF transformation, cosine similarity values were

calculated to measure the similarity between different notable\_effects categories. These ratings served

as a quantitative representation of the similarity between pairs of products based on their notable

effects.

**Cosine Similarity Matrix:**

●

●

●

Each row and column correspond to skin care products.

Values represent cosine similarity values between pairs of products.

Higher values indicate greater similarity for notable effects.

Figure 3: Cosine Similarity



<a name="br13"></a> 

**3. Recommendation Generation:** Cosine similarity scores were used to generate product

recommendations within the recommendation system. The similarity scores formed the basis for

identifying products with similar notable\_effects and enabled personalized recommendations for users.

Figure 4: Recommendations Generated

**3.3.3 Development of Website Interface**

**1. Initialization and Configuration**

●

**Streamlit Setup:** Initialize Streamlit and configure page settings such as title, icon and layout.

**2. Sidebar Menu**

●

●

**Menu Configuration:** Create a sidebar menu with options for Home, Get Recommendation,

Skin Care Guide, and Contact Us.

**Icons and Style:** Use icons for menu items and style the menu for better visual appeal and

user experience.

**3. Home Page**

●

●

●

**Introduction:** Provide an introduction to the application and explain its purpose and

functionality.

**Video display:** Embed a video to give users a visual overview of the application and its

features.

**Information:** Provide information about the skin care products available and encourage users

to explore recommendations and skin care tips.

**4. Get Recommendation Page**

●

●

●

**Input Selection:** Allow users to select their skin type, skin concerns, desired benefits, and

brand preference.

**Recommendation generation:** Recommend suitable skin care products based on user input

using a content-based filtering algorithm.

**Interactive Features:** Implement interactive elements such as dropdowns, multi-selects, and

buttons for a seamless user experience.

**5. Skincare Guide Page**

●

**Skincare Tips:**: Present tips and tricks for maximizing the effectiveness of skincare products.



<a name="br14"></a> 

●

●

**Visuals:** Add images to supplement the information provided and make the content more

engaging.

**Educational Content:** Educate users on the proper use and benefits of various skin care

products and routines.

**6. Contact Page**

●

**Contact Information:** View contact information for inquiries and feedback, including email,

phone, website and social media links.

●

**Accessibility:** Ensure users can easily request help or more information.

**4. Proposed Architecture**

The proposed architecture for the project “Cosmetics Recommendation System” involves building a

Python web application using Streamlit that enables users to explicitly select various product types,

skin types, skin problems and notable effects which are utilized to provide personalized

recommendations. The architecture consists of two main components: Web Design and

Recommendation Engine.

**1. User Interaction:** A user-friendly Streamlit web interface allows users to effortlessly enter their

desired product type, skin type and desired effects through intuitive forms.

**2. Feature Extraction:** User input is converted into a numeric format for seamless integration with

recommendation algorithms that Enable personalized product recommendations based on preferences.

**3. Filtering:** The system filters the data set to identify user-specified products with similar notable

effects, ensuring personalized skin care recommendations tailored to individual needs.

**4. Data pre-processing and Analysis:** The dataset is cleaned, coded, examined and analyzed to ensure

reliability and suitability for developing recommender systems. Visualizations help understand product

attributes and relationships within the data.

**5. TF-IDF and Cosine Similarity:** TF-IDF converts notable effects into numerical vectors, enabling

the creation of a TF-IDF matrix. Cosine Similarity measures the similarity between products based on

their TF-IDF values, enabling tailored recommendations.

**6. Recommendations:** Using TF-IDF and Cosine Similarity, the system suggests skin care products

that best match user preferences, sorted by similarity scores for personalized and well-organized

recommendations.

Figure 5: Architecture for Cosmetics Recommendation System



<a name="br15"></a> 

**5. Experimental Results**

In this section, we present the results of the cosmetic recommendation system. We present the

recommendations generated by the model based on user input and highlight the personalized nature of

the suggestions. Through a detailed analysis of the results, we provide a comprehensive understanding

of how the recommendation system works in real-world scenarios and its impact on improving user

experience in the cosmetics industry.

After executing the code, the website will open and display as shown below. The sidebar menu can be

resized and also hidden.

Figure 6: Website look of the Cosmetics Recommendation System



<a name="br16"></a> 

When the user clicks on the home page, the page appears like this:

Figure 7: Home Page



<a name="br17"></a> 

When the user interacts with the Get Recommendation page To get personalized recommendations for

the products, the page looks like this:

Figure 8: Get Recommendation Page



<a name="br18"></a> 

When the user clicks on the Skin Care Guide page “, the page looks like this:

Figure 9: Skin Care Guide Page



<a name="br19"></a> 

When the user clicks on the contact page, the page looks like this

Figure 10: Contact Page

**6. Conclusion**

The Cosmetics Recommendation System is a cutting-edge solution carefully designed to revolutionize

the way skin care recommendations are made. By incorporating sophisticated techniques such as

content-based filtering, TF-IDF vectorization, and cosine similarity, this system provides a personalized

approach to suggesting skin care products through an easy-to-use Streamlit web application interface.

Through a detailed analysis of the unique properties of different skin care products, the system

generates tailored recommendations based on users' individual preferences. This includes considering

factors such as product category, different skin types, specific skin care concerns, and the remarkable

benefits each product delivers. With an emphasis on intuitive interface design and the use of advanced

algorithms, users can seamlessly explore a curated selection of skincare solutions, allowing them to

make informed decisions regarding their skincare routines.

Leveraging TF-IDF vectorization allows the system to effectively capture the essence of each product's

remarkable effects, enabling precise recommendations tailored to each user's different preferences and

goals. By prioritizing user experience and leveraging data-driven insights, the Cosmetics

Recommendation System stands out as a pioneer in providing tailored skincare recommendations.

Additionally, by facilitating exploration of products with similarly remarkable effects, the system

ensures an enjoyable and enriching skincare journey tailored to each user's diverse needs and desires.

Overall, this innovative system sets a new standard in providing personalized skin care solutions that

are both effective and user-focused.



<a name="br20"></a> 

**7. References**

[1] Hsiao-hui Li, Yuan-Hsun Liao, Yen-nun Huang, Po-Jen Cheng, "Based on machine learning for

personalized skin care products recommendation engine", 2020, IEEE Xplore, [link](https://ieeexplore.ieee.org/document/9394031).

[2] Yoko Nakajima, Hirotoshi Honma, Haruka Aoshima, Tomoyoshi Akiba, Shigeru Masuyama,

"Recommender System Based on User Evaluations and Cosmetic Ingredients", 2019, IEEE Xplore,

[link](https://ieeexplore.ieee.org/document/8912051).

[3] Gyeongeun Lee, "A Content-based Skincare Product Recommendation System", 2020, Earlham

College Portfolio, [link](https://portfolios.cs.earlham.edu/wp-content/uploads/2020/05/Gyeongeun_Lee_Paper.pdf).

[4] Joanna Cristy Patty, Elika Thea Kirana, Made Sandra Diamond Khrismayanti Giri,

"Recommendations System for Purchase of Cosmetics Using Content-Based Filtering", 2018,

International Journal of Computer Engineering and Information Technology, [link](https://www.ijceit.org/published/volume10/issue1/1Vol10No1.pdf).

[5] Ting-Yu Lin, Hung-Tse Chan, Chih-Hsien Hsia, Chin-Feng Lai, "Facial Skincare Products’

Recommendation with Computer Vision Technologies", 2022, MDPI, [link](https://www.mdpi.com/2079-9292/11/1/143).

[6] Jinhee Lee, Huisu Yoon, Semin Kim, Chanhyeok Lee, Jongha Lee, Sangwook Yoo, "Deep

learning-based skin care product recommendation: A focus on cosmetic ingredient analysis and facial

skin conditions", 2024, Wiley Online Library, [link](https://onlinelibrary.wiley.com/doi/full/10.1111/jocd.16218).

[7] Chih-Hsien Hsia, Ting-Yu Lin, Jhe-Li Lin, Heri Prasetyo, Shih-Lun Chen, Hsien-Wei Tseng,

"System for Recommending Facial Skincare Products", 2020, Myu Group, [link](https://sensors.myu-group.co.jp/sm_pdf/SM2335.pdf).

[8] Jiyoung Yoon, Soonhee Joung, "A Big Data Based Cosmetic Recommendation Algorithm", 2020,

Asian Association of Schools of Management and Research, [link](http://www.aasmr.org/jsms/Vol10/Vol.10.2.3.pdf).

[9] Anam Naz Sodhar, Umair Ali Khan, Irum Naz Sodhar, Abdul Hafeez Buller, Jahanzeb Sodhar,

"Product Recommendation Using Machine Learning a Review of the Existing Techniques", 2022,

ResearchGate, [link](https://www.researchgate.net/publication/365744577_Product_Recommendation_Using_Machine_Learning_a_Review_of_the_Existing_Techniques).

[10] Villia Putriany, Jaidan Jauhari, Rahmat Izwan Heroza, "Item Clustering as An Input for Skin Care

Product Recommended System using Content Based Filtering", 2019, ResearchGate, [link](https://www.researchgate.net/publication/332428713_Item_Clustering_as_An_Input_for_Skin_Care_Product_Recommended_System_using_Content_Based_Filtering).

[11] Muskan Chaurasia, Neha Pathak, Meerut Rani, Muskan Verma, Nandini Gauhri, "A Machine

Learning Based Recommendation System For Cosmetics", 2022, Pacific Northwest Research Institute,

[link](https://www.pnrjournal.com/index.php/home/article/download/9483/13103/11367?__cf_chl_tk=xdsEmu5LPtPX9xbX5S9WUxJoYtXQJa1ijWdVmNm6Ask-1715336212-0.0.1.1-1642).



<a name="br21"></a> 

[12] Goeravi Malalur Rajrgoeda, Yannis Spyridis, Barbara Viklarini, Vasileios Argyriou, "An AI

-Assisted routine recommendation system in XR", 2024, arXiv, [link](https://arxiv.org/abs/2403.13466).

[13] Prof. V. S. Kadam, Kalyani Dhande, Pradnya Kadam, Gayatri Chinchansure, Aishwarya Jadhav,

"A Cosmetic Product Recommendation System Based on Skin Type Using AI/ML", 2023, Pacific

Northwest Research Institute, [link](https://ijarsct.co.in/Paper10271.pdf).

[14] A. Kothari, D. Shah, T. Soni, S. Dhage, "Cosmetic Skin Type Classification Using CNN With

Product Recommendation", 2021, IEEE Xplore, [link](https://ieeexplore.ieee.org/document/9580174).

[15] Nagarajaiah, Kavyashree, and Hanakere, Madhu. "Artificial Intelligence based Smart Cosmetics

Suggestion System based on Skin Condition", 2022, ResearchGate, [link](https://www.researchgate.net/publication/372991326_Artificial_Intelligence_based_Smart_Cosmetics_Suggestion_System_based_on_Skin_Condition).

