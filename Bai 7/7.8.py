print("Vũ Mạnh Cường")
print("235752021610030")
def write_list_to_file(filename, data_list):
    try:
        # Mở tệp để ghi thêm nội dung (chế độ 'a' giúp bảo tồn nội dung cũ)
        with open(filename, 'a', encoding='utf-8') as file:
            for item in data_list:
                file.write(f"{item}\n")  # Ghi từng phần tử của danh sách vào tệp
        
        # In thông báo thành công
        print(f"Nội dung đã được ghi vào tệp '{filename}'.")
        
        # Đọc và in nội dung trong tệp sau khi ghi
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("\nNội dung trong tệp:")
            print(content)  # In ra nội dung tệp

    except Exception as e:
        print(f"Có lỗi xảy ra khi ghi vào tệp: {e}")

def main():
    # Nhập tên tệp
    filename = input("Nhập tên tệp (bao gồm phần mở rộng, ví dụ: 'data.txt'): ")
    
    # Dữ liệu để ghi vào tệp
    data_list = ['anh', 'yeu', 'em', 'nhieu', 'lam']
    
    # Gọi hàm ghi và in nội dung
    write_list_to_file(filename, data_list)

if __name__ == "__main__":
    main()

