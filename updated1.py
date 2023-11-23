import streamlit as st
import pandas as pd
import numpy as np


#FUNCTION
def hitung_semua_rumus(df):
    # Menghitung jumlah dari setiap kolom
    result = df.sum()
    return result

def tabelkriteria():
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
    
    return normalized_matrix1, eigen_values1

# Memanggil fungsi tabelkriteria
result_normalized_matrix, result_eigen_values = tabelkriteria()

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
        'is_consistent': CR < 0.1
    }

    return hasil_matriks, sum_horizontal, total_sum, lambda_maks, CI, CR, result

# Panggil fungsi nilaicr untuk mendapatkan hasilnya
result_hasil1, result_vector, result_total, result_lambda, result_ci, result_cr, result_consistency = nilaicr()
    


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
    st.write("""# Implementasi Nilai dan Vektor Eigen untuk Menentukan Prioritas Faktor-Faktor Pembelian Barang dan Pemilihan E-Commerce""")  # menampilkan halaman utama
    st.write("""
    Web ini digunakan untuk melakukan perhitungan model keputusan dari faktor-faktor pembelian barang dan pemilihan e-commerce dengan menggunakan konsep matriks dan vektor eigen, dimana faktor-faktor ini bisa dihitung dengan menggunakan data dummy yang telah dibuat
    """)
elif option == 'Dataframe':
    st.write("""## Dataframe""")  # menampilkan judul halaman dataframe

    #DATA DUMMY
    df1 = pd.DataFrame({
        'Column 1': [1, 4, 2, 3, 4, 4],
        'Column 2': [0.25, 1, 2, 3, 3, 3],
        'Column 2': [0.5, 0.5, 1, 4, 3, 4],
        'Column 2': [0.33, 0.33, 0.25, 1, 3, 4],
        'Column 2': [0.25, 0.33, 0.33, 0.33, 1, 2],
        'Column 2': [0.25, 0.33, 0.25, 0.25, 0.5, 1]
    })

    # Menampilkan dataframe
    st.dataframe(df1)
    
    

    # Menambahkan dropdown di samping tabel
    selected_column = st.selectbox("Apa yang mau anda Hitung :",['Pilih Perhitungan', 'Kriteria faktor pembelian', 'Kriteria harga dibandingkan dengan e-commerce', 'Gratis ongkir', 'Review & rating', 'Jumlah produk terjual', 'Keaslian produk', 'Skala toko'], key='dropdown_column', help="Pilih yang ingin dihitung")
    
    if selected_column == 'Kriteria faktor pembelian':
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
       st.write(tabelkriteria)
              
    elif selected_column == 'Kriteria harga dibandingkan dengan e-commerce':   
        table2 = pd.DataFrame({
            'Harga': [1,  2,  1,  2,  2,  1 ],
            'Gratis Ongkir': [0.5, 1,  1,  2,  1,  1 ],
            'Review dan Rating': [1,  1,  1,  2,  1,  2 ],
            'Jumlah Produk Terjual': [0.5, 0.5, 0.5, 1,  2,  1],
            'Keaslina Produk': [0.5, 1,  1,  0.5, 1,  1],
            'Skala Toko': [1, 1, 0.5, 1,  1,  1], 
        })
        st.dataframe(table2)
    
    elif selected_column == 'Gratis ongkir':   
        table2 = pd.DataFrame({
            'Harga': [1,  2,  1,  2,  2,  1 ],
            'Gratis Ongkir': [0.5, 1,  1,  2,  1,  1 ],
            'Review dan Rating': [1,  1,  1,  2,  1,  2 ],
            'Jumlah Produk Terjual': [0.5, 0.5, 0.5, 1,  2,  1],
            'Keaslina Produk': [0.5, 1,  1,  0.5, 1,  1],
            'Skala Toko': [1, 1, 0.5, 1,  1,  1], 
        })
        st.dataframe(table2)
        
    elif selected_column == 'Review & rating':   
        table2 = pd.DataFrame({
            'Harga': [1,  2,  1,  2,  2,  1 ],
            'Gratis Ongkir': [0.5, 1,  1,  2,  1,  1 ],
            'Review dan Rating': [1,  1,  1,  2,  1,  2 ],
            'Jumlah Produk Terjual': [0.5, 0.5, 0.5, 1,  2,  1],
            'Keaslina Produk': [0.5, 1,  1,  0.5, 1,  1],
            'Skala Toko': [1, 1, 0.5, 1,  1,  1], 
        })
        st.dataframe(table2)
    
    elif selected_column == 'Jumlah produk terjual':   
        table2 = pd.DataFrame({
            'Harga': [1,  2,  1,  2,  2,  1 ],
            'Gratis Ongkir': [0.5, 1,  1,  2,  1,  1 ],
            'Review dan Rating': [1,  1,  1,  2,  1,  2 ],
            'Jumlah Produk Terjual': [0.5, 0.5, 0.5, 1,  2,  1],
            'Keaslina Produk': [0.5, 1,  1,  0.5, 1,  1],
            'Skala Toko': [1, 1, 0.5, 1,  1,  1], 
        })
        st.dataframe(table2)
        
    elif selected_column == 'Keaslian produk':   
        table2 = pd.DataFrame({
            'Harga': [1,  2,  1,  2,  2,  1 ],
            'Gratis Ongkir': [0.5, 1,  1,  2,  1,  1 ],
            'Review dan Rating': [1,  1,  1,  2,  1,  2 ],
            'Jumlah Produk Terjual': [0.5, 0.5, 0.5, 1,  2,  1],
            'Keaslina Produk': [0.5, 1,  1,  0.5, 1,  1],
            'Skala Toko': [1, 1, 0.5, 1,  1,  1], 
        })
        st.dataframe(table2)
    
    elif selected_column == 'Skala toko':   
        table2 = pd.DataFrame({
            'Harga': [1,  2,  1,  2,  2,  1 ],
            'Gratis Ongkir': [0.5, 1,  1,  2,  1,  1 ],
            'Review dan Rating': [1,  1,  1,  2,  1,  2 ],
            'Jumlah Produk Terjual': [0.5, 0.5, 0.5, 1,  2,  1],
            'Keaslian Produk': [0.5, 1,  1,  0.5, 1,  1],
            'Skala Toko': [1, 1, 0.5, 1,  1,  1], 
        })
        st.dataframe(table2)
       
    #kumpulan matriks untuk dihitung
      
    # Menambahkan checkbox "Hitung Semua"
    hitung_semua = st.checkbox("Hitung Semua", key='hitung_semua_checkbox', help="Centang untuk menghitung semua perhitungan")
     
    
    
    
    
    # Menambahkan tombol "Hitung"
    if st.button("Hitung"):
    # Eksekusi rumus sesuai dengan pilihan pengguna setelah tombol "Hitung" diklik
        if hitung_semua:
            result = hitung_semua_rumus(df1)
            st.write("Hasil perhitungan untuk Semua Kolom:")
            st.write(result) 
        
        elif selected_column == 'Pilih Perhitungan':
            st.write("Anda belum memilih perhitungan.")
        
        elif selected_column == 'Kriteria faktor pembelian':
            st.subheader('Matriks Normalisasi:')
            st.table(pd.DataFrame(result_normalized_matrix, columns=['Harga', 'Gratis Ongkir', 'Review dan Rating', 'Jumlah Produk Terjual', 'Keaslian Produk', 'Skala Toko']))

            # Menampilkan vektor eigen dalam bentuk tabel menggunakan Streamlit
            st.subheader('Vektor Eigen:')
            st.table(pd.DataFrame(result_eigen_values, columns=['Nilai Vektor Eigen']))
            
            st.subheader('Hasil Perkalian Matriks Normalisasi dengan Nilai Vektor Eigen:')
            st.table(pd.DataFrame(result_hasil1, columns=['1', '2', '3', '4', '5', '6']))
            
            st.subheader('Priority Vector:')
            st.table(pd.DataFrame(result_vector, columns=['Priority Vector']))
            
            st.subheader('Total Sum:')
            st.write(result_total)

            st.subheader('Lambda Maksimum:')
            st.write(result_lambda)

            st.subheader('Nilai CI:')
            st.write(result_ci)

            st.subheader('Nilai CR:')
            st.write(result_cr)

            st.subheader('Konsistensi:')
            st.write(result_consistency)
            
            
 
            
        
            
elif option == 'Chart':
    st.write("""## Draw Charts""")  # menampilkan judul halaman

    # Membuat variabel chart data yang berisi data dari dataframe
    
    # Data berupa angka acak yang di-generate menggunakan numpy
    
    # Data terdiri dari 2 kolom dan 20 baris
    chart_data = pd.DataFrame(
        np.random.randn(20, 2),
        columns=['a', 'b']
    )

    # Menampilkan data dalam bentuk chart
    st.line_chart(chart_data)

    # Menampilkan data dalam bentuk tabel
    st.dataframe(chart_data)
