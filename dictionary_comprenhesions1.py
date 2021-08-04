def run():
    dic = {i:round(i**0.5,2) for i in range(1,1001) if i**2 % 3 == 0}
    # for i in range(1,11):
    #     dic[i]=i**3
    #     # dic.setdefault(i,i**2)
    print(dic)


if __name__ == '__main__':
    run()