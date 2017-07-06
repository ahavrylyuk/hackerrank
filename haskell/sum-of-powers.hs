selections [] = [[]]
selections (x:xs) = selections xs ++ map (x:) (selections xs)

withSumOf target = filter (\xs -> sum xs == target)

powersOf n x = takeWhile (<=x) $ map (^n) [1..]

sumOfPowers x n = withSumOf x $ selections $ powersOf n x

main = do
 x <- readLn :: IO Int
 n <- readLn :: IO Int
 print $ length $ sumOfPowers x n