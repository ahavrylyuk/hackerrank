compress s = comp s 1
  where 
    comp [] n = []
    comp [x] n = if n > 1 then x:show n else [x]
    comp (x:y:xs) n
      | x == y = comp (x:xs) (n + 1)
      | x /= y && n > 1 = x:show n ++ comp (y:xs) 1
      | otherwise = x:comp (y:xs) 1

main = do
  line <- getLine
  putStrLn $ compress line
