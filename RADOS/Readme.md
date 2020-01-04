

## 1. Rados Command

- Get danh sách các pool 
```
rados lspools
```

- Xem danh sách các object có trên hệ thống ( trên tất cả namespace)
```
rados -p default.rgw.buckets.index ls --all 
```

- Get content của một object 
```
rados -p default.rgw.buckets.data get 0acc5636-e314-42d2-b1ba-1f3410072f20.114114.21_1dacd2ef1adf4dadb2572c9bf557fd39.jpg  output.txt
```
