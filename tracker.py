import streamlit as st

def tracker_page():
    st.header("📊 Health & Wellness Tracker")
    
    water_intake = st.slider("Water intake today (liters)", 0.0, 5.0, 2.0)
    sleep_hours = st.slider("Hours of sleep last night", 0, 12, 7)
    stress_level = st.slider("Stress level (0 = none, 10 = extreme)", 0, 10, 5)
    nutrition_quality = st.selectbox("How would you rate your nutrition today?", 
                                     ["Poor", "Average", "Good", "Excellent"])

    st.markdown("### Your Summary:")
    st.write(f"- Water Intake: {water_intake} L")
    st.write(f"- Sleep Hours: {sleep_hours}")
    st.write(f"- Stress Level: {stress_level}")
    st.write(f"- Nutrition Quality: {nutrition_quality}")

    # Simple advice example based on stress level
    if stress_level >= 7:
        st.warning("Your stress level is high. Consider relaxation techniques or a short break.")
    elif stress_level <= 3:
        st.success("Your stress level is low. Keep up the good work!")
    else:
        st.info("Your stress level is moderate. Stay mindful of your mental health.")

    # Hydration advice
    if water_intake < 2.0:
        st.info("Try to drink more water throughout the day to stay hydrated.")
    else:
        st.success("Great job staying hydrated!")

    # Sleep advice
    if sleep_hours < 6:
        st.info("Consider getting more sleep for better recovery and health.")
    else:
        st.success("Good amount of sleep!")

