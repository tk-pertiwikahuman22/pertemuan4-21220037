import streamlit as st
import pandas as pd

# Fungsi untuk menampilkan grafik
def display_chart(df, chart_type, selected_columns):
    for column in selected_columns:
        st.subheader(f'{chart_type.capitalize()} Chart for {column}')
        if chart_type == 'line':
            st.line_chart(df[column])
        elif chart_type == 'area':
            st.area_chart(df[column])
        elif chart_type == 'bar':
            st.bar_chart(df[column])

def main():
    st.title("Data Visualization App")
    st.write("Upload a dataset and visualize selected columns in different chart types.")
    
    # Upload dataset
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file:
        # Read the dataset
        df = pd.read_csv(uploaded_file)
        st.write("Dataset Overview:")
        st.write(df.head())
        
        # Choose chart type
        chart_type = st.selectbox(
            "Select chart type",
            ("line", "area", "bar")
        )
        
        # Choose columns to display
        selected_columns = st.multiselect(
            "Select columns to display",
            df.columns.tolist()
        )
        
        # Display charts for selected columns
        if selected_columns:
            display_chart(df, chart_type, selected_columns)
        else:
            st.warning("Please select at least one column to display.")
    else:
        st.info("Please upload a CSV file to get started.")

if __name__ == "__main__":
    main()