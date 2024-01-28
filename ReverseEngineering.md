## Searchcall

The searchcall looks as follows: 

```
curl 'https://www.wollplatz.de/wolle?s=Stylecraft' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8' \
  -H 'cookie: Next-VisitorCodeV2=RfDtv6sof0pfId5WyabVtSfkeN4yYUIuzIE17qdYafxpsBJXS0t6ujySca7d8BnUSPP8zJGuwHTlHFsC; __cf_bm=Zk7dNCpIy.eYDQgPtcsAuzZvZ2o8VZtvpLj8BDhjpCQ-1706277435-1-AWLHfKN9x5CvpmoMJSWYe0acHSl3wqjWQyxXCSfodyY8+aW3RB2jnUw6IWhFGVm3s6Zq1fAt/zeSsNOMbNIaRyM=; _cfuvid=Orl4HheFzMhYGXPJSPPAnz6zDsKdl09LAuG82vhiPT4-1706277435992-0-604800000; cf_clearance=S2c0PoPaJgdL5S2ZfR829meuhNMF4yAZ1fbNjcRE0ak-1706277437-1-AQ/w9u4IvznKytz03lxmLJuwm/aSoDSh7JN2ueUvKKqTjw+T1BanUPdfcSN1OFJD7Imk6YjTK08QJ3I6RKUjlKc='
```

The response is a html file.

Inside in the div which describes one product, there is the link to the productdescription page. This link can be used to access the availability-information: 

```
curl 'https://www.wollplatz.de/wolle/drops/drops-puna-uni-colour' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8' \
  -H 'cookie: Next-VisitorCodeV2=RfDtv6sof0pfId5WyabVtSfkeN4yYUIuzIE17qdYafxpsBJXS0t6ujySca7d8BnUSPP8zJGuwHTlHFsC; _cfuvid=Orl4HheFzMhYGXPJSPPAnz6zDsKdl09LAuG82vhiPT4-1706277435992-0-604800000; __cf_bm=NhE9E_dqTqh7lr6zCCNPVvTnMqlaQo7LVLCRdBIzJhk-1706455622-1-ARrkoXHyWtayGENfs3yhG40u20XG6x7n1vIPwubpk325pNq7J1lAGtcFAd1zYCtYNla/pYVyBURiQ1B8m8W85Sg=; cf_clearance=cKJCvvU8kMoLoobzL257s4w9ZEN1_ZYZMUwR3Td0LK8-1706455622-1-Ad7EkwuTe+f0iSrrPkyeyTglkNbEjnomaYbq9ffz4LV2+pzQRX20TtM0EcyZFuuEXTe+uwRcNav5JnOaJR5bkPc=' \
  ```