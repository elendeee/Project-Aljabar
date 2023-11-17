import numpy as np
import streamlit as st

#tabel rating
data1 = np.mat("1 4 2 3 4 4; \
               0.25 1 2 3 3 3; \
               0.5 0.5 1 4 3 4; \
               0.33 0.33 0.25 1 3 4; \
               0.25 0.33 0.33 0.33 1 2; \
               0.25 0.33 0.25 0.25 0.5 1")


print("Matriks Data:\n", data1)

max_values = np.sum(data1, axis=0)

normalized_matrix5 = data1 / max_values

print("\nMatriks Normalisasi:")
print(np.round(normalized_matrix5, 3))

num_parameters = 6
eigen_values5 = np.sum(normalized_matrix5, axis=1)/num_parameters
print("\nVektor Eigen: ")
print(np.round(eigen_values5, 3))

# Visualisasi hasil
st.write("Matriks Data:")
st.write(data1)

st.write("Matriks Normalisasi:")
st.write(np.round(normalized_matrix5, 3))

st.write("Vektor Eigen: ")
st.write(np.round(eigen_values5, 3))