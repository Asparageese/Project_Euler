hdtn :: Int
hdtn = 20
hdtnF = fromIntegral hdtn::Float
yBool a = if even a then 0 else 1
yBnds a hnum
  | a == 0 = hnum/2.0
  | otherwise = hnum/3.0
fSet a = if a == 0 then [2..(yBnds(yBool hdtn) hdtnF)] else [1,3..(yBnds(yBool hdtn) hdtnF)]
test = fSet (yBool hdtn)

main :: IO()
main = do
  print "main pass"
  print hdtn
  print hdtnF
  print test
