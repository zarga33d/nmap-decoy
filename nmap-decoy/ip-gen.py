import random

def generate_random_ip():
    # توليد IP عشوائي في النطاق 1.0.0.1 إلى 254.254.254.254 (بتجنب 0 و255 في كل أوكتت)
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def generate_ip_lists(num_lists, ips_per_list):
    generated_ips = set()

    total_ips_needed = num_lists * ips_per_list

    while len(generated_ips) < total_ips_needed:
        ip = generate_random_ip()
        if ip not in generated_ips:
            generated_ips.add(ip)

    ips_list = list(generated_ips)

    for i in range(num_lists):
        start = i * ips_per_list
        end = start + ips_per_list
        chunk = ips_list[start:end]
        filename = f"decoy_part_{i+1}.txt"
        with open(filename, 'w') as f:
            f.write("\n".join(chunk) + "\n")
        print(f"Created {filename} with {len(chunk)} unique random IPs.")

if __name__ == "__main__":
    num_lists = int(input("كم عدد القوائم التي تريد إنشاؤها؟ "))
    ips_per_list = int(input("كم عدد الـ IPs في كل قائمة (حتى 127)؟ "))
    if ips_per_list > 127:
        print("تحذير: الحد الأقصى المسموح به هو 127. سيتم استخدام 127 بدلاً من ذلك.")
        ips_per_list = 127

    generate_ip_lists(num_lists, ips_per_list)
