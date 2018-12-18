# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

# js成功!:
# var mu = 2;
# var zi = 1;
# var r = 0; // 结果
# for(var i = 0; i < 20; i++) {
#     console.log(`${mu} / ${zi}`)
#     r += mu / zi;
#     [mu, zi] = [mu + zi, mu];
# }

# console.log('r:', r);








