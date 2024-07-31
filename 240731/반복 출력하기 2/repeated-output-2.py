def recursiveHelloWorld(n):
    if n == 0:
        return
    
    recursiveHelloWorld(n-1)
    print('HelloWorld')


cnt = int(input())
recursiveHelloWorld(cnt)