print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
def sieve_of_eratosthenes(limit):
    """Hàm tìm các số nguyên tố nhỏ hơn limit bằng thuật toán Sieve of Eratosthenes."""
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False  # 0 và 1 không phải là số nguyên tố

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    # Tạo danh sách các số nguyên tố
    primes = [i for i in range(limit) if is_prime[i]]
    return tuple(primes)

# Tạo tuple P chứa các số nguyên tố nhỏ hơn 1 triệu
P = sieve_of_eratosthenes(1000000)

# In ra số lượng và một số số nguyên tố đầu tiên
print(f"Số lượng số nguyên tố nhỏ hơn 1 triệu: {len(P)}")
print("Một số số nguyên tố đầu tiên:", P[:10])  # In ra 10 số nguyên tố đầu tiên
