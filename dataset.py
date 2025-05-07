import streamlit as st
import mysql.connector

# MySQL connection settings
conn = mysql.connector.connect(
    host="82.180.143.66",
    user="u263681140_students",
    password="testStudents@123",
    database="u263681140_students"
)
cursor = conn.cursor()

st.title("Update LightTime Table (ID = 1)")

# Fetch current values from the database
cursor.execute("SELECT StartTimeH, EndTimeH, StartTimeL, StratTimeL FROM LightTime WHERE id = 1")
row = cursor.fetchone()

if row:
    # Use text inputs (no time pickers)
    start_time_h = st.text_input("Start Time H", value=row[0])
    end_time_h = st.text_input("End Time H", value=row[1])
    start_time_l = st.text_input("Start Time L", value=row[2])
    strat_time_l = st.text_input("Strat Time L", value=row[3])  # Confirm spelling is intentional

    if st.button("Update"):
        update_query = """
        UPDATE LightTime 
        SET StartTimeH = %s, EndTimeH = %s, StartTimeL = %s, StratTimeL = %s
        WHERE id = 1
        """
        cursor.execute(update_query, (start_time_h, end_time_h, start_time_l, strat_time_l))
        conn.commit()
        st.success("Record updated successfully.")
else:
    st.error("No record found with ID = 1")

# Close connection
cursor.close()
conn.close()
