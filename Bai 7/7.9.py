print("Vũ Mạnh Cường")
print("235752021610030")
def copy_file_content(source_file, destination_file):
    try:
        # Mở tệp nguồn để đọc
        with open(source_file, 'r', encoding='utf-8') as source:
            # Đọc toàn bộ nội dung tệp nguồn
            content = source.read()

        # Mở tệp đích để ghi
        with open(destination_file, 'w', encoding='utf-8') as destination:
            # Ghi nội dung vào tệp đích
            destination.write(content)

        print(f"Nội dung từ tệp '{source_file}' đã được sao chép sang tệp '{destination_file}'.")

        # Đọc lại và in nội dung tệp đích
        with open(destination_file, 'r', encoding='utf-8') as destination:
            copied_content = destination.read()
            print("\nNội dung trong tệp đích:")
            print(copied_content)  # In ra nội dung của tệp đích
    
    except FileNotFoundError:
        print(f"Tệp nguồn '{source_file}' không tồn tại.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
    # Tên tệp nguồn và tệp đích đã được xác định trước
    source_file = "sothutu.txt"
    destination_file = "notepaddich.txt"

    # Sao chép nội dung từ tệp nguồn sang tệp đích và in ra kết quả
    copy_file_content(source_file, destination_file)

if __name__ == "__main__":
    main()
