sumOfPowers = sumOfPowers' 1
  where
    sumOfPowers' curr x n
      | val == 0 = 1
      | val < 0 = 0
      | otherwise = sumOfPowers' next val n + sumOfPowers' next x n
      where
        val = x - curr ^ n
        next = curr + 1

main = do
 x <- readLn :: IO Int
 n <- readLn :: IO Int
 print $ sumOfPowers x n
