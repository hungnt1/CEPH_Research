

## 1. AIO CEPH

- Tiêu chí của CEPH
    - tất cả thành phần phải có khả năng mở rộng
    - không một process, server, hoặc các thành phần khác có thể trở thành một điểm failure trong hệ thống
    - giải pháp phải là dựa trên ứng dựng, mã nguồn mở, và khả năng thích khi triên nhiều môi trường cũng như phần cứng
    - Khả năng chạy trên các phần cứng có sẵn thay vì sử dụng các phần cứng chuyên dụng
    - Các thành phần trong cụm có khả năng tự quản lý khi có thể

- Thay vì sử dụng metadata table mỗi lần client request lên hệ thống, CEPH sử dụng thuật toán CRUSH để xác định được nơi mà dữ liệu xắp xếp và có thể  được đặt ở đâu . CRUSH cho phép client kết nối trực tiếp đên các OSD thay vì sử dụng các centralized hay broken .

- CRUSH chứa một bản bồ về các thiết bị vật lý được quản lý bởi cụm bao gồmn các driver, node, pool, network, rack.... . CRUSH cho phép dữ liệu được phân tán và copy qua các failure domain giúp dữ liệu được đảm bảo 2 tính chất : bền vững và sẵn sàng. 


- CEPH bao gồm các daemon : 
    - RADOS
    - Monitors (MONs)
    - OSDs
    - Ceph Manager
    - RGW

- CEPH CLIENT bao gồm :
    - Block
    - Ojbect 
    - File



