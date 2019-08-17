s1=input("请输入你的身高(m)：\n")
s2=input("请输入你的体重(kg)：\n")
n=float(s2)/(float(s1)**2)
print("您的BMI值为：{0:.2f}".format(n))
if n<18.5:
    print("属于偏瘦")
elif 18.5<=n<=24:
    print("属于正常")
elif 24<n<=25:
    print("国际标准属于正常，国内标准属于偏胖")
elif 25<n<=30:
    print("属于偏胖")
else:
    print("属于肥胖")
print("国际BMI值建议为18.5-25")
print("国内BMI值建议为18.5-24")
