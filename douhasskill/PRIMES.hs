-- haskell prime number finder.
bound = 10
domain = [1,3..bound]
yield_mults x a = [x*y | y <- [2..a]]
itertest a | a == bound = print "a = bound"
           | a /= bound = do
               print a
               itertest (a+1)

main :: IO()
main = do
  itertest 0
  print "Hello World!, program compiled :)"
