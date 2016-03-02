def bouquets(narcissus_price, tulip_price, rose_price, summ):
    count = 0
    max_narcissus = int(summ/narcissus_price);
    max_tulip = int(summ/tulip_price);
    max_rose = int(summ/rose_price);
    for i in range(max_narcissus+1):
        if  i*narcissus_price > summ:
            break
        for j in range(max_tulip+1):
            if  (i*narcissus_price + j*tulip_price) > summ :
                break
            for k in range(max_rose+1):
                if (i * narcissus_price + j* tulip_price + k * rose_price) <= summ:
                    if (i+j+k) % 2:
                        count += 1;
    return count;
print bouquets(1, 1, 1, 5)
print bouquets(2,3,4,10)
print bouquets(15.5,4.1,5.99,21.75)
print bouquets(21.25,13.6,10.5,100)
