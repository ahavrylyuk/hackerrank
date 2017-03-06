step = 0.001
y :: [Int] -> [Int] -> Double -> Double
y a b x = sum . map (\(a, b) -> fromIntegral a * x ** fromIntegral b) $ zip a b

area :: [Int] -> [Int] -> [Double] -> Double
area a b = sum . map (\x -> y a b x * step)
volume a b = sum . map (\x -> y a b x ** 2 * pi * step)

solve :: Int -> Int -> [Int] -> [Int] -> [Double]
--solve l r a b = area a b (takeWhile (<r) $ iterate (+step) l)
solve l r a b = map (\f -> f a b [fromIntegral l, fromIntegral l + step.. fromIntegral r]) [area, volume] 
