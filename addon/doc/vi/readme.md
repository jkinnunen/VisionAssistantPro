# Tài liệu hướng dẫn Vision Assistant Pro

**Vision Assistant Pro** là trợ lý AI đa năng nâng cao dành cho NVDA. Add-on này tận dụng các mô hình Gemini của Google để cung cấp các khả năng đọc màn hình thông minh, dịch thuật, soạn thảo bằng giọng nói và phân tích tài liệu.

*Add-on này được phát hành cho cộng đồng nhằm vinh danh Ngày Quốc tế Người khuyết tật.*

## 1. Thiết lập & Cấu hình

Truy cập **Menu NVDA > Tùy chọn > Cài đặt > Vision Assistant Pro**.

* **Khóa API:** Bắt buộc. Bạn có thể nhập nhiều khóa (phân tách bằng dấu phẩy hoặc xuống dòng). Trợ lý sẽ tự động luân chuyển giữa các khóa nếu một khóa hết hạn mức (quota).
* **Mô hình AI:** Chọn giữa các mô hình **Flash** (Nhanh nhất/Miễn phí), **Lite**, hoặc **Pro** (Trí tuệ cao).
* **Proxy URL:** Không bắt buộc. Sử dụng nếu Google bị chặn ở khu vực của bạn. Đây phải là một địa chỉ web đóng vai trò làm cầu nối tới API Gemini.
* **Công cụ OCR:** Chọn giữa **Chrome (Nhanh)** để có kết quả nhanh chóng hoặc **Gemini (Có định dạng)** để giữ nguyên bố cục và nhận dạng bảng biểu tốt hơn.
* **Giọng đọc TTS:** Chọn kiểu giọng đọc ưu thích để tạo tệp âm thanh từ các trang tài liệu.
* **Hoán đổi thông minh:** Tự động hoán đổi ngôn ngữ nếu văn bản nguồn khớp với ngôn ngữ đích.
* **Kết quả trực tiếp:** Bỏ qua cửa sổ chat và thông báo phản hồi của AI trực tiếp bằng giọng nói.
* **Tích hợp bộ nhớ tạm:** Tự động sao chép phản hồi của AI vào bộ nhớ tạm.

## 2. Lớp lệnh & Phím tắt

Để tránh xung đột phím tắt, add-on này sử dụng một **Lớp lệnh**.

1. Nhấn **NVDA + Shift + V** (Phím chính) để kích hoạt lớp lệnh (bạn sẽ nghe thấy một tiếng bíp).
2. Thả các phím, sau đó nhấn một trong các phím đơn sau:

| Phím | Chức năng | Mô tả |
| --- | --- | --- |
| **T** | Trình dịch thông minh | Dịch văn bản dưới con trỏ điều hướng hoặc đoạn đang chọn. |
| **Shift + T** | Dịch bộ nhớ tạm | Dịch nội dung hiện có trong bộ nhớ tạm. |
| **R** | Tinh chỉnh văn bản | Tóm tắt, Sửa ngữ pháp, Giải thích hoặc chạy **Lệnh tùy chỉnh**. |
| **V** | Mô tả đối tượng | Mô tả đối tượng điều hướng hiện tại. |
| **O** | Mô tả toàn màn hình | Phân tích bố cục và nội dung của toàn bộ màn hình. |
| **Shift + V** | Phân tích video trực tuyến | Phân tích video **YouTube**, **Instagram**, hoặc **Twitter (X)** qua đường dẫn. |
| **D** | Trình đọc tài liệu | Trình đọc nâng cao cho PDF và hình ảnh với khả năng chọn phạm vi trang. |
| **F** | Nhận diện tệp (OCR) | Nhận diện văn bản trực tiếp từ các tệp hình ảnh, PDF hoặc TIFF được chọn. |
| **A** | Phiên âm âm thanh | Phiên âm các tệp MP3, WAV hoặc OGG thành văn bản. |
| **C** | Giải CAPTCHA | Chụp và giải CAPTCHA trên màn hình hoặc đối tượng điều hướng. |
| **S** | Soạn thảo thông minh | Chuyển đổi giọng nói thành văn bản. Nhấn để bắt đầu ghi âm, nhấn lần nữa để dừng/nhập văn bản. |
| **L** | Báo cáo trạng thái | Thông báo tiến trình hiện tại (ví dụ: "Đang quét...", "Đang chờ"). |
| **U** | Kiểm tra cập nhật | Kiểm tra phiên bản mới nhất của add-on trên GitHub thủ công. |
| **H** | Trợ giúp lệnh | Hiển thị danh sách tất cả các phím tắt có sẵn trong lớp lệnh. |

### 2.1 Phím tắt trong Trình đọc tài liệu (Bên trong trình xem)

Khi một tài liệu được mở thông qua lệnh **D**:

* **Ctrl + PageDown:** Chuyển sang trang tiếp theo (thông báo số trang).
* **Ctrl + PageUp:** Chuyển về trang trước (thông báo số trang).
* **Alt + A:** Mở hộp thoại chat để đặt câu hỏi về tài liệu.
* **Alt + R:** Buộc quét lại trang hiện tại hoặc tất cả các trang bằng công cụ Gemini.
* **Alt + G:** Tạo và lưu tệp âm thanh chất lượng cao (WAV) từ nội dung.
* **Alt + S / Ctrl + S:** Lưu văn bản đã trích xuất dưới dạng tệp TXT hoặc HTML.

## 3. Lệnh tùy chỉnh & Biến

Bạn có thể tạo các lệnh AI tùy chỉnh mạnh mẽ trong phần Cài đặt bằng định dạng: `Tên:Nội dung lệnh` (phân tách nhiều lệnh bằng dấu `|` hoặc xuống dòng).

### Các biến hỗ trợ

| Biến | Mô tả | Loại đầu vào |
| --- | --- | --- |
| `[selection]` | Văn bản đang được chọn | Văn bản |
| `[clipboard]` | Nội dung bộ nhớ tạm | Văn bản |
| `[screen_obj]` | Chụp ảnh đối tượng điều hướng | Hình ảnh |
| `[screen_full]` | Chụp ảnh toàn màn hình | Hình ảnh |
| `[file_ocr]` | Chọn tệp ảnh/PDF để trích xuất văn bản | Hình ảnh, PDF, TIFF |
| `[file_read]` | Chọn tài liệu để đọc | TXT, Code, PDF |
| `[file_audio]` | Chọn tệp âm thanh để phân tích | MP3, WAV, OGG |

### Ví dụ về Lệnh tùy chỉnh

* **OCR nhanh:** `OCR của tôi:[file_ocr]`
* **Dịch hình ảnh:** `Dịch ảnh:Trích xuất văn bản từ hình ảnh này và dịch sang tiếng Anh. [file_ocr]`
* **Phân tích âm thanh:** `Tóm tắt âm thanh:Nghe bản ghi này và tóm tắt các điểm chính. [file_audio]`
* **Gỡ lỗi mã nguồn:** `Gỡ lỗi:Tìm lỗi trong đoạn mã này và giải thích chúng: [selection]`

---

**Lưu ý:** Cần có kết nối internet để sử dụng tất cả các tính năng AI. Các tài liệu nhiều trang và tệp TIFF được xử lý tự động.

## Các thay đổi trong 4.0.1

* **Trình đọc tài liệu nâng cao:** Trình xem mới mạnh mẽ cho PDF và hình ảnh với khả năng chọn phạm vi trang, xử lý trong nền và điều hướng `Ctrl+PageUp/Down` mượt mà.
* **Trình đơn phụ mới trong Tools:** Thêm một trình đơn phụ "Vision Assistant" riêng biệt trong menu Công cụ của NVDA để truy cập nhanh hơn vào các tính năng chính, cài đặt và tài liệu hướng dẫn.
* **Tùy biến linh hoạt:** Giờ đây bạn có thể chọn công cụ OCR và giọng đọc TTS ưa thích trực tiếp từ bảng cài đặt.
* **Hỗ trợ nhiều khóa API:** Thêm hỗ trợ cho nhiều khóa API Gemini. Bạn có thể nhập mỗi dòng một khóa hoặc phân tách bằng dấu phẩy trong cài đặt.
* **Công cụ OCR thay thế:** Giới thiệu một công cụ OCR mới để đảm bảo nhận diện văn bản đáng tin cậy ngay cả khi đạt giới hạn hạn mức API Gemini.
* **Luân chuyển khóa API thông minh:** Tự động chuyển sang và ghi nhớ khóa API hoạt động nhanh nhất để vượt qua giới hạn hạn mức.
* **Tài liệu sang MP3/WAV:** Tích hợp khả năng tạo và lưu tệp âm thanh chất lượng cao ở cả định dạng MP3 (128kbps) và WAV trực tiếp trong trình đọc.
* **Hỗ trợ Instagram Stories:** Thêm khả năng mô tả và phân tích Instagram Stories bằng đường dẫn của chúng.
* **Hỗ trợ TikTok:** Giới thiệu hỗ trợ cho video TikTok, cho phép mô tả hình ảnh đầy đủ và phiên âm âm thanh của các clip.
* **Thiết kế lại hộp thoại cập nhật:** Giao diện hỗ trợ tiếp cận mới với khung văn bản có thể cuộn để đọc rõ ràng các thay đổi phiên bản trước khi cài đặt.
* **Trạng thái & UX hợp nhất:** Tiêu chuẩn hóa các hộp thoại tệp trong toàn bộ add-on và cải tiến lệnh 'L' để báo cáo tiến độ theo thời gian thực.

## Các thay đổi trong 3.6.0

* **Hệ thống trợ giúp:** Thêm lệnh trợ giúp (`H`) trong Lớp lệnh để cung cấp danh sách tất cả các phím tắt và chức năng của chúng một cách dễ dàng.
* **Phân tích video trực tuyến:** Mở rộng hỗ trợ bao gồm cả video trên **Twitter (X)**. Đồng thời cải thiện khả năng phát hiện đường dẫn và độ ổn định để có trải nghiệm đáng tin cậy hơn.
* **Đóng góp dự án:** Thêm hộp thoại ủng hộ (donation) tùy chọn cho những người dùng muốn hỗ trợ các bản cập nhật trong tương lai và sự phát triển liên tục của dự án.

## Các thay đổi trong 3.5.0

* **Lớp lệnh:** Giới thiệu hệ thống Lớp lệnh (mặc định: `NVDA+Shift+V`) để nhóm các phím tắt dưới một phím chính duy nhất. Ví dụ, thay vì nhấn `NVDA+Control+Shift+T` để dịch, giờ đây bạn nhấn `NVDA+Shift+V` sau đó nhấn `T`.
* **Phân tích video trực tuyến:** Thêm tính năng mới để phân tích video YouTube và Instagram trực tiếp bằng cách cung cấp đường dẫn.

## Các thay đổi trong 3.1.0

* **Chế độ kết quả trực tiếp:** Thêm tùy chọn để bỏ qua hộp thoại chat và nghe phản hồi của AI trực tiếp qua giọng nói để có trải nghiệm nhanh hơn và liền mạch hơn.
* **Tích hợp bộ nhớ tạm:** Thêm cài đặt mới để tự động sao chép phản hồi AI vào bộ nhớ tạm.

## Các thay đổi trong 3.0

* **Ngôn ngữ mới:** Thêm bản dịch tiếng **Ba Tư** và tiếng **Việt**.
* **Mở rộng mô hình AI:** Sắp xếp lại danh sách lựa chọn mô hình với các tiền tố rõ ràng (`[Free]`, `[Pro]`, `[Auto]`) để giúp người dùng phân biệt giữa các mô hình miễn phí và các mô hình giới hạn hạn mức (trả phí). Thêm hỗ trợ cho **Gemini 3.0 Pro** và **Gemini 2.0 Flash Lite**.
* **Độ ổn định của soạn thảo:** Cải thiện đáng kể độ ổn định của Soạn thảo thông minh. Thêm kiểm tra an toàn để bỏ qua các đoạn âm thanh ngắn hơn 1 giây, ngăn chặn AI "ảo giác" và các lỗi trống.
* **Xử lý tệp:** Khắc phục lỗi tải lên các tệp có tên không phải tiếng Anh bị thất bại.
* **Tối ưu hóa câu lệnh:** Cải thiện logic Dịch thuật và cấu trúc kết quả Thị giác (Vision).

## Các thay đổi trong 2.9

* **Thêm bản dịch tiếng Pháp và tiếng Thổ Nhĩ Kỳ.**
* **Xem có định dạng:** Thêm nút "Xem bản có định dạng" trong hộp thoại chat để xem cuộc hội thoại với định dạng chuẩn (Tiêu đề, Chữ đậm, Mã nguồn) trong một cửa sổ duyệt văn bản tiêu chuẩn.
* **Cài đặt Markdown:** Thêm tùy chọn mới "Làm sạch Markdown trong Chat" trong Cài đặt. Bỏ chọn mục này cho phép người dùng thấy cú pháp Markdown thô (ví dụ: `**`, `#`) trong cửa sổ chat.
* **Quản lý hộp thoại:** Khắc phục lỗi các cửa sổ "Tinh chỉnh văn bản" hoặc cửa sổ chat mở ra nhiều lần hoặc không thể tập trung chính xác.
* **Cải tiến UX:** Tiêu chuẩn hóa tiêu đề các hộp thoại tệp thành "Mở" và loại bỏ các thông báo giọng nói dư thừa (ví dụ: "Đang mở trình đơn...") để có trải nghiệm mượt mà hơn.

## Các thay đổi trong 2.8

* Thêm bản dịch tiếng Ý.
* **Báo cáo trạng thái:** Thêm lệnh mới (NVDA+Control+Shift+I) để thông báo trạng thái hiện tại của add-on (ví dụ: "Đang tải lên...", "Đang phân tích...").
* **Xuất HTML:** Nút "Lưu nội dung" trong các hộp thoại kết quả giờ đây lưu kết quả dưới dạng tệp HTML có định dạng, giữ nguyên các kiểu như tiêu đề và chữ đậm.
* **Giao diện Cài đặt:** Cải thiện bố cục bảng Cài đặt với các nhóm có thể tiếp cận tốt hơn.
* **Mô hình mới:** Thêm hỗ trợ cho gemini-flash-latest và gemini-flash-lite-latest.
* **Ngôn ngữ:** Thêm tiếng Nepal vào danh sách các ngôn ngữ được hỗ trợ.
* **Logic trình đơn Tinh chỉnh:** Khắc phục một lỗi nghiêm trọng khiến các lệnh "Tinh chỉnh văn bản" thất bại nếu ngôn ngữ giao diện NVDA không phải là tiếng Anh.
* **Soạn thảo:** Cải thiện khả năng phát hiện sự im lặng để ngăn kết quả văn bản không chính xác khi không có tiếng nói đầu vào.
* **Cài đặt cập nhật:** Mục "Kiểm tra cập nhật khi khởi động" hiện bị tắt theo mặc định để tuân thủ các chính sách của Cửa hàng Add-on.
* Làm sạch mã nguồn.

## Các thay đổi trong 2.7

* Di chuyển cấu trúc dự án sang Mẫu Add-on chính thức của NV Access để tuân thủ tốt hơn các tiêu chuẩn.
* Triển khai logic tự động thử lại cho các lỗi HTTP 429 (Giới hạn hạn mức) để đảm bảo độ tin cậy khi lưu lượng truy cập cao.
* Tối ưu hóa các câu lệnh dịch thuật để có độ chính xác cao hơn và xử lý logic "Hoán đổi thông minh" tốt hơn.
* Cập nhật bản dịch tiếng Nga.

## Các thay đổi trong 2.6

* Thêm hỗ trợ bản dịch tiếng Nga (Cảm ơn nvda-ru).
* Cập nhật các thông báo lỗi để cung cấp phản hồi mô tả chi tiết hơn về kết nối.
* Thay đổi ngôn ngữ đích mặc định thành tiếng Anh.

## Các thay đổi trong 2.5

* Thêm lệnh Nhận diện tệp (OCR) gốc (NVDA+Control+Shift+F).
* Thêm nút "Lưu cuộc trò chuyện" vào các hộp thoại kết quả.
* Triển khai hỗ trợ bản địa hóa đầy đủ (i18n).
* Di chuyển phản hồi âm thanh sang mô-đun âm báo gốc của NVDA.
* Chuyển sang sử dụng Gemini File API để xử lý các tệp PDF và âm thanh tốt hơn.
* Khắc phục lỗi crash khi dịch văn bản có chứa dấu ngoặc nhọn.

## Các thay đổi trong 2.1.1

* Khắc phục lỗi biến [file_ocr] hoạt động không chính xác trong các Lệnh tùy chỉnh.

## Các thay đổi trong 2.1

* Tiêu chuẩn hóa tất cả các phím tắt sử dụng tổ hợp NVDA+Control+Shift để loại bỏ các xung đột với bố cục Laptop của NVDA và các phím nóng hệ thống.

## Các thay đổi trong 2.0

* Triển khai hệ thống Tự động cập nhật tích hợp.
* Thêm Bộ nhớ tạm dịch thông minh để truy xuất tức thì các văn bản đã dịch trước đó.
* Thêm Bộ nhớ hội thoại để tinh chỉnh kết quả theo ngữ cảnh trong các hộp thoại chat.
* Thêm lệnh Dịch bộ nhớ tạm riêng biệt (NVDA+Control+Shift+Y).
* Tối ưu hóa các câu lệnh AI để ép buộc nghiêm ngặt kết quả đầu ra theo ngôn ngữ đích.
* Khắc phục lỗi crash do các ký tự đặc biệt trong văn bản đầu vào.

## Các thay đổi trong 1.5

* Thêm hỗ trợ cho hơn 20 ngôn ngữ mới.
* Triển khai Hộp thoại tinh chỉnh tương tác cho các câu hỏi tiếp nối.
* Thêm tính năng Soạn thảo thông minh gốc.
* Thêm danh mục "Vision Assistant" vào hộp thoại Cử chỉ nhập liệu của NVDA.
* Khắc phục các lỗi COMError trong các ứng dụng cụ thể như Firefox và Word.
* Thêm cơ chế tự động thử lại cho các lỗi máy chủ.

## Các thay đổi trong 1.0

* Phiên bản phát hành đầu tiên.
