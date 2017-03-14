compress s = comp "" ' ' 0 s
  where
    comp :: [Char] -> Char -> Int -> [Char] -> [Char]
    comp res ch n []
      | n > 0 = res ++ show (n + 1)
      | otherwise = res
    comp res ch n (x:xs)
      | x == ch = comp res x (n + 1) xs
      | x /= ch && n > 0 = comp (res ++ (show (n + 1)) ++ [x]) x 0 xs
      | otherwise = comp (res ++ [x]) x 0 xs

main = do
  line <- getLine
  putStrLn $ compress line
