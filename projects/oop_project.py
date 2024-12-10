from bank_accounts import *

Naksh = BankAccount(1000,"Naksh")
sara = BankAccount(5000,"Sara")

Naksh.getBalance()
sara.getBalance()

sara.deposit(500)

Naksh.withdraw(200)
Naksh.withdraw(10)

Naksh.transfer(1000,sara)

sara.transfer(10000,Naksh)

kim = InterestRewardsAcct(1000,"kim")

kim.getBalance()
kim.deposit(100)

kim.transfer(100,Naksh)

khloe = SavingsAcct(1000,"khloe")
khloe.getBalance()
khloe.deposit(100)
khloe.transfer(1000,sara)