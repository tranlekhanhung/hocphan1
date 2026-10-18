import random
#Bài 1 
so_xuc_xac = random.randint(1, 6)
print("Kết quả tung xúc xắc là:", so_xuc_xac)
#Bài 2 
ten = input("nhập họ và tên")
chu_may_man_cua_ban = random.choice(ten)
print ("Chữ may mắn của bạn là", chu_may_man_cua_ban)
#Bài 3 
tinh_tu = ("Cool", "Fast", "Smart", "Happy")
danh_tu = ("Tiger", "Eagle", "Panda", "Coder")
tinh_tu_duoc_chon = random.choice(tinh_tu)
danh_tu_duoc_chon = random.choice(danh_tu)
print ("Username gợi ý cho bạn:", tinh_tu_duoc_chon+danh_tu_duoc_chon)
#Bài 4
so_thu_nhat= random.randint(0, 9)
so_thu_hai= random.randint(0, 9)
so_thu_ba= random.randint(0, 9)
so_thu_tu= random.randint(0, 9)
print ("Mã PIN ngẫu nhiên của bạn", str(so_thu_nhat)+str(so_thu_hai)+str(so_thu_ba)+str(so_thu_tu))
#Bài 5
n = int(input("Nhập độ dài N: "))
kho_ky_tu = "abcdefghijklmnopqrstuvwxyz"
danh_sach_ky_tu = random.choices(kho_ky_tu, k=n)
mat_khau = "".join(danh_sach_ky_tu)
print("Mật khẩu của bạn:", mat_khau)
#Bài 6
cau_cua_ban = input("Nhập câu của bạn:")
ds = cau_cua_ban.split()
random.shuffle(ds)
print ("câu của bạn sau khi xáo trộn: ", end="")
for v in ds:
    print(v,end=" ")
#Bài 7
n = int(input("Nhập độ dài N: "))
kho_ky_tu_viet_thuong = "abcdefghijklmnopqrstuvwxyz"
kho_ky_tu_viet_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
kho_chu_so = "0,1,2,3,4,5,6,7,8,9"
kho_ky_tu_dac_biet = "!@#$%^&*"
kho_tong = kho_ky_tu_viet_thuong + kho_ky_tu_viet_hoa + kho_chu_so + kho_ky_tu_dac_biet
danh_sach_ky_tu = random.choices(kho_tong, k=n)
mat_khau_an_toan = "".join(danh_sach_ky_tu)
print("Mật khẩu an toàn:", mat_khau_an_toan)
#Bài 8
n = int(input("Nhập độ dài N: "))
kho_ky_tu_viet_thuong = "abcdefghijklmnopqrstuvwxyz"
kho_ky_tu_viet_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
kho_chu_so = "0,1,2,3,4,5,6,7,8,9"
kho_ky_tu_dac_biet = "!@#$%^&*"
kho_tong = kho_ky_tu_viet_thuong + kho_ky_tu_viet_hoa + kho_chu_so + kho_ky_tu_dac_biet
mat_khau_1 = random.choices(kho_tong, k=n)
mat_khau_2 = random.choices(kho_tong, k=n)
mat_khau_3 = random.choices(kho_tong, k=n)
goi_y_1 = "".join(mat_khau_1)
goi_y_2 = "".join(mat_khau_2)
goi_y_3 = "".join(mat_khau_3)
print ("--- GỢI Ý MẬT KHẨU ---")
print("1:", goi_y_1)
print("2:", goi_y_2)
print("3:", goi_y_3)
#Bài 9
