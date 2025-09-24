import streamlit as st
import pandas as pd
import io
import pyarrow as pq
# Streamlit app title
st.title("Parquet to CSV Converter")

# Step 1: Upload a Parquet file
uploaded_file = st.file_uploader("Upload a Parquet file", type=["parquet"])


#able = pq.ParquetFile(uploaded_file)

#row_count = table.metadata.num_rows
#print(f"Row count from metadata: {row_count}") 
 

if uploaded_file is not None:
    # Step 2: Read the uploaded Parquet file into a DataFrame
    df = pd.read_parquet(uploaded_file, engine='pyarrow')

    # Step 3: Show row count
    st.success(f"✅ Loaded file with {len(df):,} rows.")

    # Step 4: Convert DataFrame to CSV in memory
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_data = csv_buffer.getvalue()

    # Step 5: Provide download button for CSV
    st.download_button(
        label="⬇️ Download CSV",
        data=csv_data,
        file_name="converted.csv",
        mime="text/csv"
    )

    # Optional: Show preview
    st.subheader("Preview of Data:")
    st.dataframe(df.head())
