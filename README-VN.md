# Herafi Testnet Scripts

Kho lưu trữ này chứa một bộ sưu tập các tập lệnh Python được thiết kế để tương tác với Herafi Testnet, một mạng lưới thử nghiệm blockchain hiệu suất cao. Tập lệnh chính, main.py, cung cấp giao diện dòng lệnh (CLI) thân thiện với người dùng để thực hiện các hoạt động khác nhau trên Herafi Testnet, chẳng hạn như nhận token từ faucet, hoán đổi token, quản lý vault, và cung cấp/rút thanh khoản. Được xây dựng bằng web3.py, các tập lệnh hỗ trợ thực thi không đồng bộ và cung cấp đầu ra song ngữ (tiếng Anh và tiếng Việt) để tăng cường tương tác với người dùng.

Faucet: [Herafi Testnet Faucet](https://testnet.herafi.xyz/faucet)

## Tổng quan về tính năng

### Tính năng chung

- **Hỗ trợ nhiều tài khoản**: Đọc khóa riêng từ `pvkey.txt` để thực hiện các hành động trên nhiều tài khoản.
- **CLI đầy màu sắc**: Sử dụng `colorama` để tạo đầu ra hấp dẫn về mặt hình ảnh với văn bản và đường viền có màu.
- **Thực thi không đồng bộ**: Được xây dựng bằng `asyncio` để tương tác blockchain hiệu quả.
- **Xử lý lỗi**: Bắt lỗi toàn diện cho các giao dịch blockchain và các vấn đề RPC.
- **Hỗ trợ song ngữ**: Hỗ trợ cả đầu ra tiếng Anh và tiếng Việt dựa trên lựa chọn của người dùng.


### Các tập lệnh được bao gồm

1. **Faucet**: Nhận token (WETH, CRV, SUSHI, UNI, USDC) từ faucet.
2. **Faucet Max**: Nhận số lượng tối đa token có sẵn (WETH, CRV, SUSHI, UNI, USDC, wBTC) từ faucet.
3. **Swap**: Hoán đổi token giữa hDEFI và các token khác (WETH, CRV, SUSHI, UNI, USDC).
4. **Vault**: Phát hành hoặc đổi token thông qua hợp đồng vault.
5. **Liquidity**: Cung cấp và rút thanh khoản từ các pool token.



## Điều kiện tiên quyết

Trước khi chạy các tập lệnh, hãy đảm bảo bạn đã cài đặt các phần sau:

- Python 3.8+
- `pip` (trình quản lý gói Python)
- **Phụ thuộc**: Cài đặt qua `pip install -r requirements.txt` (đảm bảo `web3.py`, `colorama`, `asyncio`, `aiohttp_socks`, `eth-account` và `inquirer` được bao gồm).
- **pvkey.txt**: Thêm khóa riêng (mỗi dòng một khóa) để tự động hóa ví.
- Truy cập vào Herafi Testnet RPC (ví dụ: https://sepolia.optimism.io).
- **proxies.txt** (tùy chọn): Thêm địa chỉ proxy cho các yêu cầu mạng, nếu cần.

## Cài đặt

1. **Clone this repository:**
- Mở cmd hoặc Shell, sau đó chạy lệnh:
```sh
git clone https://github.com/thog9/Herafi-testnet.git
```
```sh
cd Herafi-testnet
```
2. **Install Dependencies:**
- Mở cmd hoặc Shell, sau đó chạy lệnh:
```sh
pip install -r requirements.txt
```
3. **Prepare Input Files:**
- Mở `pvkey.txt`: Thêm khóa riêng của bạn (mỗi dòng một khóa) vào thư mục gốc.
```sh
nano pvkey.txt
```
```sh
nano proxies.txt
```
4. **Run:**
- Mở cmd hoặc Shell, sau đó chạy lệnh:
```sh
python main.py
```
- Chọn ngôn ngữ (Tiếng Việt/Tiếng Anh).

## Liên hệ

- **Telegram**: [thog099](https://t.me/thog099)
- **Channel**: [CHANNEL](https://t.me/thogairdrops)
- **Group**: [GROUP CHAT](https://t.me/thogchats)
- **X**: [Thog](https://x.com/thog099) 

