import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from streamlit_lottie import st_lottie

#function untuk all 

#function table1
def tabelkriteria1():
    # Tabel rating
    data1 = np.mat("1 4 2 3 4 4; \
                   0.25 1 2 3 3 3; \
                   0.5 0.5 1 4 3 4; \
                   0.33 0.33 0.25 1 3 4; \
                   0.25 0.33 0.33 0.33 1 2; \
                   0.25 0.33 0.25 0.25 0.5 1")

    print("Matriks Data:\n", data1)

    max_values = np.sum(data1, axis=0)

    normalized_matrix1 = data1 / max_values

    print("\nMatriks Normalisasi:")
    print(np.round(normalized_matrix1, 6))
    
    num_parameters = 6  # Jumlah parameter
    eigen_values1 = np.sum(normalized_matrix1, axis=1) / num_parameters
    print("\nVektor Eigen: ")
    print(np.round(eigen_values1, 5))
    
    sum_columns = np.sum(normalized_matrix1, axis=0)
    print("\nJumlah tiap kolom pada Matriks Normalisasi:")
    print(np.round(sum_columns, 6))
    
    sum_columns_eigen = np.sum(eigen_values1, axis=0)
    print(np.round(sum_columns, 6))
    return normalized_matrix1, eigen_values1, sum_columns, sum_columns_eigen

# Memanggil fungsi tabelkriteria
result_normalized_matrix, result_eigen_values, result_sum, result_sum_eigen1 = tabelkriteria1()

def nilaicr():
    # Data diambil dari tabel parameter (data 1)
    data = np.array([[1., 4., 2., 3., 4., 4.],
                     [0.25, 1., 2., 3., 3., 3.],
                     [0.5, 0.5, 1., 4., 3., 4.],
                     [0.33, 0.33, 0.25, 1., 3., 4.],
                     [0.25, 0.33, 0.33, 0.33, 1., 2.],
                     [0.25, 0.33, 0.25, 0.25, 0.5, 1.]])

    # Priority vector merupakan vektor eigen yang didapat dari tabel parameter
    priority_vector = np.array([[0.35069, 0.20444, 0.20281, 0.12285, 0.06882, 0.05037]])

    hasil_matriks = np.multiply(data, priority_vector)

    sum_horizontal = np.sum(hasil_matriks, axis=1)

    total_sum = np.sum(sum_horizontal / priority_vector)
    
    num_parameters = 6
    lambda_maks = total_sum / num_parameters

    CI = (lambda_maks - num_parameters) / (num_parameters - 1)

    RI = 1.24
    CR = CI / RI


    result = {
        'Karena CR < 0.1 berarti referensi data dummy adalah konsisten.': CR < 0.1
    }

    return hasil_matriks, sum_horizontal, total_sum, lambda_maks, CI, CR, result
result_hasil1, result_vector, result_total, result_lambda, result_ci, result_cr, result_consistency = nilaicr()

#function table 2 harga
def tabelkriteria2():
    # Tabel rating
    data2 = np.mat("1 2 1 2 2 1; \
               0.5 1 1 2 1 1; \
               1 1 1 2 1 2; \
               0.5 0.5 0.5 1 2 1; \
               0.5 1 1 0.5 1 1; \
               1 1 0.5 1 1 1")

    print("Matriks Data:\n", data2)

    max_values = np.sum(data2, axis=0)

    normalized_matrix2 = data2 / max_values

    print("\nMatriks Normalisasi:")
    print(np.round(normalized_matrix2, 6))
    
    num_parameters = 6  # Jumlah parameter
    eigen_values2 = np.sum(normalized_matrix2, axis=1) / num_parameters
    print("\nVektor Eigen: ")
    print(np.round(eigen_values2, 5))
    
    sum_columns2 = np.sum(normalized_matrix2, axis=0)
    print("\nJumlah tiap kolom pada Matriks Normalisasi:")
    print(np.round(sum_columns2, 6))
    
    sum_columns_eigen2 = np.sum(eigen_values2, axis=0)
    print(np.round(sum_columns2, 6))
    return normalized_matrix2, eigen_values2, sum_columns2, sum_columns_eigen2

# Memanggil fungsi tabelkriteria
result_normalized_matrix2, result_eigen_values2, result_sum2, result_sum_eigen2 = tabelkriteria2()

def nilaicr2():
    # Data diambil dari tabel parameter (data 2)
    data2 = np.array([[1. , 2. , 1. , 2. , 2. , 1. ],
                 [0.5, 1. , 1. , 2. , 1. , 1. ],
                 [1. , 1. , 1. , 2. , 1. , 2. ],
                 [0.5, 0.5, 0.5, 1. , 2. , 1. ],
                 [0.5, 1. , 1. , 0.5, 1. , 1. ],
                 [1. , 1. , 0.5, 1. , 1. , 1. ]])

    # Priority vector merupakan vektor eigen yang didapat dari tabel parameter
    priority_vector2 = np.array([[0.22634, 0.16135, 0.20368, 0.13309, 0.13194, 0.1436 ]])

    hasil_matriks2 = np.multiply(data2, priority_vector2)

    sum_horizontal2 = np.sum(hasil_matriks2, axis=1)

    total_sum2 = np.sum(sum_horizontal2 / priority_vector2)
    
    num_parameters = 6
    lambda_maks2 = total_sum2 / num_parameters

    CI2 = (lambda_maks2 - num_parameters) / (num_parameters - 1)

    RI = 1.24
    CR2 = CI2 / RI


    result2 = {
        'Karena CR < 0.1 berarti referensi data dummy adalah konsisten.': CR2 < 0.1
    }

    return hasil_matriks2, sum_horizontal2, total_sum2, lambda_maks2, CI2, CR2, result2
result_hasil2, result_vector2, result_total2, result_lambda2, result_ci2, result_cr2, result_consistency2 = nilaicr2()

#function tabel 3 freeong
def tabelkriteria3():
    # Tabel rating
    data3 = np.mat("1 2 1 2 1 2; \
               0.5 1 2 1 2 2; \
               1 0.5 1 2 1 2; \
               0.5 1 0.5 1 1 2; \
               1 0.5 1 1 1 2; \
               0.5 0.5 0.5 0.5 0.5 1")

    print("Matriks Data:\n", data3)

    max_values3 = np.sum(data3, axis=0)

    normalized_matrix3 = data3 / max_values3

    print("\nMatriks Normalisasi:")
    print(np.round(normalized_matrix3, 6))
    
    num_parameters = 6  # Jumlah parameter
    eigen_values3 = np.sum(normalized_matrix3, axis=1) / num_parameters
    print("\nVektor Eigen: ")
    print(np.round(eigen_values3, 5))
    
    sum_columns3 = np.sum(normalized_matrix3, axis=0)
    print("\nJumlah tiap kolom pada Matriks Normalisasi:")
    print(np.round(sum_columns3, 6))
    
    sum_columns_eigen3 = np.sum(eigen_values3, axis=0)
    print(np.round(sum_columns3, 6))
    return normalized_matrix3, eigen_values3, sum_columns3, sum_columns_eigen3

# Memanggil fungsi tabelkriteria
result_normalized_matrix3, result_eigen_values3, result_sum3, result_sum_eigen3 = tabelkriteria3()

def nilaicr3():
    # Data diambil dari tabel parameter (data 3)
    data3 = np.array([[1.,  2.,  1.,  2.,  1.,  2. ],
                  [0.5, 1.,  2.,  1., 2.,  2. ],
                  [1.,  0.5, 1.,  2.,  1.,  2. ],
                  [0.5, 1.,  0.5, 1.,  1.,  2. ],
                  [1.,  0.5, 1.,  1.,  1.,  2. ],
                  [0.5, 0.5, 0.5, 0.5, 0.5, 1. ]])

    # Priority vector merupakan vektor eigen yang didapat dari tabel parameter
    priority_vector3 = np.array([[0.22581, 0.20818, 0.18035, 0.14088, 0.15813, 0.08664 ]])

    hasil_matriks3 = np.multiply(data3, priority_vector3)

    sum_horizontal3 = np.sum(hasil_matriks3, axis=1)

    total_sum3 = np.sum(sum_horizontal3 / priority_vector3)
    
    num_parameters = 6
    lambda_maks3 = total_sum3 / num_parameters

    CI3 = (lambda_maks3 - num_parameters) / (num_parameters - 1)

    RI = 1.24
    CR3 = CI3 / RI


    result3 = {
        'Karena CR < 0.1 berarti referensi data dummy adalah konsisten.': CR3 < 0.1
    }

    return hasil_matriks3, sum_horizontal3, total_sum3, lambda_maks3, CI3, CR3, result3
result_hasil3, result_vector3, result_total3, result_lambda3, result_ci3, result_cr3, result_consistency3 = nilaicr3()
    
#function tabel 4 Review Rating
def tabelkriteria4():
    # Tabel rating
    data4 = np.mat("1 1 1 2 2 1; \
               1 1 2 1 2 1; \
               1 0.5 1 2 1 2; \
               0.5 1 0.5 1 1 1; \
               0.5 0.5 1 1 1 2; \
               1 1 0.5 1 0.5 1")

    print("Matriks Data:\n", data4)

    max_values4 = np.sum(data4, axis=0)

    normalized_matrix4 = data4 / max_values4

    print("\nMatriks Normalisasi:")
    print(np.round(normalized_matrix4, 6))
    
    num_parameters = 6  # Jumlah parameter
    eigen_values4 = np.sum(normalized_matrix4, axis=1) / num_parameters
    print("\nVektor Eigen: ")
    print(np.round(eigen_values4, 5))
    
    sum_columns4 = np.sum(normalized_matrix4, axis=0)
    print("\nJumlah tiap kolom pada Matriks Normalisasi:")
    print(np.round(sum_columns4, 6))
    
    sum_columns_eigen4 = np.sum(eigen_values4, axis=0)
    print(np.round(sum_columns4, 6))
    return normalized_matrix4, eigen_values4, sum_columns4, sum_columns_eigen4


# Memanggil fungsi tabelkriteria
result_normalized_matrix4, result_eigen_values4, result_sum4, result_sum_eigen4 = tabelkriteria4()

def nilaicr4():
    # Data diambil dari tabel parameter (data 4)
    data4 = np.array([[1.,  1.,  1.,  2.,  2.,  1. ],
                [1.,  1.,  2.,  1.,  2.,  1. ],
                [1.,  0.5, 1.,  2.,  1.,  2. ],
                [0.5, 1.,  0.5, 1.,  1.,  1. ],
                [0.5, 0.5, 1.,  1.,  1.,  2. ],
                [1.,  1.,  0.5, 1.,  0.5, 1. ]])

    # Priority vector merupakan vektor eigen yang didapat dari tabel parameter
    priority_vector4 = np.array([[0.20139, 0.20833, 0.18333, 0.12778, 0.14583, 0.13333 ]])

    hasil_matriks4 = np.multiply(data4, priority_vector4)

    sum_horizontal4 = np.sum(hasil_matriks4, axis=1)

    total_sum4 = np.sum(sum_horizontal4 / priority_vector4)
    
    num_parameters = 6
    lambda_maks4 = total_sum4 / num_parameters

    CI4 = (lambda_maks4 - num_parameters) / (num_parameters - 1)

    RI = 1.24
    CR4 = CI4 / RI


    result4 = {
        'Karena CR < 0.1 berarti referensi data dummy adalah konsisten.': CR4 < 0.1
    }

    return hasil_matriks4, sum_horizontal4, total_sum4, lambda_maks4, CI4, CR4, result4
result_hasil4, result_vector4, result_total4, result_lambda4, result_ci4, result_cr4, result_consistency4 = nilaicr4()

#function tabel 5 Jumlah Produk Terjual
def tabelkriteria5():
    # Tabel rating
    data5 = np.mat("1 2 1 2 2 1; \
               0.5 1 2 1 2 1; \
               1 0.5 1 2 1 2; \
               0.5 1 0.5 1 1 1; \
               0.5 0.5 1 1 1 2; \
               1 1 0.5 1 0.5 1")

    print("Matriks Data:\n", data5)

    max_values5 = np.sum(data5, axis=0)

    normalized_matrix5 = data5 / max_values5

    print("\nMatriks Normalisasi:")
    print(np.round(normalized_matrix5, 6))
    
    num_parameters = 6  # Jumlah parameter
    eigen_values5 = np.sum(normalized_matrix5, axis=1) / num_parameters
    print("\nVektor Eigen: ")
    print(np.round(eigen_values5, 5))
    
    sum_columns5 = np.sum(normalized_matrix5, axis=0)
    print("\nJumlah tiap kolom pada Matriks Normalisasi:")
    print(np.round(sum_columns5, 6))
    
    sum_columns_eigen5 = np.sum(eigen_values5, axis=0)
    print(np.round(sum_columns5, 6))
    return normalized_matrix5, eigen_values5, sum_columns5, sum_columns_eigen5


# Memanggil fungsi tabelkriteria
result_normalized_matrix5, result_eigen_values5, result_sum5, result_sum_eigen5 = tabelkriteria5()

def nilaicr5():
    # Data diambil dari tabel parameter (data 5)
    data5 = np.array([[1.,  2.,  1.,  2.,  2.,  1. ],
                [0.5,  1.,  2.,  1.,  2.,  1. ],
                [1.,  0.5, 1.,  2.,  1.,  2. ],
                [0.5, 1.,  0.5, 1.,  1.,  1. ],
                [0.5, 0.5, 1.,  1.,  1.,  2. ],
                [1.,  1.,  0.5, 1.,  0.5, 1. ]])

    # Priority vector merupakan vektor eigen yang didapat dari tabel parameter
    priority_vector5 = np.array([[0.22731, 0.18796, 0.18426, 0.12407, 0.14491, 0.13148 ]])

    hasil_matriks5 = np.multiply(data5, priority_vector5)

    sum_horizontal5 = np.sum(hasil_matriks5, axis=1)

    total_sum5 = np.sum(sum_horizontal5 / priority_vector5)
    
    num_parameters = 6
    lambda_maks5 = total_sum5 / num_parameters

    CI5 = (lambda_maks5 - num_parameters) / (num_parameters - 1)

    RI = 1.24
    CR5 = CI5 / RI


    result5 = {
        'Karena CR < 0.1 berarti referensi data dummy adalah konsisten.': CR5 < 0.1
    }

    return hasil_matriks5, sum_horizontal5, total_sum5, lambda_maks5, CI5, CR5, result5
result_hasil5, result_vector5, result_total5, result_lambda5, result_ci5, result_cr5, result_consistency5 = nilaicr5()

#function tabel 6 Keaslian Produk
def tabelkriteria6():
    # Tabel rating
    data6 = np.mat("1 2 1 2 2 1; \
               0.5 1 2 1 1 1; \
               1 0.5 1 2 1 1; \
               0.5 1 0.5 1 2 1; \
               0.5 1 1 0.5 1 2; \
               1 1 1 1 0.5 1")

    print("Matriks Data:\n", data6)

    max_values6 = np.sum(data6, axis=0)

    normalized_matrix6 = data6 / max_values6

    print("\nMatriks Normalisasi:")
    print(np.round(normalized_matrix6, 6))
    
    num_parameters = 6  # Jumlah parameter
    eigen_values6 = np.sum(normalized_matrix6, axis=1) / num_parameters
    print("\nVektor Eigen: ")
    print(np.round(eigen_values6, 5))
    
    sum_columns6 = np.sum(normalized_matrix6, axis=0)
    print("\nJumlah tiap kolom pada Matriks Normalisasi:")
    print(np.round(sum_columns6, 6))
    
    sum_columns_eigen6 = np.sum(eigen_values6, axis=0)
    print(np.round(sum_columns6, 6))
    return normalized_matrix6, eigen_values6, sum_columns6, sum_columns_eigen6

# Memanggil fungsi tabelkriteria
result_normalized_matrix6, result_eigen_values6, result_sum6, result_sum_eigen6 = tabelkriteria6()

def nilaicr6():
    # Data diambil dari tabel parameter (data 6)
    data6 = np.array([[1.,  2.,  1.,  2.,  2.,  1. ],
                [0.5,  1.,  2.,  1.,  1.,  1. ],
                [1.,  0.5, 1.,  2.,  1.,  1. ],
                [0.5, 1.,  0.5, 1.,  2.,  1. ],
                [0.5, 1., 1.,  0.5,  1.,  2. ],
                [1.,  1.,  1., 1.,  0.5, 1. ]])

    # Priority vector merupakan vektor eigen yang didapat dari tabel parameter
    priority_vector6 = np.array([[0.22666, 0.1637, 0.16597, 0.14746, 0.15075, 0.14546 ]])

    hasil_matriks6 = np.multiply(data6, priority_vector6)

    sum_horizontal6 = np.sum(hasil_matriks6, axis=1)

    total_sum6 = np.sum(sum_horizontal6 / priority_vector6)
    
    num_parameters = 6
    lambda_maks6 = total_sum6 / num_parameters

    CI6 = (lambda_maks6 - num_parameters) / (num_parameters - 1)

    RI = 1.24
    CR6 = CI6 / RI


    result6 = {
        'Karena CR < 0.1 berarti referensi data dummy adalah konsisten.': CR6 < 0.1
    }

    return hasil_matriks6, sum_horizontal6, total_sum6, lambda_maks6, CI6, CR6, result6
result_hasil6, result_vector6, result_total6, result_lambda6, result_ci6, result_cr6, result_consistency6 = nilaicr6()

def tabelkriteria7():
    # Tabel rating
    data7 = np.mat("1 2 2 2 2 2; \
               0.5 1 2 2 1 1; \
               0.5 0.5 1 2 1 1; \
               0.5 0.5 0.5 1 1 1; \
               0.5 1 1 1 1 1; \
               0.5 1 1 1 1 1")

    print("Matriks Data:\n", data7)

    max_values7 = np.sum(data7, axis=0)

    normalized_matrix7 = data7 / max_values7

    print("\nMatriks Normalisasi:")
    print(np.round(normalized_matrix7, 6))
    
    num_parameters = 6  # Jumlah parameter
    eigen_values7 = np.sum(normalized_matrix7, axis=1) / num_parameters
    print("\nVektor Eigen: ")
    print(np.round(eigen_values7, 5))
    
    sum_columns7 = np.sum(normalized_matrix7, axis=0)
    print("\nJumlah tiap kolom pada Matriks Normalisasi:")
    print(np.round(sum_columns7, 6))
    
    sum_columns_eigen7 = np.sum(eigen_values7, axis=0)
    print(np.round(sum_columns7, 6))
    return normalized_matrix7, eigen_values7, sum_columns7, sum_columns_eigen7

# Memanggil fungsi tabelkriteria
result_normalized_matrix7, result_eigen_values7, result_sum7, result_sum_eigen7 = tabelkriteria7()


def nilaicr7():
    # Data diambil dari tabel parameter (data 7)
    data7 = np.array([[1.,  2.,  2.,  2.,  2.,  2. ],
                [0.5,  1.,  2.,  2.,  1.,  1. ],
                [0.5,  0.5, 1.,  2.,  1.,  1. ],
                [0.5, 0.5,  0.5, 1.,  1.,  1. ],
                [0.5, 1., 1.,  1.,  1.,  1. ],
                [0.5,  1.,  1., 1.,  1., 1. ]])

    # Priority vector merupakan vektor eigen yang didapat dari tabel parameter
    priority_vector7 = np.array([[0.27989, 0.18069, 0.14458, 0.11495, 0.13995, 0.13995 ]])

    hasil_matriks7 = np.multiply(data7, priority_vector7)

    sum_horizontal7 = np.sum(hasil_matriks7, axis=1)

    total_sum7 = np.sum(sum_horizontal7 / priority_vector7)
    
    num_parameters = 6
    lambda_maks7 = total_sum7 / num_parameters

    CI7 = (lambda_maks7 - num_parameters) / (num_parameters - 1)

    RI = 1.24
    CR7 = CI7 / RI


    result7 = {
        'Karena CR < 0.1 berarti referensi data dummy adalah konsisten.': CR7 < 0.1
    }

    return hasil_matriks7, sum_horizontal7, total_sum7, lambda_maks7, CI7, CR7, result7
result_hasil7, result_vector7, result_total7, result_lambda7, result_ci7, result_cr7, result_consistency7 = nilaicr7()

# Menambahkan latar belakang gradasi
st.markdown(
    """
    <style>
        body {
            background-image: linear-gradient(to right, #aa4465, #9f4398, #7868e6, #6573e6);
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

#SIDEBAR
option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Home', 'Dataframe', 'Chart')
)

if option == 'Home' or option == '':
    with open("Animation - 1700811928398.json") as source:
        animation=json.load(source)

    st_lottie(animation)
    
    st.write("""# Implementasi Nilai dan Vektor Eigen untuk Menentukan Prioritas Faktor-Faktor Pembelian Barang dan Pemilihan E-Commerce""")  # menampilkan halaman utama
    st.write("""
    Web ini digunakan untuk melakukan perhitungan model keputusan dari faktor-faktor pembelian barang dan pemilihan e-commerce dengan menggunakan konsep matriks dan vektor eigen, dimana faktor-faktor ini bisa dihitung dengan menggunakan data dummy yang telah dibuat
    """)
elif option == 'Dataframe':
    st.write("""## Data Dummy""")  # menampilkan judul halaman dataframe
    st.write("""Definisi Kode :
    \n1: Kedua kriteria sama-sama dominan
    \n2: Kriteria (A) sedikit lebih dominan dibanding
    dengan (B)
    \n3: Kriteria (A) jelas lebih dominan dibanding
    \ndengan (B)
    \n4: Kriteria (A) sangat lebih dominan dibanding
    dengan (B)
    \nKebalikan Jika mendapat A terhadap B, maka B terhadap A adalah 1/a.
    """)
    #DATA DUMMY
    df = pd.DataFrame({
        'Kode': ['A,B', 'A,B', 'A,B', 'A,B', 'A,B', 'A,B', 'A,B', 'A,B', 'A,B', 'A,B', 'A,B', 'A,B', 'A,B', 'A,B', 'A,B'],
        'Parameter': ['Harga, Gratis Ongkir', 'Harga, Review & Rating', 'Harga, Jumlah Produk Terjual', 'Harga, Keaslian Produk', 'Harga, Skala Toko', 'Gratis Ongkir, Review & Rating', 'Gratis Ongkir, Jumlah Produk Terjual', 'Gratis Ongkir, Keaslian Produk', 'Gratis Ongkir, Skala Toko', 'Review & Rating, Jumlah Produk Terjual', 'Review & Rating, Keaslian Produk', 'Review & Rating, Skala Toko', 'Jumlah Produk Terjual, Keaslian Produk', 'Jumlah Produk Terjual, Skala Toko', 'Keaslian Produk, Skala Toko'],
        'Dominan': ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
        'Bobot': [4, 2, 3, 4, 4, 2, 3, 3, 3, 4, 3, 4, 3, 4, 2]
    })

    # Menampilkan dataframe
    st.dataframe(df)
    
    

    # Menambahkan dropdown di samping tabel
    selected_column = st.selectbox("Apa yang mau anda Hitung :",['Pilih Perhitungan', 'Kriteria Faktor Pembelian', 'Kriteria Harga Dibandingkan dengan Alternatif E-Commerce', 'Kriteria Gratis Ongkir Dibandingkan dengan Alternatif E-Commerce', 'Kriteria Review & Rating Dibandingkan dengan Alternatif E-Commerce', 'Kriteria Jumlah Produk Terjual Dibandingkan dengan Alternatif E-Commerce', 'Kriteria Keaslian Produk Dibandingkan dengan Alternatif E-Commerce', 'Kriteria Skala Toko Dibandingkan dengan Alternatif E-Commerce'], key='dropdown_column', help="Pilih yang ingin dihitung")
    
    if selected_column == 'Kriteria Faktor Pembelian':
       table1 = pd.DataFrame({
            'Parameter': ['Harga', 'Gratis Ongkir', 'Review dan Rating', 'Jumlah Produk Terjual', 'Keaslian Produk', 'Skala Toko'],
            'Harga': [1,  '1/4',  '1/2',  '1/3',  '1/4',  '1/4'],
            'Gratis Ongkir': [4, 1,  '1/2',  '1/3',  '1/3',  '1/3'],
            'Review dan Rating': [2,  2,  1,  '1/4',  '1/3', '1/4' ],
            'Jumlah Produk Terjual': [3, 3, 4, 1,  '1/3',  '1/4'],
            'Keaslian Produk': [4, 3,  3,  3, 1,  '1/2'],
            'Skala Toko': [4, 3, 4, 4,  2,  1], 
        })
       st.dataframe(table1)
              
    elif selected_column == 'Kriteria Harga Dibandingkan dengan Alternatif E-Commerce':   
        table2 = pd.DataFrame({
            'Harga': ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami'],
            'Shopee': [1,  '1/2',  '1',  '1/2',  '1/2',  1],
            'Tokopedia': [2, 1,  1,  '1/2',  1,  1],
            'Lazada': [1,  1,  1,  '1/2',  1, '1/2' ],
            'Bukalapak': [2, 2, 2, 1,  '1/2',  1],
            'Blibli': [2, 1,  1,  2, 1,  1],
            'Orami': [1, 1, 2, 1,  1,  1], 
        })
        st.dataframe(table2)
    
    elif selected_column == 'Kriteria Gratis Ongkir Dibandingkan dengan Alternatif E-Commerce':   
        table3 = pd.DataFrame({
            'Gratis Ongkir': ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami'],
            'Shopee': [1,  '1/2',  '1',  '1/2',  1, '1/2'],
            'Tokopedia': [2, 1,  '1/2', 1, '1/2',  '1/2'],
            'Lazada': [1,  2,  1,  '1/2',  1, '1/2' ],
            'Bukalapak': [2, 1, 2, 1,  1, '1/2'],
            'Blibli': [1, 2,  1,  1, 1,  '1/2'],
            'Orami': [2, 2, 2, 2,  2,  1], 
        })
        st.dataframe(table3)
        
    elif selected_column == 'Kriteria Review & Rating Dibandingkan dengan Alternatif E-Commerce':   
        table4 = pd.DataFrame({
            'Review & rating': ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami'],
            'Shopee': [1,  1,  '1',  '1/2', '1/2', 1],
            'Tokopedia': [1, 1,  '1/2', 1, '1/2',  1],
            'Lazada': [1,  2,  1,  '1/2',  1, '1/2' ],
            'Bukalapak': [2, 1, 2, 1,  1, 1],
            'Blibli': [2, 2,  1,  1, 1,  '1/2'],
            'Orami': [1, 1, 2, 1,  2,  1], 
        })
        st.dataframe(table4)
    
    elif selected_column == 'Kriteria Jumlah Produk Terjual Dibandingkan dengan Alternatif E-Commerce':   
        table5 = pd.DataFrame({
            'Jumlah produk terjual': ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami'],
            'Shopee': [1,  '1/2',  '1',  '1/2', '1/2', 1],
            'Tokopedia': [2, 1,  '1/2', 1, '1/2',  1],
            'Lazada': [1,  2,  1,  '1/2',  1, '1/2' ],
            'Bukalapak': [2, 1, 2, 1,  1, 1],
            'Blibli': [2, 2,  1,  1, 1,  '1/2'],
            'Orami': [1, 1, 2, 1,  2,  1],
        })
        st.dataframe(table5)
        
    elif selected_column == 'Kriteria Keaslian Produk Dibandingkan dengan Alternatif E-Commerce':   
        table6 = pd.DataFrame({
            'Keaslian produk': ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami'],
            'Shopee': [1,  '1/2',  '1',  '1/2', '1/2', 1],
            'Tokopedia': [2, 1,  '1/2', 1, 1,  1],
            'Lazada': [1,  2,  1,  '1/2',  1, 1 ],
            'Bukalapak': [2, 1, 2, 1,  '1/2', 1],
            'Blibli': [2, 1,  1,  2, 1,  '1/2'],
            'Orami': [1, 1, 1, 1,  2,  1],
        })
        st.dataframe(table6)
    
    elif selected_column == 'Kriteria Skala Toko Dibandingkan dengan Alternatif E-Commerce':   
        table7 = pd.DataFrame({
            'Skala Toko': ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami'],
            'Shopee': [1,  '1/2',  '1/2',  '1/2', '1/2', '1/2'],
            'Tokopedia': [2, 1,  '1/2', '1/2', 1,  1],
            'Lazada': [2,  2,  1,  '1/2',  1, 1 ],
            'Bukalapak': [2, 2, 2, 1,  1, 1],
            'Blibli': [2, 1,  1,  1, 1,  1],
            'Orami': [2, 1, 1, 1,  1,  1],
        })
        st.dataframe(table7)

    # Menambahkan tombol "Hitung"
    if st.button("Hitung"):
    # Eksekusi rumus sesuai dengan pilihan pengguna setelah tombol "Hitung" diklik
        if selected_column == 'Pilih Perhitungan':
            st.write("Anda belum memilih perhitungan.")
        
        elif selected_column == 'Kriteria Faktor Pembelian':
            st.subheader('Hasil Normalisasi Data: ')
            st.table(pd.DataFrame(result_normalized_matrix, columns=['Harga', 'Gratis Ongkir', 'Review dan Rating', 'Jumlah Produk Terjual', 'Keaslian Produk', 'Skala Toko']))
            st.subheader('Hasil Penjumlahan Per Kolom Pada Tabel Normalisasi Data: ')
            st.table(pd.DataFrame(result_sum, columns=['Harga', 'Gratis Ongkir', 'Review dan Rating', 'Jumlah Produk Terjual', 'Keaslian Produk',	'Skala Toko']))
           
            # Menampilkan vektor eigen dalam bentuk tabel menggunakan Streamlit
            st.subheader('Vektor Eigen:')
            st.table(pd.DataFrame(result_eigen_values, columns=['Nilai Vektor Eigen']))
            st.subheader('Hasil Penjumlahan Vektor Eigen: ')
            st.table(pd.DataFrame(result_sum_eigen1, columns=['Hasil']))
          
            st.subheader('Hasil Perkalian Matriks Normalisasi dengan Nilai Vektor Eigen:')
            st.table(pd.DataFrame(result_hasil1, columns=['1', '2', '3', '4', '5', '6']))
            
            st.subheader('Dari perkalian tersebut didapatkan nilai Priority Vector sebagai berikut:')
            st.table(pd.DataFrame(result_vector, columns=['Priority Vector']))
            
            st.subheader('Setelah itu hasil perkalian nya dijumlahkan dan dibagi dengan nilai priority vector, sehingga didapatkan nilai berikut:')
            st.write(result_total)

            st.subheader('Lambda Maksimum:')
            st.write(result_lambda)

            st.subheader('Nilai CI:')
            st.write(result_ci)

            st.subheader('Nilai CR:')
            st.write(result_cr)

            st.subheader('Kesimpulan:')
            st.write(result_consistency)
            
        elif selected_column == 'Kriteria Harga Dibandingkan dengan Alternatif E-Commerce':
            st.subheader('Hasil Normalisasi Data: ')
            st.table(pd.DataFrame(result_normalized_matrix2, columns=['Harga', 'Gratis Ongkir', 'Review dan Rating', 'Jumlah Produk Terjual', 'Keaslian Produk', 'Skala Toko']))
            st.subheader('Hasil Penjumlahan Per Kolom Pada Tabel Normalisasi Data: ')
            st.table(pd.DataFrame(result_sum2, columns=['Harga', 'Gratis Ongkir', 'Review dan Rating', 'Jumlah Produk Terjual', 'Keaslian Produk',	'Skala Toko']))
           
            # Menampilkan vektor eigen dalam bentuk tabel menggunakan Streamlit
            st.subheader('Vektor Eigen:')
            st.table(pd.DataFrame(result_eigen_values2, columns=['Nilai Vektor Eigen']))
            st.subheader('Hasil Penjumlahan Vektor Eigen: ')
            st.table(pd.DataFrame(result_sum_eigen2, columns=['Hasil']))
            
            st.subheader('Hasil Perkalian Matriks Normalisasi dengan Nilai Vektor Eigen:')
            st.table(pd.DataFrame(result_hasil2, columns=['1', '2', '3', '4', '5', '6']))
            
            st.subheader('Dari perkalian tersebut didapatkan nilai Priority Vector sebagai berikut:')
            st.table(pd.DataFrame(result_vector2, columns=['Priority Vector']))
            
            st.subheader('Setelah itu hasil perkalian nya dijumlahkan dan dibagi dengan nilai priority vector, sehingga didapatkan nilai berikut:')
            st.write(result_total2)

            st.subheader('Lambda Maksimum:')
            st.write(result_lambda2)

            st.subheader('Nilai CI:')
            st.write(result_ci2)

            st.subheader('Nilai CR:')
            st.write(result_cr2)

            st.subheader('Kesimpulan:')
            st.write(result_consistency2)
            
        elif selected_column == 'Kriteria Gratis Ongkir Dibandingkan dengan Alternatif E-Commerce':
            st.subheader('Hasil Normalisasi Data: ')
            st.table(pd.DataFrame(result_normalized_matrix3, columns=['Harga', 'Gratis Ongkir', 'Review dan Rating', 'Jumlah Produk Terjual', 'Keaslian Produk', 'Skala Toko']))
            st.subheader('Hasil Penjumlahan Per Kolom Pada Tabel Normalisasi Data: ')
            st.table(pd.DataFrame(result_sum3, columns=['Harga', 'Gratis Ongkir', 'Review dan Rating', 'Jumlah Produk Terjual', 'Keaslian Produk',	'Skala Toko']))
           
            # Menampilkan vektor eigen dalam bentuk tabel menggunakan Streamlit
            st.subheader('Vektor Eigen:')
            st.table(pd.DataFrame(result_eigen_values3, columns=['Nilai Vektor Eigen']))
            st.subheader('Hasil Penjumlahan Vektor Eigen: ')
            st.table(pd.DataFrame(result_sum_eigen3, columns=['Hasil']))
            
            st.subheader('Hasil Perkalian Matriks Normalisasi dengan Nilai Vektor Eigen:')
            st.table(pd.DataFrame(result_hasil3, columns=['1', '2', '3', '4', '5', '6']))
            
            st.subheader('Dari perkalian tersebut didapatkan nilai Priority Vector sebagai berikut:')
            st.table(pd.DataFrame(result_vector3, columns=['Priority Vector']))
            
            st.subheader('Setelah itu hasil perkalian nya dijumlahkan dan dibagi dengan nilai priority vector, sehingga didapatkan nilai berikut:')
            st.write(result_total3)

            st.subheader('Lambda Maksimum:')
            st.write(result_lambda3)

            st.subheader('Nilai CI:')
            st.write(result_ci3)

            st.subheader('Nilai CR:')
            st.write(result_cr3)

            st.subheader('Kesimpulan:')
            st.write(result_consistency3)
            
        elif selected_column == 'Kriteria Review & Rating Dibandingkan dengan Alternatif E-Commerce':
            st.subheader('Hasil Normalisasi Data:')
            st.table(pd.DataFrame(result_normalized_matrix4, columns=['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami']))
            st.subheader('Hasil Penjumlahan Per Kolom Pada Tabel Normalisasi Data: ')
            st.table(pd.DataFrame(result_sum4, columns=['Harga', 'Gratis Ongkir', 'Review dan Rating', 'Jumlah Produk Terjual', 'Keaslian Produk',	'Skala Toko']))
           
            # Menampilkan vektor eigen dalam bentuk tabel menggunakan Streamlit
            st.subheader('Vektor Eigen:')
            st.table(pd.DataFrame(result_eigen_values4, columns=['Nilai Vektor Eigen']))
            st.subheader('Hasil Penjumlahan Vektor Eigen: ')
            st.table(pd.DataFrame(result_sum_eigen4, columns=['Hasil']))
            
            st.subheader('Hasil Perkalian Matriks Normalisasi dengan Nilai Vektor Eigen:')
            st.table(pd.DataFrame(result_hasil4, columns=['1', '2', '3', '4', '5', '6']))
            
            st.subheader('Dari perkalian tersebut didapatkan nilai Priority Vector sebagai berikut:')
            st.table(pd.DataFrame(result_vector4, columns=['Priority Vector']))
            
            st.subheader('Setelah itu hasil perkalian nya dijumlahkan dan dibagi dengan nilai priority vector, sehingga didapatkan nilai berikut:')
            st.write(result_total4)

            st.subheader('Lambda Maksimum:')
            st.write(result_lambda4)

            st.subheader('Nilai CI:')
            st.write(result_ci4)

            st.subheader('Nilai CR:')
            st.write(result_cr4)

            st.subheader('Kesimpulan:')
            st.write(result_consistency4)
            
        elif selected_column == 'Kriteria Jumlah Produk Terjual Dibandingkan dengan Alternatif E-Commerce':
             st.subheader('Hasil Normalisasi Data:')
             st.table(pd.DataFrame(result_normalized_matrix5, columns=['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami']))
             st.subheader('Hasil Penjumlahan Per Kolom Pada Tabel Normalisasi Data: ')
             st.table(pd.DataFrame(result_sum5, columns=['Harga', 'Gratis Ongkir', 'Review dan Rating', 'Jumlah Produk Terjual', 'Keaslian Produk',	'Skala Toko']))
           
            # Menampilkan vektor eigen dalam bentuk tabel menggunakan Streamlit
             st.subheader('Vektor Eigen:')
             st.table(pd.DataFrame(result_eigen_values5, columns=['Nilai Vektor Eigen']))
             st.subheader('Hasil Penjumlahan Vektor Eigen: ')
             st.table(pd.DataFrame(result_sum_eigen5, columns=['Hasil']))
            
             st.subheader('Hasil Perkalian Matriks Normalisasi dengan Nilai Vektor Eigen:')
             st.table(pd.DataFrame(result_hasil5, columns=['1', '2', '3', '4', '5', '6']))
            
             st.subheader('Dari perkalian tersebut didapatkan nilai Priority Vector sebagai berikut:')
             st.table(pd.DataFrame(result_vector5, columns=['Priority Vector']))
            
             st.subheader('Setelah itu hasil perkalian nya dijumlahkan dan dibagi dengan nilai priority vector, sehingga didapatkan nilai berikut:')
             st.write(result_total5)

             st.subheader('Lambda Maksimum:')
             st.write(result_lambda5)

             st.subheader('Nilai CI:')
             st.write(result_ci5)

             st.subheader('Nilai CR:')
             st.write(result_cr5)

             st.subheader('Kesimpulan:')
             st.write(result_consistency5)
            
        elif selected_column == 'Kriteria Keaslian Produk Dibandingkan dengan Alternatif E-Commerce':
             st.subheader('Hasil Normalisasi Data:')
             st.table(pd.DataFrame(result_normalized_matrix6, columns=['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami']))
             st.subheader('Hasil Penjumlahan Per Kolom Pada Tabel Normalisasi Data: ')
             st.table(pd.DataFrame(result_sum6, columns=['Harga', 'Gratis Ongkir', 'Review dan Rating', 'Jumlah Produk Terjual', 'Keaslian Produk',	'Skala Toko']))
           
            # Menampilkan vektor eigen dalam bentuk tabel menggunakan Streamlit
             st.subheader('Vektor Eigen:')
             st.table(pd.DataFrame(result_eigen_values6, columns=['Nilai Vektor Eigen']))
             st.subheader('Hasil Penjumlahan Vektor Eigen: ')
             st.table(pd.DataFrame(result_sum_eigen6, columns=['Hasil']))
            
             st.subheader('Hasil Perkalian Matriks Normalisasi dengan Nilai Vektor Eigen:')
             st.table(pd.DataFrame(result_hasil6, columns=['1', '2', '3', '4', '5', '6']))
            
             st.subheader('Dari perkalian tersebut didapatkan nilai Priority Vector sebagai berikut:')
             st.table(pd.DataFrame(result_vector6, columns=['Priority Vector']))
            
             st.subheader('Setelah itu hasil perkalian nya dijumlahkan dan dibagi dengan nilai priority vector, sehingga didapatkan nilai berikut:')
             st.write(result_total6)

             st.subheader('Lambda Maksimum:')
             st.write(result_lambda6)

             st.subheader('Nilai CI:')
             st.write(result_ci6)

             st.subheader('Nilai CR:')
             st.write(result_cr6)

             st.subheader('Kesimpulan:')
             st.write(result_consistency6)
            
            
        elif selected_column == 'Kriteria Skala Toko Dibandingkan dengan Alternatif E-Commerce':
             st.subheader('Hasil Normalisasi Data:')
             st.table(pd.DataFrame(result_normalized_matrix7, columns=['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami']))
             st.subheader('Hasil Penjumlahan Per Kolom Pada Tabel Normalisasi Data: ')
             st.table(pd.DataFrame(result_sum7, columns=['Harga', 'Gratis Ongkir', 'Review dan Rating', 'Jumlah Produk Terjual', 'Keaslian Produk',	'Skala Toko']))
           
            # Menampilkan vektor eigen dalam bentuk tabel menggunakan Streamlit
             st.subheader('Vektor Eigen:')
             st.table(pd.DataFrame(result_eigen_values7, columns=['Nilai Vektor Eigen']))
             st.subheader('Hasil Penjumlahan Vektor Eigen: ')
             st.table(pd.DataFrame(result_sum_eigen7, columns=['Hasil']))
            
             st.subheader('Hasil Perkalian Matriks dengan Nilai Vektor Eigen:')
             st.table(pd.DataFrame(result_hasil7, columns=['1', '2', '3', '4', '5', '6']))
            
             st.subheader('Dari perkalian tersebut didapatkan nilai Priority Vector sebagai berikut:')
             st.table(pd.DataFrame(result_vector7, columns=['Priority Vector']))
            
             st.subheader('Setelah itu hasil perkalian nya dijumlahkan dan dibagi dengan nilai priority vector, sehingga didapatkan nilai berikut:')
             st.write(result_total7)

             st.subheader('Lambda Maksimum:')
             st.write(result_lambda7)

             st.subheader('Nilai CI:')
             st.write(result_ci7)

             st.subheader('Nilai CR:')
             st.write(result_cr7)

             st.subheader('Kesimpulan:')
             st.write(result_consistency7)
            

            
elif option == 'Chart':
    st.write("""## Diagram Pie Kriteria dan Alternatif""")  # menampilkan judul halaman

    # Data untuk Kriteria
    data_kriteria = {'Kategori': ['Gratis Ongkir', 'Review Rating', 'Jumlah Produk Terjual', 'Keaslian Produk', 'Skala Toko'],
                     'Nilai': [0.205, 0.203, 0.123, 0.069, 0.050]}

    df_kriteria = pd.DataFrame(data_kriteria)

    # Data untuk Harga
    data_harga = {'Kategori': ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami'],
                  'Nilai': [0.226, 0.161, 0.204, 0.133, 0.132, 0.144]}
    
    df_harga = pd.DataFrame(data_harga)

    # Data untuk Gratis Ongkir
    data_gratisongkir = {'Kategori': ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami'],
                         'Nilai': [0.226, 0.208, 0.181, 0.141, 0.158, 0.086]}
    
    df_gratisongkir = pd.DataFrame(data_gratisongkir)
    
    # Data untuk Review dan Rating
    data_rera = {'Kategori': ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami'],
                  'Nilai': [0.202, 0.208, 0.183, 0.128, 0.146, 0.133]}
    
    df_rera = pd.DataFrame(data_rera)
    
    # Data untuk Jumlah Produk Terjual
    data_terjual = {'Kategori': ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami'],
                  'Nilai': [0.227, 0.188, 0.184, 0.124, 0.145, 0.132]}
    
    df_terjual = pd.DataFrame(data_terjual)
    
    # Data untuk Keaslian Produk
    data_keaslian = {'Kategori': ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami'],
                  'Nilai': [0.227, 0.163, 0.166, 0.148, 0.151, 0.145]}
    
    df_keaslian = pd.DataFrame(data_keaslian)
    
    # Data untuk Skala Toko
    data_skala = {'Kategori': ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak', 'Blibli', 'Orami'],
                  'Nilai': [0.280, 0.181, 0.144, 0.115, 0.140, 0.140]}
    
    df_skala = pd.DataFrame(data_skala)


    # Fungsi untuk membuat diagram pie
    def create_pie_chart(dataframe, column_name, title):
        labels = dataframe[column_name]
        values = dataframe['Nilai']
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title(title)
        return fig

    # Tampilkan diagram pie untuk Kriteria
    st.pyplot(create_pie_chart(df_kriteria, 'Kategori', 'Diagram Pie Kriteria'))

    # Tampilkan diagram pie untuk Harga
    st.pyplot(create_pie_chart(df_harga, 'Kategori', 'Diagram Pie Harga'))

    # Tampilkan diagram pie untuk Gratis Ongkir
    st.pyplot(create_pie_chart(df_gratisongkir, 'Kategori', 'Diagram Pie Gratis Ongkir'))

    # Tampilkan diagram pie untuk Review dan Rating
    st.pyplot(create_pie_chart(df_rera, 'Kategori', 'Diagram Pie Review dan Rating'))

    # Tampilkan diagram pie untuk Produk Terjual
    st.pyplot(create_pie_chart(df_terjual, 'Kategori', 'Diagram Pie Produk Terjual'))

    # Tampilkan diagram pie untuk Keaslian Produk
    st.pyplot(create_pie_chart(df_keaslian, 'Kategori', 'Diagram Pie Keaslian Produk'))

    # Tampilkan diagram pie untuk Skala Toko
    st.pyplot(create_pie_chart(df_skala, 'Kategori', 'Diagram Pie Skala Toko'))
