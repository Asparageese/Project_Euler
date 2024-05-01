-- haskell prime number finder.
bound = 7
domain = drop 1 [1,3..bound] 
z = [map (tau *) m | m<-[2..(bound/2)],tau<-[domain]]


main :: IO()
main = do
  print "BEGINING MAIN CALL"
  print domain
  print z
