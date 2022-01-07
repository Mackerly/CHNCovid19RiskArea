# 写这个项目的时候的一点收获
主要是 javascript || nodejs 和 python 的对比

```javascript
// javascript || nodejs用到的库
let CryptoJS = require("crypto-js");
let SHA256 = require("crypto-js/sha256");

// javascript || nodejs 的语法
signatureHeader = SHA256(e + a + i + e).toString(CryptoJS.enc.Hex).toUpperCase();
```

```python
# python 用到的库
import hashlib

# python 的语法
signatureHeader = hashlib.sha256((e + a + i + e).encode("utf-8")).hexdigest().upper()
```
