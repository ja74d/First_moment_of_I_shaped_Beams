
tf1 = float(input("tf1"))
tf2 = float(input("tf2"))
b = float(input("b"))
bf1 = float(input("bf1"))
tb = float(input("tb"))
bf2 = float(input("bf2"))

A1 = bf1 * tf1
A2 = tb * b
A3 = bf2 * tf2

X = (bf1)/2

Y1 = tf1/2
Y2 = (b/2) + tf1
Y3 = tf2/2 + b + tf1

print(X)

print(Y1)
print(Y2)
print(Y3)

fs1 = (A1*Y1 + A2*Y2 + A3*Y3)

Y = fs1/(A1+A2+A3)

print(Y)