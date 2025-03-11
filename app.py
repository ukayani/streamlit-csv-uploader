import streamlit as st
import pandas as pd

# Set page title and description
st.title("CSV Uploader and Viewer")
st.write("Upload a CSV file to view its contents in a table format")

# Create file uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Display success message
    st.success("File successfully uploaded!")
    
    # Read the CSV file into a pandas DataFrame
    try:
        df = pd.read_csv(uploaded_file)
        
        # Display basic information about the dataset
        st.subheader("Data Overview")
        st.write(f"**Rows:** {df.shape[0]}")
        st.write(f"**Columns:** {df.shape[1]}")
        
        # Display the DataFrame
        st.subheader("Data Preview")
        st.dataframe(df)
        
        # Display basic statistics
        if st.checkbox("Show Statistics"):
            st.subheader("Statistical Summary")
            st.write(df.describe())
            
    except Exception as e:
        st.error(f"Error reading the CSV file: {e}")
else:
    # Display instructions when no file is uploaded
    st.info("👆 Please upload a CSV file to view its contents.")
    
    # Example of what the app does
    st.subheader("Example")
    st.write("""
    This app allows you to:
    1. Upload a CSV file
    2. View the data in a table format
    3. See basic statistics about the data
    """)
