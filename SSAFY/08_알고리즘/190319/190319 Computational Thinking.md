# 190319 Computational Thinking

등...비...수열...의... 합...

pseudo



```pseudocode
merge(n, p, r){
	if(p < r) then {			
		q <= (p + q) / 2;		p, q 중간 지점 계산
		mergeSort(n, p, q);		왼쪽 부분 정렬
		mergeSort(n, q+1, r);	오른쪽 부분 정렬
		merge(n, p, q, r)		합병
		
merge(n, p, q, r){
	정렬되어 있는 두 배열(왼쪽, 오른쪽)을 합하여 정렬된 배열 하나를 만듦
}
```





### 6. 동적 프로그래밍

```python
coin = [6, 4, 1] # 내가 사용할 수 있는 동전의 종류
path = [0] * 100
# ans = 0xffffff

def coinChange(n): # k : 높이, n : 거스름돈 금액
    if n == 0:
        # global ans
        # ans = min(ans, k)
        # print(path[:k])
        # return 
        return 0
   	if memo[n]:
        return memo[n]
    MIN = 0xffffff
    for val in coin;
    	if val > :
            continue
    	# path[k] = val
	    # coinChange(k + 1, n - val)
        ret = coinChange(n - val)
		MIN = min(MIN, ret)
    memo[n] = MIN + 1
    return memo[n]

print(coinChange(80))


def coinChange(n):
    
    for i in range(1, n + 1):
        for val in coin:
            if val > i:
                continue
                ret = memo[i - val]
                MIN = min(MIN, ret)
            memo[i] = MIN + 1
    return memo[n]

print(coinChange(80))
```



문제 풀 때

백트래킹 => 재귀호출 => 메모이제이션 => 반복