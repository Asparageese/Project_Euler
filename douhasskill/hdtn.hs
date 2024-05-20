hdtn :: Int
hdtn = 10
yBool a = if even a then 0 else 1
test = yBool hdtn
hdtnF = fromIntegral hdtn::Float


main :: IO()
main = do
  print "main pass"
  print hdtn
  print test
  print hdtnF
