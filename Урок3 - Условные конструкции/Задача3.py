productOne = int(input())
productTwo = int(input())
productThree = int(input())
Amount = productOne + productTwo + productThree
if ((productOne < productTwo) and (productOne < productThree) and (productTwo < productThree)):
    print('Акция!', Amount/2)
elif ((productOne > productTwo) and (productOne > productThree) and (productTwo > productThree)):
    print('Акция', Amount/4)
else:
    print('К оплате:',Amount)