import Control.Monad
import Data.List

main :: IO ()
main = do
  numTests <- liftM read getLine
  replicateM_ numTests $ do
    line <- getLine
    let rots = tail $ zipWith (++) (tails line) (inits line)
    putStrLn $ unwords rots

{-
import Control.Monad
import Data.List

rotate lst = tail lst ++ [head lst]

rotateAll n line = do
    if n == 0
        then []
        else do
            let next = rotate line
            next:rotateAll (n-1) next

main = do
    n <- readLn :: IO Int
    forM_ [0..n-1] $ \_ -> do
        line <- getLine
        putStrLn $ intercalate " " (rotateAll (length line) line)
-}
