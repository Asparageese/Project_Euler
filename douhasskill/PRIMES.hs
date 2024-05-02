-- haskell prime number finder.
-- no parallel computations dand no statistical methods.
-- to be added in prime number finder version 2, the goal is to push
-- the search bound to 1,000,000 and easily preform computations. 
bound = 1000
domain = drop 1 [1,3..bound]
mnet = [x*y | x <- domain, y <- [a | a <- [2..((length domain))]], (x*y <= last domain) && (mod (x*y) 2 /= 0)] 
tau = [x | x <- domain, not(any (x==) mnet)]
main :: IO()
main = do
  print tau
  
