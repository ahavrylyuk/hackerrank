{-
fib = zipWith (+) (0:fib) (0:1:fib)

main = do
  n <- readLn :: IO Int
  putStrLn $ show $ (fib !! (n - 1))
fib n = 
    if n <= 2 then n - 1
    else fib (n - 1) + fib (n - 2)

main = do
    input <- getLine
    print . fib . (read :: String -> Int) $ input
fib 1 = 0
fib 2 = 1
fib n = fib' 0 1 3
    where        
        fib' x' x i
            | i == n = x' + x
            | otherwise = fib' x (x + x') (i + 1)
-}

fib = (map fib' [0..] !!)
  where fib' n
          | n == 0 = 0
          | n == 1 = 1 
          | otherwise = fib (n - 2) + fib (n - 1)
