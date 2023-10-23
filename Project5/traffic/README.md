1st test:
-model has 7 layers: 1 convolution(size (3,3)) , 1 max pooling(size (2,2)) , 1 platten, 1 hidden player (NUM_CATEGORIES * 12 units, dropout 0.5), 1 output (NUM_CATEGORIES units)
-Accuracy: 0.4576
2nd test:
-add 2 layers: 1 convolution(size (3,3)) , 1 max pooling(size (2,2)) into model
-Accuracy: 0.9179
--Add more convolution and pooling got better accuracy
3rd test:
-add 1 hidden player (NUM_CATEGORIES * 12 units, dropout 0.5) into model
-Accuracy: 0.4931
--Add more hidden layers with same number of units reduce accuracy
4th test:
-change number of units of 2nd hidden player (NUM_CATEGORIES * 15 units) into model
-Accuracy: accuracy: 0.9006
--change number of units of 2nd hidden player increase accuracy
5th test:
-change all max pooling to average pooling(size (2,2))
-Accuracy: 0.9726 
--average pooling fit the data set, got better accuracy
6th test:
--Add 2 convolution(size (3,3)) before 1st average pooling and before 2nd average pooling
-Accuracy: accuracy: 0.9928
--Add more convolution got better accuracy
7th test:
--Add 1 convolution(size (3,3)) before 2nd average pooling
--Accuracy reduce a little bit
-- Reach limit convolution
8th:
add 1 hidden layer (NUM_CATEGORIES * 9 units, dropout 0.5) after 2nd hidden layer
--Accuracy: 0.9889
-- add hidden layer with smaller number of units not increase accuracy
8th:
change 3rd hidden layer (NUM_CATEGORIES * 18 units, dropout 0.5)
--Accuracy: accuracy: 0.9861
-- change hidden layer with higher number of units not increase accuracy, model overfitting, reach limit accuracy