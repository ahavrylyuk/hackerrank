dedup res [] = res
dedup res (x:xs)
  | x `elem` res = dedup res xs 
  | otherwise = dedup (res ++ [x]) xs

main = do
  line <- getLine
  putStrLn $ dedup "" line
