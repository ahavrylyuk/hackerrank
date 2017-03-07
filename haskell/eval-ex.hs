import Control.Monad
import System.IO
import Text.Printf

fac = product . flip take [1..]
solve x = 1 + sum (map (\t -> x ** fromIntegral t / fac(t)) [1..9]) 

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    forM_ [1..n] $ \a0  -> do
        x_temp <- getLine
        let x = read x_temp :: Double
        printf "%.4f\n" (solve x)  

