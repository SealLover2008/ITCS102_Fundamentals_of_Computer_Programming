amount = eval(input (
    "How Much money would you like to deposit? "
))

dot = amount // 1000 
dfo = amount % 1000 // 500
dtwo = amount %1000 %500 // 200
dhun = amount %1000 %500 %200 //100
dfif = amount %1000 %500 %200 %100 //50
dtwe = amount %1000 %500 %200 %100 %50 //20
dten = amount %1000 %500 %200 %100 %50 %20 //10
done = amount %1000 %500 %200 %100 %50 %20 %10 //1
print ("Amount to deposit", "₱",amount)
print ("THOUSANDS", "₱", dot)
print ("FIVE HUNDREDS", "₱",dfo)
print ("TWO HUNDREDS", "₱",dtwo)
print ("ONE HUNDREDS", "₱",dhun)
print ("FIFTIES","₱",dfif)
print ("TWENTIES","₱",dtwe)
print ("TENS","₱",dten)
print ("ONES","₱",done)
