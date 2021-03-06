# Coupon Collector's Problem 赠券收集问题

The program calculates mathematical expectation, variation, probability density function, cumulative distribution function and confidence interval of coupon collector's problem.
本程序计算赠券收集问题的数学期望、方差、概率密度函数、累积分布函数和置信区间。  

## 运行方法
使用命令行
```bash
python3 main.py
```
即可运行图形界面。（由于matplotlib不支持中文，所以本程序不得不采用全英文界面）  
本程序实时计算结果，所以滑动卡片种类（number of types）滚动条时，卡顿是正常现象。
## 应用举例
1. **集齐十二星座的前任**  
假设某人集齐了十二星座的前任，求前任数量的数学期望和方差。如下图所示，把卡片种类（number of types）设置为12，置信水平（confidence level）设置为95%，即可得到前任数量的数学期望是37.238528138528146个，方差是188.11810779408185，我们有95%的把握认为前任数量大于18个且小于71个，或有95%的把握认为前任数量少于63个，或有95%的把握认为前任数量多于19个。
![程序截图](https://raw.githubusercontent.com/shxuy/CouponCollectorsProblem/master/img/DefaultScreenshot.png)
通过滑动置信水平（confidence level）滚动条，可得我们有10%的把握少于23个，有50%的把握少于35个，有90%的把握少于55个,有99%的把握少于82个。  
拓展练习：假设某人集齐了星期一至星期日的前任，求前任数量的数学期望，方差和99%置信区间。  
注意：四种血型、三十四省级行政区等其它划分人群分布不均，所以不能使用本程序，需要用\int_{0}^{\infty}1-\prod_{i=1}^{n}(1-e^{-p_it})dt（左侧公式采用Latex格式书写，其中n是划分种类，p_i是第i种划分所占的比例(0<p_i<1)）计算数学期望，用蒙特卡洛方法估算置信区间。  
2. **小浣熊干脆面中的水浒卡**  
1999年，小浣熊公司聘请专业画师绘制水浒卡片，附赠在干脆面里。卡片一共108种，对应水浒一百单八将。把卡片种类（number of types）设置为108，置信水平（confidence level）设置为99%，即可得到抽取次数的数学期望是568.5086927404586次，方差是18510.500719793843，我们有99%的把握认为集齐卡片所需的抽取次数少于998次，也有99%的把握认为集齐卡片所需的抽取次数多于349次。
3. **旺仔牛奶五十六民族新包装**  
2019年，旺仔牛奶为挽回销量的下滑趋势，以盲盒形式出售56款民族罐，也就是说打开箱子前根本不知道里面牛奶盒的包装长什么样。把卡片种类（number of types）设置为56，置信水平（confidence level）设置为95%，即可得到购买箱数的数学期望是258.2422838678609箱，方差是4844.767973767466，我们有95%的把握认为需要购买的箱数大于158箱，小于428箱。
## 计算正确性证明
赠券收集问题的数学期望、方差、概率密度函数、累积分布函数的公式推导和详细证明见本目录下的“赠券收集问题.docx”或者“赠券收集问题.pdf”。
