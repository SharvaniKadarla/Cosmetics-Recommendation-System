import streamlit as st
from streamlit_option_menu import option_menu
from numpy.core.fromnumeric import prod
import tensorflow as tf
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image

# Import the Dataset
skincare = pd.read_csv("Myntra_export_skincare.csv", encoding="utf-8", index_col=None)

# Header
st.set_page_config(
    page_title="Cosmetics Recommendation System",
    page_icon="🌸",
    layout="wide",
)

# Add background image using st.sidebar.image
makeup = "makeup.jpeg"  # Replace "makeup.jpeg" with the path to your image file
st.sidebar.image(makeup, use_column_width=True)
# Sidebar menu
with st.sidebar:
    st.title("Main Menu")
    selected = option_menu(
        menu_title="",  # No title needed
        options=["Home", "Get Recommendation ✨", "Skin Care Guide 📚", "Contact 📧"],
        icons=["house", "search", "book", "person"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#fafafa",
            },
            "icon": {"color": "#86eba1", "font-size": "25px"},  # green
            "nav-link": {
                "font-size": "18px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#ac6ade"},  # purple
        },
    )

# Content
st.markdown(
    """
    <style>
    body {
        background-color: #bb95ed; /* Set background color */
    }
    h1 {
        text-align: center; /* Center-align text */
        color: #7965d6; /* Set text color */
        font-family: "Times New Roman",Times, serif; /* Set font family */
        /*font-style: italic; /* Set font style to italic */*/
    }
    span[data-baseweb="tag"] {background-color: #ac6ade !important;} /*purple*/
    div[data-baseweb="select"] > div:first-child {
    border-color: #ac6ade; /* Change border color to coral */ }  /*purple*/
    </style>
    <h1>Cosmetics Recommendation System 🫧</h1>
    """,
    unsafe_allow_html=True,
)

if selected == "Home":
    st.markdown(
        "<h2 style='text-align: center; color: #e84393;'>Step into the World of Personalized Beauty! 💖</h2>",
        unsafe_allow_html=True,
    )
    st.write("---")

    st.markdown(
        """
        <div style='text-align: center;'>
            <h4><strong>🌟 Welcome to Your Bespoke Cosmetics Journey! 🛍️ ✨</strong></h4>
        </div>
        """,
        unsafe_allow_html=True,
    )

    video_file = open("skincare.mp4", "rb").read()
    st.video(video_file, start_time=1)  # displaying the video

    st.write(" ")
    st.write(" ")
    st.write(
        """
        ##### You will get recommendations for skin care products from various cosmetic brands with a total of 900+ products tailored to your skin's needs.
        ##### There are 4 categories of skin care products with 6 different skin types, as well as the problems and benefits you want to get from the products. This recommendation application is just a system that provides recommendations according to the data you enter, not a scientific consultation.
        ##### Please select the *Get Recommendation* page to start getting recommendations. Or select the *Skin Care Guide* page to see tips and tricks about skin care.
        """
    )
    st.write(
        """
        **Good luck!** 🍀
        """
    )

    st.info("Credit: Created by Team-02")

if selected == "Get Recommendation ✨":
    st.markdown(
        "<h2 style='text-align: center; color: #e84393;'>Discover Your Beauty Favorites! 💫</h2>",
        unsafe_allow_html=True,
    )
    st.write("")
    st.write(
        """
        ##### **Unveil Your Perfect Skincare Regimen! 💁‍♀️ Simply tell us your preferred product category, skin type, specific concerns, notable effects, and even your favorite brands, and let us tailor personalized recommendations just for you! 🌿**
         """
    )
    st.write("---")

    first, last = st.columns(2)

    # Choose a product type category pt = product type
    category = first.selectbox(
        label="Product Category 📦", options=skincare["product_type"].unique()
    )
    category_pt = skincare[skincare["product_type"] == category]

    # Choose a skin type st = skin type
    skin_type = last.selectbox(
        label="Your Skin Type 🧴",
        options=["All", "Combination", "Sensitive", "Oily", "Dry", "Normal"],
    )
    category_st_pt = category_pt[category_pt[skin_type] == 1]

    # Select complaint for Skin Problems
    prob = st.multiselect(
        label="Skin Problems 💆‍♀️",
        options=[
            "Acne",
            "Anti-Ageing",
            "Anti-Pollution",
            "Blemishes",
            "Blackheads",
            "Dark Circles",
            "Dark Spots",
            "Deep Nourishment",
            "Dryness",
            "Dull Skin",
            "Excess Oil",
            "Eye Bags",
            "Fine Lines",
            "General Care",
            "Hydration",
            "Irregular Textures",
            "Oily Skin",
            "Pigmentation",
            "Redness",
            "Skin Inflammation",
            "Skin Sagging",
            "Skin Tightening",
            "Smoothening",
            "Softening",
            "Sun Protection",
            "Tan Removal",
            "Uneven Skin Tone",
            "Wrinkles",
            "Whiteheads",
        ],
    )

    # Choose notable_effects
    # From products that have been filtered based on product type and skin type (category_st_pt), we will take a unique value in the notable_effects column
    unique_notable_effects = category_st_pt["notable_effects"].unique().tolist()
    # unique notable effects-notable effects are then entered into the option_ne variable and used for the value in the multiselect which is wrapped in the selected_options variable below
    selected_options = st.multiselect("Notable Effects ✨", unique_notable_effects)
    # We put the results of selected_options into the category_ne_st_pt variable
    category_ne_st_pt = category_st_pt[
        category_st_pt["notable_effects"].isin(selected_options)
    ]

    # Ask user about brand preference
    brand_preference = st.radio("Choose your Brand Preference?", ("Yes", "No"))

    if brand_preference == "Yes":
        brand = st.selectbox(
            "Select Brand 🏷️",
            options=category_ne_st_pt["brand"].unique().tolist(),
            index=0,
        )
        category_brand_ne_st_pt = category_ne_st_pt[category_ne_st_pt["brand"] == brand]
    else:
        category_brand_ne_st_pt = category_ne_st_pt

    # Choose product
    unique_product_href_pairs = category_brand_ne_st_pt[
        ["product_name", "product_href"]
    ].drop_duplicates()
    product = st.selectbox(
        label="Products Recommended for You",
        options=unique_product_href_pairs["product_name"].tolist(),
    )
    if product:
        selected_product_href = unique_product_href_pairs.loc[
            unique_product_href_pairs["product_name"] == product, "product_href"
        ].iloc[0]
        st.markdown(
            f"Explore the Product: <a href='{selected_product_href}' style='color:blue; text-decoration:underline;' target='_blank'>{product}</a>",
            unsafe_allow_html=True,
        )

    # The product variable above will hold a product that will give rise to recommendations for other products
    ## MODELLING with Content Based Filtering
    # Initialization TfidfVectorizer
    tf = TfidfVectorizer()

    # Performing idf calculations on 'notable_effects' data
    tf.fit(skincare["notable_effects"])

    # Mapping array from integer index features to name features
    tf.get_feature_names_out()

    # Perform the fit and then transform it into matrix form
    tfidf_matrix = tf.fit_transform(skincare["notable_effects"])

    # View the tfidf matrix size
    shape = tfidf_matrix.shape

    # Converting tf-idf vector in matrix form with todense() function
    tfidf_matrix.todense()

    # Create a dataframe to view the tf-idf matrix
    # The column is filled with the desired effects
    # The line is filled with the product name

    pd.DataFrame(
        tfidf_matrix.todense(),
        columns=tf.get_feature_names_out(),
        index=skincare.product_name,
    ).sample(shape[1], axis=1).sample(10, axis=0)

    # Calculating cosine similarity on the tf-idf matrix
    cosine_sim = cosine_similarity(tfidf_matrix)

    # Create a dataframe from the cosine_sim variable with rows and columns in the form of product names
    cosine_sim_df = pd.DataFrame(
        cosine_sim, index=skincare["product_name"], columns=skincare["product_name"]
    )

    # Look at the similarity matrix for each product name
    cosine_sim_df.sample(7, axis=1).sample(10, axis=0)

    # Create a function to get recommendations
    def skincare_recommendations(
        product_itemname,
        similarity_data=cosine_sim_df,
        items=skincare[
            ["product_name", "brand", "price", "product_href", "picture_src"]
        ],
        k=10,
    ):
        if product_itemname in similarity_data.columns:
            index = (
                similarity_data.loc[:, product_itemname]
                .to_numpy()
                .argpartition(range(-1, -k, -1))
            )
            recommended_products = similarity_data.columns[index[-1 : -(k + 2) : -1]]
            recommended_products = recommended_products.drop(
                product_itemname, errors="ignore"
            )
            df = pd.DataFrame(recommended_products).merge(items).head(k)
            return df
        else:
            return (
                pd.DataFrame()
            )  # Return an empty DataFrame if product_itemname is not found

    # Define custom CSS styles for the button hover effect
    button_hover_style = """
    <style>
    /* CSS to change the border color and text color of the button */
    .stButton>button {
    border-color: green !important; /* Change border color to green */
    color: green !important; /* Change text color to green */
    }
    /* CSS to change the color of the button when hovered */
    .stButton>button:hover {
    border-color: #ac6ade !important; /* Change border color to purple */
    color: #ac6ade !important; /* Change text color to purple */
    }
    /* CSS to change the background color of the button when clicked */
    .stButton>button:active {
    background-color: #b5ebb5 !important; /* Change background color to light green */
    }
    </style>
    """
    # Display the custom CSS styles
    st.write(button_hover_style, unsafe_allow_html=True)
    model_run = st.button("Find Other Product Recommendations!")
    if model_run:
        st.write(
            "Following are recommendations for other similar products according to what you want"
        )
        recommendations_df = skincare_recommendations(product)
        if not recommendations_df.empty:
            st.write(recommendations_df)
        else:
            st.warning(
                f"No recommendations found for '{product}'. Please try another product."
            )


if selected == "Skin Care Guide 📚":
    st.markdown(
        "<h2 style='text-align: center; color: #e84393;'>Explore Your Skincare Handbook 📖</h2>",
        unsafe_allow_html=True,
    )
    st.write("---")

    st.write(
        """
        ##### **Explore Pro Tips and Tricks for Maximizing Your Skincare Routine! 🎉 Get the Most Out of Your Products with Expert Advice!**
        """
    )

    image = Image.open("imagepic.jpg")
    st.image(image, caption="Skin Care Guide", use_column_width=True)

    st.write(
        """
        ### **1. Face Moisturizer**
        """
    )
    st.write(
        """
        **How to Use:**

        Cleanse: Start with a clean face.

        Apply Moisturizer: Use a small amount of Face Moisturizer, applying evenly to your face and neck.

        Frequency: Use twice daily – morning and night.

        **Benefits:**

        Hydration Boost: Instantly replenishes moisture.

        Nourishment: Provides a soft, revitalized feel.

        Anti-Aging: Fights fine lines and wrinkles.

        Skin Barrier Support: Strengthens against environmental stressors.

        Versatile: Suitable for all skin types.

        Lightweight: Fast-absorbing, non-greasy formula.

        Daily Ritual: Simple step for beautiful, glowing skin.
        """
    )

    st.write(
        """
        ### **2. Cleanser**
        """
    )
    st.write(
        """
        **How to Use:**

        Wet Face: Start with a damp face.

        Apply Cleanser: Dispense a small amount of our Facial Cleanser onto your palm.

        Gentle Massage: Gently massage the cleanser onto your face using circular motions, focusing on areas with makeup or impurities.

        Rinse: Thoroughly rinse your face with lukewarm water until the cleanser is completely washed away.

        Pat Dry: Pat your face dry with a clean towel.

        **Benefits:**

        Deep Cleansing: Removes impurities, makeup, and excess oil.

        Refreshing: Leaves your skin feeling refreshed and rejuvenated.

        Balancing: Balances skin without over-drying.

        Prepares Skin: Prepares your skin for subsequent skincare steps.

        Glowing Complexion: Promotes a radiant and clear complexion.

        Suitable for All Skin Types: Gentle formula suitable for various skin types.

        Daily Use: Ideal for daily use in your skincare routine.
        """
    )

    st.write(
        """
        ### **3. Mask And Peel**
        """
    )
    st.write(
        """
        **How to Use:**

        Cleanse: Begin with a clean face using your suitable cleanser.

        Apply Mask: Apply a generous layer of our Mask and Peel evenly across your face, avoiding the eye and lip areas.

        Relax: As the product mentions, allow the mask to sit for minutes. Use this time to relax and unwind.

        Peel Off or Rinse: Once dry, gently peel off the mask or rinse it off with lukewarm water, revealing fresh, revitalized skin.

        Pat Dry: Pat your face dry with a clean towel.

        **Benefits:**

        Exfoliation: Gently exfoliates, removing dead skin cells.

        Deep Cleansing: Purifies pores for a clearer complexion.

        Brightening: Reveals a brighter and more radiant skin tone.

        Hydration Boost: Infuses the skin with moisture.

        Tightening: Firms and tightens the skin for a lifted appearance.

        Smooth Texture: Promotes a smoother and softer skin texture.

        Weekly Ritual: Use weekly to enhance your skincare routine.
        """
    )

    st.write(
        """
        ### **4. Eye Cream**
        """
    )
    st.write(
        """
       **How to Use:**

        Cleanse: Begin with a gentle cleanse to ensure a fresh canvas.

        Dispense a Pea-Sized Amount: Take a small amount of Eye Cream on your ring finger.

        Dab and Pat: Gently dab the eye cream around the eye area using your ring finger. Avoid direct contact with the eyes.

        Smooth Inward: With a gentle patting motion, smooth the eye cream from the outer to the inner corner of the eye.

        Apply Morning and Night: Use daily, both in the morning and night, as the final step in your skincare routine.

        **Benefits:**

        Dark Circle Reduction: Targets and minimizes the appearance of dark circles.

        Puffiness Relief: Soothes and reduces under-eye puffiness.

        Fine Line Smoothing: Helps diminish the look of fine lines and crow's feet.

        Hydration Boost: Infuses delicate skin with essential moisture.

        Brightening Effect: Enhances the brightness and vitality of the eye area.

        Fast Absorption: Lightweight formula absorbs quickly, suitable for under makeup.

        Daily Ritual: Elevate your daily routine for refreshed and revitalized eyes.
         """
    )

    st.write(
        """
    ### **5. Stick to Your Skincare Routine**
    """
    )
    st.write(
        """
    It's tempting to switch skincare products frequently, but doing so can stress your skin as it adapts to new ingredients. For optimal results, stick to your skincare regimen for several months to allow your skin to adjust and see the full benefits.
     """
    )

    st.write(
        """
    ### **6. Embrace Consistency**
    """
    )
    st.write(
        """
    Consistency is key when it comes to skincare. Make it a habit to use your skincare products diligently and regularly. Remember, skincare is a journey, not a destination, so stay committed to your routine for long-term results.
     """
    )

    st.write(
        """
    ### **7. Treat Your Face as a Precious Asset**
    """
    )
    st.write(
        """
    Your face is a precious gift, deserving of the best care possible. Treat your skincare routine as a form of self-care and gratitude for your body. Invest in products and practices that nourish and protect your skin, starting from a young age to maintain its health and vitality throughout your life.
     """
    )

# Placeholder function for "Contact" option
if selected == "Contact 📧":
    st.write(
        """
    ## Contact
    For any inquiries or feedback, please feel free to reach out to us using the following methods:
    
    📧 **Email:** team2@gmail.com
    
    📞 **Phone:** +0123456789
    
    🌐 **Website:** [www.cosmeticsrecommendations.com](http://www.cosmeticsrecommendations.com)
    
    📱 **Social Media:**
        - [Twitter](https://twitter.com/cosmeticsrec)
        - [Instagram](https://www.instagram.com/cosmeticsrecommendations/)
        - [Facebook](https://www.facebook.com/cosmeticsrecommendations/)
    """
    )
