
## 1. Pool

- Placement groups (PGs)  : tập hợp các object trong một pool dựa vào object placement and object metadata từ client request. 
![](http://docs.ceph.com/docs/mimic/_images/ditaa-1fde157d24b63e3b465d96eb6afea22078c85a90.png)

- Khi khởi tạo một cluster mới, Ceph sẽ sử dụng default pool  để lưu trữ dữ liệu . Một cung có thể cung cấp :
    - Resilience : chỉ định số OSD có thể ở status fail ở mode replicas . Ví dụ với   replicated pools sẽ xác định số lượng số OSD =3 , tương ứng với số bản copi = 3, nêu số ODS ở status fail nhỏ hơn 2, pool sẽ ngừng hoạt động. 
    - Placement Groups : chỉ số lượng placement groups  cho pool 
    - CRUSH Rules: khi đặt dữ liiệu vào một rule , vị trí của dữ liệu và bản sao trong cụm được điều chỉnh dựa vào các rule
    - Snapshots : khả năng snapshot nhanh 1 pool


    
### 4.2 : . Data Durability

- Kịch bản phục hồi dữ liệu trên một placement group có số bản copy 3 : 
    - Sau khi một OSD bị fail, bản sao của các object trên  placement group sẽ bị giảm xuống 2
    - Ceph bắt đầu thực hiện khôi phục object trên placment group bằng cách tìm một OSD mới, để thực hiện copy bản thứ 3 của object trên OSD này
    - Các OSD khác nằm trong placement group sẽ trở về trạng fail cho đến khi OSD mới được copy object hoàn thành
    - Ceph tiếp tục chọn một OSD khác và tiếp tục sao chép đến khi đạt số repli number mong muốn
    - OSD thứ 3 sẽ đi về trạng thái fail trước khi thực hiện recovery thành cồng

-