selections _ [] = [[]]
selections target (x:xs) =
  sel ++ map (x:) sel
  where sel = selections target xs

sumsTo = sumsTo' 0
  where
    sumsTo' _ _ [] = False
    sumsTo' s target (x:xs)
      | null xs && s' == target = True
      | s' > target = False
      | otherwise = sumsTo' s' target xs
      where s' = s + x

powersOf n x = takeWhile (<=x) $ map (^n) [1..]
sumOfPowers x n = filter (sumsTo x) $ selections x $ powersOf n x

main = do
 x <- readLn :: IO Int
 n <- readLn :: IO Int
 print $ length $ sumOfPowers x n
