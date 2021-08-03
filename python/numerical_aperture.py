import optical_fiber
D=int(input("enter the value of D:"))
L=int(input("enter the value of L:"))

Na = optical_fiber.n_a(D,L)

print("The numerical aperture is:%d"%Na)
