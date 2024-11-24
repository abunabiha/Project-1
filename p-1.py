import subprocess  # Mengimpor modul subprocess untuk menjalankan perintah sistem

def get_ifconfig_info():
    """
    Fungsi ini digunakan untuk mendapatkan informasi jaringan menggunakan perintah ifconfig.
    """
    try:
        # Menjalankan perintah ifconfig dan menangkap outputnya
        result = subprocess.run(['ifconfig'], capture_output=True, text=True, check=True)
        return result.stdout  # Mengembalikan output dari perintah ifconfig
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

if __name__ == "__main__":
    """
    Blok ini memastikan bahwa kode di dalamnya hanya dijalankan jika file ini adalah program utama.
    Di sini, kita mencetak informasi jaringan yang diperoleh dari fungsi get_ifconfig_info().
    """
    ifconfig_info = get_ifconfig_info()  # Mendapatkan informasi jaringan
    print(ifconfig_info)  # Mencetak informasi jaringan