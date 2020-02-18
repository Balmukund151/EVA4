5 Steps:-

1. setup+batch normalization --> Target reach Accuracy
	Result:- reaches 99.57% in 15 epochs with 301,984 params
	best train accuracy= 100%
	best test accuracy= 99.57%
	
	Analysis:-
	Base Model is heavy with 300k params but it has reached desired accuracy 99.4% + in 15 epochs.
	Gap between train accuracy(100%) and test accuracy(99.57%) is 0.42 which can be reduced with regularization.
	Target for next step is to 1st make model light weight and also also GAP.
	
2. reduce params to make model lightweight
	Result:-
	Params=7832
	best train accuracy= 99.65%
	best test accuracy= 99.21%
	
	Analysis:-
	Model has become lean with 7832 params but hasn't crossed the 99.4% accuracy mark.
	still Gap between train accuracy and test accuracy is 0.44%. So need to add regularization.
	Next add Dropouts

3. Add 	Dropouts
	results:-
	params=7832
	best train accuracy= 99.09%
	best test accuracy= 99.29%
	
	Analysis:-
	with dropout regularization it looks like there is underfitting as test accuracy is higher than train accuracy.
	Also GAP can be applied to reduce big kernals and then we can increase the capacity.
	In next step we will add GAP to reduce big kernels, so that in final step we can improve capacity.

4. Add GAP and add a conv block for adding capacity
	results:-
	params=8456
	best train accuracy= 99.00%
	best test accuracy= 99.29%
	
	Analysis:-
	Even after adding Gap and a conv block the train and test accuracy are not improved much.
	To improve target we will add Image Augmentation and remove dropout so that test accuracy also improves and croses target.
	

5. Add Image Augmentation and remove dropout
	results:-
	params=8456
	best train accuracy= 99.08%
	best test accuracy= 99.52% in 13th epoch and 99.42% in 12th epoch
	
	Analysis:-
	a. Applied Image Augmentation
	b. removed dropout
	c. reduced bacth size
	The combination of all the 3 above worked and improved the accuracy to more extent. Batch size was reduced to 64 which made it move to 99.52%. without batch size reduction it just made to 99.42% only once.
	