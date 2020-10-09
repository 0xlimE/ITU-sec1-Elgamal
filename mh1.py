#Python script to solve 1-3 in mandatory handin 1 - El Gamal
#   Author: Emil Hørning. 0xlimE


#Helper function for finding the multiplicative inverse of a (mod m), this means that a * x mod m = 1 (where we want to find x)
#This helper function basically just bruteforces from 1-m, I dont think this is the best way
def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

g = 666
p = 6661
PK_bob = 2227 #Bobs public key g^x mod p


############Part 1: Send the message '2000' to bob.
print("Assignment part 1")
message = 2000
y = 201 # Random y
PK_alice = pow(g,y,p)
gxy = pow(PK_bob,y,p)
c = (gxy * message) % p

print("sending g^y:",PK_alice, "and c:",c,"from alice to bob")

#bob recovers message by calculating c/g^yx (we actually want c * (g^yx)^-1 (the multiplicative inverse))
gxy_1 = modInverse(gxy,p)
message_reconstructed = (c * gxy_1) %p
print("Bob recovers the secret",message_reconstructed)
print("")
print("-------------")
print("")


############Part 2: You are now Eve and intercept Alice’s encrypted message. Find  Bob’s private key and reconstruct Alice’s message
#Eve observes both g and p and bobs public key. Eves first step is to try and bruteforce the private key (bobs x), bruteforce from 1-p
print("Assignment part 2")
print("Hehe I am the evil eve and will try and bruteforce bobs private key")
for i in range(1,6662):
    if(pow(g,i,p) == PK_bob): 
        x = i
        print("Haha! I found bobs private key, it is x =",i)
        break

#Eve can calculate g^xy since g^y is given from alice
eve_gxy = pow(PK_alice,x,p)
#again get multiplicative inverse
eve_gxy_1 = modInverse(eve_gxy,p)
message_intercepted = (c*eve_gxy_1)%p
print("I find alice' message =",message_intercepted)
print("")
print("-------------")
print("")


############Part 3 You are now mallory and intercept alice encrypted message, you cannot find bobs private key, modify alice message so it says 6000 instead of 2000.
print("Assignment part 3")
print("I am mallory!, I see the ciphertext and will multiply it to make the number seem bigger!")
c = c*3 #We intercept just the ciphertext and multiply this by 3 to get 6000.
gxy_1 = modInverse(gxy,p)
message_reconstructed = (c * gxy_1) %p
print("Bob recovers the secret",message_reconstructed)
print("")
print("-------------")

