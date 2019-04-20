
## 1. Pool

- Placement groups (PGs)  : tập hợp các object trong một pool dựa vào object placement and object metadata từ client request. 
![](http://docs.ceph.com/docs/mimic/_images/ditaa-1fde157d24b63e3b465d96eb6afea22078c85a90.png)

- Khi khởi tạo một cluster mới, Ceph sẽ sử dụng default pool  để lưu trữ dữ liệu . Một cung có thể cung cấp :
    - Resilience : chỉ định số OSD có thể ở status fail ở mode replicas . Ví dụ với   replicated pools sẽ xác định số lượng số OSD =3 , tương ứng với số bản copi = 3, nêu số ODS ở status fail nhỏ hơn 2, pool sẽ ngừng hoạt động. 
    - Placement Groups : chỉ số lượng placement groups  cho pool 
    - CRUSH Rules: khi đặt dữ liiệu vào một rule , vị trí của dữ liệu và bản sao trong cụm được điều chỉnh dựa vào các rule
    - Snapshots : khả năng snapshot nhanh 1 pool


    