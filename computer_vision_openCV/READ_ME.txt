These are the steps that I have used to create reliable haar cascades.

$ opencv_createsamples -img image_to_recognize.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950

$ opencv_createsamples -info info/info.lst -num 1950 -w 20 -h 20 -vec positives.vec

$ opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 50 -h 50 -featureType LBP -precalcValBufSize 4096 -precalcIdxBufSize 4096
