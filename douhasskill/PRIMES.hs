-- unoptimized prime number finder, haskell. 
bound = 10000
domain = drop 1 [1,3..bound]
mnet = [x*y | x <- domain, y <- [a | a <- [2..((length domain))]], (x*y <= last domain) && (mod (x*y) 2 /= 0)] 
tau = [x | x <- domain, not(any (x==) mnet)]
main :: IO()
main = do
  print tau
  
