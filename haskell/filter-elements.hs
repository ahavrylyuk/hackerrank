import Control.Monad

filter' k arr = arr

main = do
  n <- readLn :: IO Int
  replicateM_ n $ do
    line <- getLine
    arrLine <- getLine
    let k = read (words line !! 1) :: Int
    let arr = map (\x -> read x :: Int) (words arrLine)
    putStrLn $ unwords (map (show) (filter' k arr))

