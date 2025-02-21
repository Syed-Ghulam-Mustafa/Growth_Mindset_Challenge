#streamlit
import streamlit as st

st.set_page_config(page_title= "Growth Mindset Project", page_icon="✦")
st.title("Growth Mindset Challenge: Web App with Streamlit 🚀")

st.header("Welcome to the Growth Mindset Journey 🌱")
st.write("🌝 Embrace challenges, learn from mistakes, and unlock your full potential. This is a web app that will help you to develop a growth mindset. You will find a series of challenges that will help you to develop a growth mindset. Are you ready to start? 🌝")

#quote section
st.header("Quote of the Day 🌟")
st.write("🌟 'The only limit to our realization of tomorrow will be our doubts of today.' - Franklin D. Roosevelt 🌟")

#challenge section
st.header("Today's Challenge 🌱")
user_input = st.text_input("What is your challenge for today?")

#condition

if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing forward and don't give up! 💪✨")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflect on your Learning 📝")
reflection = st.text_area("Write your outcomes and reflections here:")

if reflection:
    st.success(f" Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past experience help you grow! Share your difficulties")
    
#achievements

st.header("🏆 Celebrate Your Wins!")
achievments = st.text_input("Share something you have recently achieved:")

if achievments:
    st.success(f"🎉 Congratulations! You have achieved: {achievments}. Keep up the good work! ✨")
else:
    st.info("Big or small achievements, they all count! Share your wins with us now 😍")
    
#footer
st.write("- - -")
st.write("Keep believing in yourself. Growth is a journey, not a destination. 🌱✨")
st.write("©️ 2025 Growth Mindset Project. All rights reserved.")
st.write("**Made with ❤️ by Syed Ghulam Mustafa**")