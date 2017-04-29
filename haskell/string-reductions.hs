reduce = reduce' ['a'..'z']
  where
    reduce' _ [] = []
    reduce' memo (x:xs)
      | memo == rest = reduce' rest xs
      | otherwise = x:reduce' rest xs
      where
        rest = filter (/= x) memo

main = getLine >>= putStrLn . reduce
