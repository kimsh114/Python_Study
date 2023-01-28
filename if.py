temp = int(input('오늘 기온은 어때요?'))

if temp >= 30:
    print('너무 덥네요 나가지 마요')
elif 18 <= temp < 30:
    print('산책하기 좋은 날씨네요')
elif 10<=temp<18:
    print('쌀쌀하니 겉옷을 챙기세요.')
else:
    print('추우니 옷을 따뜻하게 입으세요')
